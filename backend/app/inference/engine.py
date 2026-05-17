import torch
import timm
from torchvision import transforms
from PIL import Image
import io
import os
import time
import logging
import cv2
import numpy as np
import base64

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AI-Pipeline")

class PredictionEngine:
    def __init__(self, model_path="outputs/best_phase2.pth"):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.is_ready = False
        
        # ISIC Dataset Class Mapping (Turkish)
        self.class_names = [
            'Aktinik Keratoz',         # akiec
            'Bazal Hücreli Karsinom',  # bcc
            'Benign Keratoz',          # bkl
            'Dermatofibrom',           # df
            'Melanom',                 # mel
            'Melanositik Nevüs',       # nv
            'Vasküler Lezyon'          # vasc
        ]

        # EfficientNet-B4 standard resolution is 380x380
        self.input_size = 380
        self.transform = transforms.Compose([
            transforms.Resize(self.input_size + 32), 
            transforms.CenterCrop(self.input_size),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        
        self.model = self._load_model(model_path)
        self.gradients = None
        self.activations = None

    def _load_model(self, model_path):
        model = timm.create_model('efficientnet_b4', pretrained=False, num_classes=len(self.class_names))
        
        if os.path.exists(model_path):
            try:
                checkpoint = torch.load(model_path, map_location=self.device)
                state_dict = checkpoint if isinstance(checkpoint, dict) and 'state_dict' not in checkpoint else checkpoint.get('state_dict', checkpoint)
                model.load_state_dict(state_dict)
                self.is_ready = True
                logger.info(f"✅ Model loaded successfully from {model_path}")
            except Exception as e:
                logger.error(f"❌ Critical error loading model: {e}")
                raise RuntimeError(f"Could not load model state dict: {e}")
        else:
            logger.error(f"❌ Model checkpoint missing at {model_path}")
            self.is_ready = False
            
        model.to(self.device)
        model.eval()
        return model

    def save_gradient(self, grad):
        self.gradients = grad

    def save_activation(self, module, input, output):
        self.activations = output

    def generate_gradcam(self, input_tensor, target_class):
        # Attach hooks to the last convolutional layer
        target_layer = self.model.conv_head
        handle_act = target_layer.register_forward_hook(self.save_activation)
        # Use full_backward_hook for better reliability in newer Torch versions
        handle_grad = target_layer.register_full_backward_hook(lambda module, grad_in, grad_out: self.save_gradient(grad_out[0]))

        # Forward pass
        output = self.model(input_tensor)
        
        # Backward pass for the target class
        self.model.zero_grad()
        target_score = output[0][target_class]
        target_score.backward()

        # Remove hooks
        handle_act.remove()
        handle_grad.remove()

        # Generate heatmap logic
        # Weight the activations by the gradients
        weights = torch.mean(self.gradients, dim=(2, 3), keepdim=True)
        weighted_activations = weights * self.activations
        heatmap = torch.sum(weighted_activations, dim=1).squeeze()
        
        # ReLU on heatmap
        heatmap = np.maximum(heatmap.detach().cpu().numpy(), 0)
        
        # Normalize
        if np.max(heatmap) > 0:
            heatmap /= np.max(heatmap)
        
        return heatmap

    def predict(self, image_bytes, top_k=3):
        if not self.is_ready:
            logger.error("Attempted prediction with uninitialized model.")
            raise RuntimeError("AI model is not loaded.")

        start_time = time.time()
        try:
            # 1. Image Preprocessing
            orig_image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
            
            # To fix alignment, we MUST use the same crop for the background image
            # EfficientNet-B4 uses CenterCrop(380)
            preprocess_for_display = transforms.Compose([
                transforms.Resize(self.input_size + 32),
                transforms.CenterCrop(self.input_size)
            ])
            display_img_pil = preprocess_for_display(orig_image)
            img_cv = cv2.cvtColor(np.array(display_img_pil), cv2.COLOR_RGB2BGR)
            
            # Input tensor for model
            input_tensor = self.transform(orig_image).unsqueeze(0).to(self.device)
            
            # 2. Inference
            with torch.no_grad():
                outputs = self.model(input_tensor)
                probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
                
            top_prob, top_catid = torch.topk(probabilities, min(top_k, len(self.class_names)))
            
            predictions = []
            for i in range(top_prob.size(0)):
                predictions.append({
                    "class": self.class_names[top_catid[i]],
                    "confidence": float(top_prob[i]) * 100
                })
            
            # 3. Generate Grad-CAM Heatmap
            input_tensor.requires_grad = True
            heatmap_raw = self.generate_gradcam(input_tensor, top_catid[0])
            
            # 4. Post-process Heatmap (overlay on the CROPPED display image)
            heatmap_resized = cv2.resize(heatmap_raw, (self.input_size, self.input_size))
            heatmap_color = cv2.applyColorMap(np.uint8(255 * heatmap_resized), cv2.COLORMAP_JET)
            
            # Superimpose
            superimposed_img = cv2.addWeighted(img_cv, 0.6, heatmap_color, 0.4, 0)
            
            # Encode to Base64
            _, buffer = cv2.imencode('.jpg', superimposed_img)
            heatmap_base64 = base64.b64encode(buffer).decode('utf-8')
            
            inference_time = (time.time() - start_time) * 1000
            logger.info(f"Inference completed in {inference_time:.2f}ms")
            
            return {
                "predictions": predictions,
                "heatmap": f"data:image/jpeg;base64,{heatmap_base64}"
            }
        except Exception as e:
            logger.error(f"Prediction error: {e}")
            raise e

prediction_engine = PredictionEngine()



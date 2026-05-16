import torch
import timm
from torchvision import transforms
from PIL import Image
import io
import os
import time
import logging

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
            transforms.Resize(self.input_size + 32), # Resize slightly larger
            transforms.CenterCrop(self.input_size),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        
        self.model = self._load_model(model_path)

    def _load_model(self, model_path):
        # Initialize EfficientNet-B4 using timm
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
            # Do NOT fall back to uninitialized weights in production/presentation
            self.is_ready = False
            
        model.to(self.device)
        model.eval()
        return model

    def predict(self, image_bytes, top_k=3):
        if not self.is_ready:
            logger.error("Attempted prediction with uninitialized model.")
            raise RuntimeError("AI model is not loaded. Please check outputs/best_phase2.pth")

        start_time = time.time()
        try:
            image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
            input_tensor = self.transform(image).unsqueeze(0).to(self.device)
            
            with torch.no_grad():
                outputs = self.model(input_tensor)
                probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
                
            top_prob, top_catid = torch.topk(probabilities, min(top_k, len(self.class_names)))
            
            results = []
            for i in range(top_prob.size(0)):
                results.append({
                    "label": self.class_names[top_catid[i]],
                    "confidence": float(top_prob[i])
                })
            
            inference_time = (time.time() - start_time) * 1000
            logger.info(f"Inference completed in {inference_time:.2f}ms")
            
            return results
        except Exception as e:
            logger.error(f"Prediction error: {e}")
            raise e

prediction_engine = PredictionEngine()



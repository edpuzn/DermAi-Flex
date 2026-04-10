import { createI18n } from 'vue-i18n'

const messages = {
  tr: {
    app: {
      title: 'DermAI',
      subtitle: 'Yapay Zeka Destekli Cilt Analizi',
      online: 'Yapay Zeka Aktif',
      version: 'Sistem versiyonu 2.4.1 (Kararlı)'
    },
    nav: {
      home: 'Ana Sayfa',
      features: 'Özellikler',
      login: 'Sisteme Giriş Yap',
      dashboard: 'Panele Git',
      language: 'Dil',
    },
    landing: {
      heroTitle: 'Yapay Zeka Destekli Cilt Analizi',
      heroSubtitle: 'Klinik görüntüler ve raporlarla desteklenen yeni nesil dermatolojik tanı destek sistemi.',
      getStarted: 'Hemen Başlayın',
      learnMore: 'Nasıl Çalışır?',
      feature1Title: 'Çoklu Modalite',
      feature1Desc: 'Hem tıbbi görüntüleri hem de pdf raporlarını aynı anda analiz eder.',
      feature2Title: 'Yüksek Doğruluk',
      feature2Desc: 'Son teknoloji EfficientNet tabanlı derin öğrenme modeli.',
      feature3Title: 'Güvenli & Gizli',
      feature3Desc: 'HIPAA uyumlu, uçtan uca şifrelenmiş veri işleme altyapısı.',
      footer: '© 2026 DermaAI. Tüm hakları saklıdır.'
    },
    login: {
      welcome: 'Tekrar Hoş Geldiniz',
      instruction: 'Devam etmek için klinik bilgilerinizi girin.',
      email: 'E-posta adresi',
      emailPlaceholder: 'doktor@klinik.com',
      password: 'Şifre',
      passwordPlaceholder: '••••••••',
      remember: 'Beni 30 gün hatırla',
      forgot: 'Şifremi unuttum?',
      signin: 'Güvenli Giriş',
      authenticating: 'Doğrulanıyor...',
      hipaa: 'HIPAA Uyumlu',
      e2e: 'Uçtan Uca Şifreli',
      prompt: 'Gelişmiş multimodal dermatolojik analiz sistemi. Sisteme giriş yaparak resim ve rapor yükleyebilir, analiz başlatabilirsiniz.'
    },
    dashboard: {
      title: 'Multimodal Dermatolojik Analiz',
      subtitle: 'Tıbbi görüntü ve klinik raporları yükleyin. Sistemimiz cilt lezyonlarını değerlendirmenize yardımcı olmak için algoritmalarla çalışır.',
      imgTitle: 'Klinik Görüntü',
      imgDesc: 'Birincil cilt lezyonu görüntüsünü yükleyin.',
      pdfTitle: 'Medikal Rapor',
      pdfDesc: 'Histopatoloji veya klinik notlarınızı yükleyin.',
      multiTitle: 'Çoklu Modalite',
      multiDesc: 'Görüntü ve metin kullanarak kapsamlı yapay zeka analizi.',
      howItWorksTitle: 'Nasıl Çalışır?',
      howItWorksDesc: 'EfficientNet tabanlı model füzyon motorumuz görsel yapıları işler ve teşhis önerisi sunmak için NLP ile ilişkilendirir.',
      simComplete: 'Analiz tamamlandı! (Simülasyon)'
    },
    action: {
      ready: 'Analiz için hazır',
      processing: 'Klinik veriler işleniyor...',
      uploadReq: 'Devam etmek için klinik veri yükleyin',
      analyzeBtn: 'Analizi Başlat',
      analyzingBtn: 'Analiz Ediliyor...',
      browse: 'Dosya seçin',
      dragDrop: 'veya sürükleyip bırakın',
      addAnother: 'Başka dosya ekle',
      imgAccept: "10MB'a kadar JPG, PNG",
      pdfAccept: "10MB'a kadar PDF",
      multiAccept: "10MB'a kadar JPG, PNG ve PDF",
      errImg: 'Lütfen geçerli bir resim dosyası yükleyin.',
      errPdf: 'Lütfen geçerli bir PDF dosyası yükleyin.',
      remove: 'Kaldır'
    }
  },
  en: {
    app: {
      title: 'DermAI',
      subtitle: 'AI-Supported Skin Analysis',
      online: 'AI Engine Online',
      version: 'System version 2.4.1 (Stable)'
    },
    nav: {
      home: 'Home',
      features: 'Features',
      login: 'Sign in to System',
      dashboard: 'Go to Dashboard',
      language: 'Lang',
    },
    landing: {
      heroTitle: 'AI-Powered Dermatological Analysis',
      heroSubtitle: 'Next-generation dermatological diagnostic support system powered by clinical images and reports.',
      getStarted: 'Get Started',
      learnMore: 'How it Works',
      feature1Title: 'Multimodal',
      feature1Desc: 'Analyzes both medical images and pdf reports simultaneously.',
      feature2Title: 'High Accuracy',
      feature2Desc: 'State-of-the-art EfficientNet based deep learning model.',
      feature3Title: 'Secure & Private',
      feature3Desc: 'HIPAA compliant, end-to-end encrypted data processing.',
      footer: '© 2026 DermaAI. All rights reserved.'
    },
    login: {
      welcome: 'Welcome back',
      instruction: 'Please enter your clinic credentials to sign in.',
      email: 'Email address',
      emailPlaceholder: 'doctor@clinic.com',
      password: 'Password',
      passwordPlaceholder: '••••••••',
      remember: 'Remember me for 30 days',
      forgot: 'Forgot password?',
      signin: 'Sign in securely',
      authenticating: 'Authenticating...',
      hipaa: 'HIPAA Compliant',
      e2e: 'E2E Encrypted',
      prompt: 'Advanced multimodal dermatological analysis system. Sign in to access your dashboard, upload imagery, and generate AI-assisted clinical reports.'
    },
    dashboard: {
      title: 'Multimodal Dermatological Analysis',
      subtitle: 'Upload medical imagery and clinical reports. Our deep learning system analyzes visual and clinical data to assist dermatological evaluation.',
      imgTitle: 'Clinical Image',
      imgDesc: 'Upload primary skin lesion imagery.',
      pdfTitle: 'Medical Report',
      pdfDesc: 'Upload histopathology or clinical notes.',
      multiTitle: 'Multimodal Study',
      multiDesc: 'Comprehensive AI analysis using both image and clinical text.',
      howItWorksTitle: 'How it works',
      howItWorksDesc: 'Our EfficientNet-based model fusion engine processes visual structures and correlates them with clinical NLP markers from your reports to provide a synthesized diagnostic suggestion.',
      simComplete: 'Analysis complete! (Simulation)'
    },
    action: {
      ready: 'Ready for analysis',
      processing: 'Processing clinical data...',
      uploadReq: 'Please upload clinical data to continue',
      analyzeBtn: 'Run Analysis',
      analyzingBtn: 'Analyzing...',
      browse: 'Browse files',
      dragDrop: 'or drag and drop here',
      addAnother: 'Add another file',
      imgAccept: 'JPG, PNG up to 10MB',
      pdfAccept: 'PDF up to 10MB',
      multiAccept: 'JPG, PNG & PDF up to 10MB',
      errImg: 'Please upload a valid image file.',
      errPdf: 'Please upload a valid PDF file.',
      remove: 'Remove'
    }
  }
}

export default createI18n({
  legacy: false, 
  locale: 'tr', 
  fallbackLocale: 'en',
  messages
})

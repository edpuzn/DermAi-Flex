import { createI18n } from 'vue-i18n'

const messages = {
  tr: {
    app: {
      title: 'DermAI-Flex',
      subtitle: 'Yapay Zeka Destekli Cilt Analizi',
      online: 'Yapay Zeka Aktif',
      version: 'Sistem versiyonu 2.4.1 (Kararlı)'
    },
    nav: {
      home: 'Ana Sayfa',
      features: 'Özellikler',
      login: 'Sisteme Giriş Yap',
      dashboard: 'Analiz Paneli',
      language: 'Dil',
      backToDashboard: 'Panele Geri Dön'
    },
    login: {
      title: 'DermAI-Flex Giriş',
      subtitle: 'Güvenli klinik analiz portalına hoş geldiniz',
      username: 'Kullanıcı Adı',
      password: 'Şifre',
      submit: 'SİSTEME GİRİŞ YAP',
      processing: 'DOĞRULANIYOR...',
      demoAccess: 'DEMO ERİŞİMİ',
      demoUser: 'Kullanıcı',
      demoPass: 'Şifre',
      error: 'Geçersiz kullanıcı adı veya şifre!'
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
      simComplete: 'Analiz tamamlandı!'
    },
    action: {
      ready: 'Analiz için hazır',
      processing: 'Klinik veriler işleniyor...',
      uploadReq: 'Devam etmek için veri yükleyin',
      analyzeBtn: 'Analizi Başlat',
      analyzingBtn: 'Analiz Ediliyor...',
      browse: 'Dosya seçin',
      dragDrop: 'veya sürükleyin',
      addAnother: 'Dosya ekle',
      imgAccept: "10MB'a kadar JPG, PNG, WEBP",
      pdfAccept: "10MB'a kadar PDF",
      multiAccept: "Görüntü ve PDF (Maks 10MB)",
      errImg: 'Geçersiz resim formatı.',
      errPdf: 'Geçersiz PDF formatı.',
      remove: 'Kaldır',
      print: 'Yazdır',
      share: 'Paylaş'
    },
    results: {
      title: 'Analiz Sonuçları',
      visualAnalysis: 'Görsel Analiz',
      predictions: 'Hastalık Tahminleri',
      riskLevel: 'RİSK SEVİYESİ',
      urgentNote: 'Klinik değerlendirme önerilir',
      aiExplanation: 'Yapay Zeka Klinik Açıklaması',
      ragContext: 'Genişletilmiş Medikal Bağlam (RAG)',
      ocrDataTitle: 'Ayıklanan Tıbbi Veriler (OCR)',
      nextSteps: 'Önerilen Adımlar',
      clinicalNotes: 'Klinik Notlar',
      disclaimerTitle: 'DOKTOR YASAL UYARI',
      disclaimerText: 'Bu bir tıbbi teşhis değildir. Kararlar lisanslı bir tıp uzmanı tarafından verilmelidir.',
      visualDisclaimer: 'Isı haritası, yapay zekanın kararına en çok etki eden bölgeleri gösterir.',
      noData: 'Görüntülenecek veri bulunamadı.',
      risk: {
        high: "YÜKSEK RİSK",
        medium: "ORTA RİSK",
        low: "DÜŞÜK RİSK",
        findSpecialist: "Uzman Randevusu Al →",
        clinicalEvaluation: "Klinik muayene şarttır",
        mediumDesc: "Klinik muayene önerilir",
        lowDesc: "Rutin kontrol yeterlidir"
      },
      ragData: {
        similarCasesTitle: "Benzer Klinik Vakalar",
        similarCasesDesc: "Veritabanımızdaki 14 benzer vakaya dayanarak, dermatoskopik değerlendirme sonrası %85.7 oranında teşhis doğrulanmıştır.",
        defaultNotes: "Asimetri ve düzensiz sınırlar saptandı. Lezyon sınır uyumsuzluğu saptandı.",
        defaultSteps: [
          "48 saat içinde biyopsi planlayın",
          "Güneş maruziyetinden kaçının",
          "Lezyon boyutundaki değişimleri belgeleyin"
        ]
      }
    }
  },
  en: {
    app: {
      title: 'DermAI-Flex',
      subtitle: 'AI-Powered Skin Analysis',
      online: 'AI Engine Online',
      version: 'System v2.4.1 (Stable)'
    },
    nav: {
      home: 'Home',
      features: 'Features',
      login: 'Sign in',
      dashboard: 'Analysis Panel',
      language: 'Language',
      backToDashboard: 'Back to Dashboard'
    },
    login: {
      title: 'DermAI-Flex Login',
      subtitle: 'Welcome to the secure clinical analysis portal',
      username: 'Username',
      password: 'Password',
      submit: 'SIGN IN TO SYSTEM',
      processing: 'AUTHENTICATING...',
      demoAccess: 'DEMO ACCESS',
      demoUser: 'User',
      demoPass: 'Pass',
      error: 'Invalid username or password!'
    },
    dashboard: {
      title: 'Multimodal Dermatological Analysis',
      subtitle: 'Upload medical imagery and clinical reports for AI-assisted evaluation.',
      imgTitle: 'Clinical Image',
      imgDesc: 'Upload primary skin lesion imagery.',
      pdfTitle: 'Medical Report',
      pdfDesc: 'Upload histopathology or clinical notes.',
      multiTitle: 'Multimodal Study',
      multiDesc: 'Comprehensive analysis using image and clinical text.',
      howItWorksTitle: 'How it works',
      howItWorksDesc: 'Our EfficientNet-based engine processes visual structures and correlates them with clinical markers.',
      simComplete: 'Analysis complete!'
    },
    action: {
      ready: 'Ready for analysis',
      processing: 'Processing data...',
      uploadReq: 'Upload data to continue',
      analyzeBtn: 'Run Analysis',
      analyzingBtn: 'Analyzing...',
      browse: 'Browse files',
      dragDrop: 'or drag here',
      addAnother: 'Add file',
      imgAccept: 'JPG, PNG, WEBP up to 10MB',
      pdfAccept: 'PDF up to 10MB',
      multiAccept: 'Image & PDF (Max 10MB)',
      errImg: 'Invalid image format.',
      errPdf: 'Invalid PDF format.',
      remove: 'Remove',
      print: 'Print',
      share: 'Share'
    },
    results: {
      title: 'Analysis Results',
      visualAnalysis: 'Visual Analysis',
      predictions: 'Disease Predictions',
      riskLevel: 'RISK LEVEL',
      urgentNote: 'Clinical evaluation recommended',
      aiExplanation: 'AI Clinical Explanation',
      ragContext: 'Extended Medical Context (RAG)',
      ocrDataTitle: 'Extracted Medical Data (OCR)',
      nextSteps: 'Recommended Next Steps',
      clinicalNotes: 'Clinical Notes',
      disclaimerTitle: 'PHYSICIAN DISCLAIMER',
      disclaimerText: 'This is not a medical diagnosis. Decisions must be made by a licensed professional.',
      visualDisclaimer: 'Heatmap indicates regions that most influenced the AI decision.',
      noData: 'No analysis data found.',
      risk: {
        high: "HIGH RISK",
        medium: "MEDIUM RISK",
        low: "LOW RISK",
        findSpecialist: "Find Specialist →",
        clinicalEvaluation: "Clinical exam required",
        mediumDesc: "Clinical evaluation recommended",
        lowDesc: "Routine follow-up is sufficient"
      },
      ragData: {
        similarCasesTitle: "Similar Clinical Cases",
        similarCasesDesc: "Based on 14 similar cases, 85.7% confirmed diagnosis following evaluation.",
        defaultNotes: "Asymmetry and irregular borders detected. High confidence in lesion boundary mismatch.",
        defaultSteps: [
          "Schedule biopsy within 48h",
          "Avoid sun exposure",
          "Document size changes"
        ]
      }
    }
  }
}

export default createI18n({
  legacy: false, 
  locale: 'tr', 
  fallbackLocale: 'en',
  messages
})

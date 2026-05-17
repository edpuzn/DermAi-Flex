<template>
  <div class="min-h-screen bg-gray-50 pb-24">
    <!-- Header -->
    <header class="bg-white border-b border-gray-200 sticky top-0 z-10 shadow-sm">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex items-center justify-between">
        <router-link to="/dashboard" class="flex items-center text-gray-500 hover:text-indigo-600 transition-colors group">
          <svg class="w-5 h-5 mr-2 transform group-hover:-translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path>
          </svg>
          <span class="font-semibold">{{ $t('nav.backToDashboard') }}</span>
        </router-link>
        
        <div class="flex items-center space-x-3">
          <div class="bg-indigo-600 p-2 rounded-lg text-white">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
            </svg>
          </div>
          <h1 class="text-lg font-bold text-gray-900">Laboratuvar Analiz Sonuçları</h1>
        </div>
        
        <div class="flex items-center space-x-3">
          <button @click="exportReport" class="p-2 text-gray-400 hover:text-indigo-600 hover:bg-indigo-50 rounded-lg transition-all" title="Yazdır">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4H9v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"></path>
            </svg>
          </button>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div v-if="store.analysisResult" class="grid grid-cols-1 lg:grid-cols-12 gap-8">
        
        <!-- Left Column: Risk & Disclaimers -->
        <div class="lg:col-span-5 space-y-6">
          
          <!-- Risk Level Card (Exactly matching ResultPage.vue style) -->
          <div :class="['bg-white rounded-2xl shadow-sm border p-6 flex items-center justify-between overflow-hidden relative transition-all duration-500', riskConfig.borderClass]">
            <div :class="['absolute top-0 right-0 w-32 h-full -skew-x-12 transform translate-x-16 transition-all duration-500', riskConfig.bgSkewClass]"></div>
            <div>
              <h3 class="text-sm font-bold text-gray-500 uppercase tracking-widest mb-1">{{ $t('results.riskLevel') }}</h3>
              <div class="flex items-center">
                <span :class="['text-3xl font-black transition-colors duration-500 uppercase', riskConfig.textClass]">{{ $t(riskConfig.labelText) }}</span>
                <span class="ml-3 flex h-3 w-3 relative">
                  <span :class="['animate-ping absolute inline-flex h-full w-full rounded-full opacity-75 transition-colors duration-500', riskConfig.pingClass]"></span>
                  <span :class="['relative inline-flex rounded-full h-3 w-3 transition-colors duration-500', riskConfig.dotClass]"></span>
                </span>
              </div>
            </div>
            <div class="text-right z-10">
              <p class="text-xs text-gray-500 font-medium transition-colors duration-500">{{ $t(riskConfig.descriptionText) }}</p>
              <button @click="exportReport" class="mt-2 text-sm font-bold text-indigo-600 hover:text-indigo-800 transition-colors uppercase tracking-widest text-[10px]">Hekim Raporu Oluştur</button>
            </div>
          </div>

          <!-- Doctor Disclaimer Box (Exactly matching ResultPage.vue style) -->
          <div class="bg-white rounded-2xl shadow-sm border border-gray-200 p-6">
            <h3 class="font-bold text-gray-900 mb-4 flex items-center">
              <svg class="w-5 h-5 text-gray-400 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path>
              </svg>
              Klinik Karar Bildirgesi
            </h3>
            <p class="text-xs text-gray-500 leading-relaxed">
              <span class="font-bold uppercase text-gray-700 block mb-1.5">TIBBİ YASAL UYARI:</span> 
              {{ store.analysisResult.disclaimer }}
            </p>
          </div>

          <!-- Action Buttons Console -->
          <div class="flex flex-col gap-4">
            <button @click="exportReport" class="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-3.5 px-6 rounded-xl shadow-lg shadow-indigo-100 transition-all flex items-center justify-center group text-sm uppercase tracking-wide">
              <svg class="w-5 h-5 mr-2 group-hover:scale-110 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4H9v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"></path>
              </svg>
              Yazdır / Resmi A4 Raporu Al
            </button>
            <router-link to="/dashboard" class="w-full bg-white border border-gray-200 hover:bg-gray-50 text-gray-700 font-bold py-3.5 px-6 rounded-xl transition-all flex items-center justify-center text-sm uppercase tracking-wide">
              Yeni Rapor Analiz Et
            </router-link>
          </div>

        </div>

        <!-- Right Column: AI Analysis & RAG (Exactly matching ResultPage.vue style) -->
        <div class="lg:col-span-7 space-y-6">
          <div class="bg-white rounded-2xl shadow-sm border border-gray-200 p-6 min-h-[500px] flex flex-col">
            <h3 class="font-bold text-gray-900 mb-4 flex items-center flex-shrink-0">
              <svg class="w-5 h-5 mr-2 text-indigo-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
              </svg>
              Tahlil & Klinik Değerlendirme Raporu
            </h3>
            
            <div class="flex-grow overflow-y-auto pr-2 custom-scrollbar">
              <div class="prose prose-indigo max-w-none">
                <div class="explanation-html text-gray-600 leading-relaxed text-sm" v-html="processedExplanation"></div>
              </div>
            </div>
          </div>
        </div>

      </div>

      <!-- No Data View -->
      <div v-else class="flex flex-col items-center justify-center py-20 bg-white border border-gray-200 rounded-2xl shadow-sm">
        <div class="animate-pulse flex flex-col items-center">
          <div class="w-16 h-16 bg-gray-100 rounded-full mb-6 flex items-center justify-center text-gray-300">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
            </svg>
          </div>
          <div class="h-4 w-48 bg-gray-100 rounded mb-3"></div>
          <div class="h-3 w-32 bg-gray-100 rounded"></div>
        </div>
        <p class="mt-8 text-gray-500 font-bold uppercase tracking-wider text-xs">Analiz Kaydı Bulunamadı</p>
        <router-link to="/dashboard" class="mt-4 bg-indigo-600 text-white font-bold px-6 py-2.5 rounded-lg text-xs uppercase hover:bg-indigo-700 transition-colors shadow-md">{{ $t('nav.backToDashboard') }}</router-link>
      </div>
    </main>

    <!-- Patient Information Form Modal -->
    <div v-if="showPatientFormModal" class="fixed inset-0 z-[70] flex items-center justify-center p-4 bg-black/80 backdrop-blur-md animate-fade-in">
      <div class="bg-white rounded-2xl shadow-[0_40px_100px_-20px_rgba(0,0,0,0.7)] overflow-hidden animate-scale-up border border-gray-100 max-w-[500px] w-full">
        <div class="px-8 py-6 border-b border-gray-100 bg-gray-50/50 flex items-center justify-between">
          <div>
            <h2 class="text-sm font-black text-gray-900 uppercase tracking-wider">HASTA KAYIT VE RAPORLAMA</h2>
            <p class="text-[9px] text-indigo-600 font-bold uppercase tracking-widest mt-1">Dijital Klinik Rapor Girişi</p>
          </div>
          <button @click="showPatientFormModal = false" class="text-gray-400 hover:text-gray-900 transition-colors">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
        </div>

        <div class="p-8 space-y-6">
          <div class="space-y-2">
            <div class="flex justify-between items-center">
              <label class="text-xs font-bold text-gray-700 uppercase tracking-wide">Hastanın Adı Soyadı</label>
              <span v-if="errors.name" class="text-[10px] font-bold text-red-600 uppercase">{{ errors.name }}</span>
            </div>
            <input 
              v-model="patientInfo.name" 
              type="text" 
              @input="validateForm"
              placeholder="Örn: Ahmet Yılmaz" 
              class="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-sm font-bold text-gray-900 focus:bg-white focus:border-indigo-600 focus:ring-4 focus:ring-indigo-500/10 outline-none transition-all placeholder:text-gray-300" 
            />
          </div>

          <div class="grid grid-cols-2 gap-5">
            <div class="space-y-2">
              <div class="flex justify-between items-center">
                <label class="text-xs font-bold text-gray-700 uppercase tracking-wide">TC Kimlik / Protokol</label>
                <span v-if="errors.id" class="text-[10px] font-bold text-red-600 uppercase">!</span>
              </div>
              <input 
                v-model="patientInfo.id" 
                type="text" 
                maxlength="11"
                @input="validateForm"
                placeholder="11 Haneli" 
                class="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-sm font-bold text-gray-900 focus:bg-white focus:border-indigo-600 focus:ring-4 focus:ring-indigo-500/10 outline-none transition-all placeholder:text-gray-300"
              />
            </div>
            <div class="space-y-2">
              <div class="flex justify-between items-center">
                <label class="text-xs font-bold text-gray-700 uppercase tracking-wide">Hasta Yaşı</label>
                <span v-if="errors.age" class="text-[10px] font-bold text-red-600 uppercase">!</span>
              </div>
              <input 
                v-model="patientInfo.age" 
                type="number" 
                @input="validateForm"
                placeholder="Örn: 42" 
                class="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-sm font-bold text-gray-900 focus:bg-white focus:border-indigo-600 focus:ring-4 focus:ring-indigo-500/10 outline-none transition-all placeholder:text-gray-300"
              />
            </div>
          </div>

          <div class="space-y-3 pt-2">
            <label class="text-xs font-bold text-gray-700 uppercase tracking-wide">Cinsiyet</label>
            <div class="grid grid-cols-3 gap-3">
              <button 
                v-for="g in ['ERKEK', 'KADIN', 'DİĞER']" 
                :key="g"
                @click="patientInfo.gender = g"
                :class="patientInfo.gender === g ? 'bg-indigo-600 text-white border-indigo-600 shadow-lg shadow-indigo-100' : 'bg-white text-gray-500 border-gray-200 hover:border-indigo-200'"
                class="py-3 text-xs font-bold rounded-xl border-2 transition-all uppercase tracking-tighter"
              >
                {{ g }}
              </button>
            </div>
          </div>
        </div>

        <div class="px-8 pb-8 flex flex-col space-y-4">
          <button 
            @click="startGenerationProcess" 
            :disabled="hasErrors"
            :class="hasErrors ? 'bg-gray-100 text-gray-300 cursor-not-allowed' : 'bg-indigo-600 text-white hover:bg-indigo-700 shadow-xl shadow-indigo-100'"
            class="w-full py-4 rounded-xl font-black text-sm uppercase tracking-widest transition-all"
          >
            Resmi A4 Raporunu Derle ve Yazdır
          </button>
          <button @click="generateAnonymousReport" class="text-xs font-bold text-gray-400 hover:text-indigo-600 transition-colors uppercase tracking-widest text-center">Anonim Olarak Devam Et</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, reactive, computed } from 'vue'
import { useAnalysisStore } from '../stores/analysis'

const store = useAnalysisStore()
const showPatientFormModal = ref(false)

// Unique Reference Protocol Code
const currentProtocol = ref('')

onMounted(() => {
  currentProtocol.value = Math.floor(Math.random() * 900000 + 100000).toString()
})

// Custom SVGs for Medical Report Sections
const analysisSummaryIcon = `
  <svg class="w-5 h-5 mr-2 text-indigo-600 inline-block align-middle flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24" style="display: inline-block; vertical-align: middle;">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"></path>
  </svg>
`

const clinicalCorrelationIcon = `
  <svg class="w-5 h-5 mr-2 text-teal-600 inline-block align-middle flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24" style="display: inline-block; vertical-align: middle;">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"></path>
  </svg>
`

const nextStepsIcon = `
  <svg class="w-5 h-5 mr-2 text-emerald-600 inline-block align-middle flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24" style="display: inline-block; vertical-align: middle;">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path>
  </svg>
`

const processedExplanation = computed(() => {
  if (!store.analysisResult?.explanation) return ''

  let processed = store.analysisResult.explanation

  // Emojis strip to keep it clean & clinical
  processed = processed.replace(/[\u{1F300}-\u{1F9FF}]|[\u{2700}-\u{27BF}]|[\u{2600}-\u{26FF}]/gu, '')

  // 1. Analiz Özeti
  processed = processed.replace(
    /<h3>(?:🔍\s*)?Analiz Özeti<\/h3>/g,
    `<h3 class="flex items-center text-indigo-950 font-black text-sm uppercase tracking-wider border-b border-gray-150 pb-2 mt-6 mb-3 group hover:text-indigo-600">${analysisSummaryIcon} Analiz Bulguları ve Özeti</h3>`
  )

  // 2. Klinik Korelasyon
  processed = processed.replace(
    /<h3>(?:🧪\s*)?Klinik Korelasyon<\/h3>/g,
    `<h3 class="flex items-center text-teal-950 font-black text-sm uppercase tracking-wider border-b border-gray-150 pb-2 mt-6 mb-3 group hover:text-teal-600">${clinicalCorrelationIcon} Tıbbi ve Klinik Korelasyon</h3>`
  )

  // 3. Önerilen Sonraki Adımlar
  processed = processed.replace(
    /<h3>(?:🚀\s*)?(?:Önerilen Sonraki Adımlar|Önerilen Adımlar)<\/h3>/g,
    `<h3 class="flex items-center text-emerald-950 font-black text-sm uppercase tracking-wider border-b border-gray-150 pb-2 mt-6 mb-3 group hover:text-emerald-600">${nextStepsIcon} Hekim Karar Yol Haritası ve Öneriler</h3>`
  )

  return processed
})

const riskConfig = computed(() => {
  const level = store.analysisResult?.risk_level?.toLowerCase() || 'medium'
  
  if (level === 'high') {
    return {
      textClass: 'text-red-650 font-black',
      pingClass: 'bg-red-400',
      dotClass: 'bg-red-500',
      bgSkewClass: 'bg-red-500/5',
      borderClass: 'border-red-200',
      labelText: 'results.risk.high',
      descriptionText: 'results.risk.clinicalEvaluation'
    }
  } else if (level === 'low') {
    return {
      textClass: 'text-emerald-650 font-black',
      pingClass: 'bg-emerald-400',
      dotClass: 'bg-emerald-500',
      bgSkewClass: 'bg-emerald-500/5',
      borderClass: 'border-emerald-200',
      labelText: 'results.risk.low',
      descriptionText: 'results.risk.lowDesc'
    }
  } else {
    return {
      textClass: 'text-amber-650 font-black',
      pingClass: 'bg-amber-400',
      dotClass: 'bg-amber-500',
      bgSkewClass: 'bg-amber-500/5',
      borderClass: 'border-amber-200',
      labelText: 'results.risk.medium',
      descriptionText: 'results.risk.mediumDesc'
    }
  }
})

const processExplanationForReport = (html) => {
  if (!html) return ''

  let processed = html

  const summaryIcon = `
    <svg class="w-4 h-4 mr-2 text-black inline-block" fill="none" stroke="currentColor" viewBox="0 0 24 24" style="display: inline-block; vertical-align: middle;">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"></path>
    </svg>
  `

  const correlationIcon = `
    <svg class="w-4 h-4 mr-2 text-black inline-block" fill="none" stroke="currentColor" viewBox="0 0 24 24" style="display: inline-block; vertical-align: middle;">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"></path>
    </svg>
  `

  const stepsIcon = `
    <svg class="w-4 h-4 mr-2 text-black inline-block" fill="none" stroke="currentColor" viewBox="0 0 24 24" style="display: inline-block; vertical-align: middle;">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path>
    </svg>
  `

  // Headings formatted for printable report
  processed = processed.replace(
    /<h3>(?:🔍\s*)?Analiz Özeti<\/h3>/g,
    `<h3>${summaryIcon} Analiz Bulguları ve Özeti</h3>`
  )

  processed = processed.replace(
    /<h3>(?:🧪\s*)?Klinik Korelasyon<\/h3>/g,
    `<h3>${correlationIcon} Tıbbi ve Klinik Korelasyon</h3>`
  )

  processed = processed.replace(
    /<h3>(?:🚀\s*)?(?:Önerilen Sonraki Adımlar|Önerilen Adımlar)<\/h3>/g,
    `<h3>${stepsIcon} Hekim Karar Yol Haritası ve Öneriler</h3>`
  )

  return processed
}

const patientInfo = reactive({
  name: '',
  id: '',
  age: '',
  gender: 'ERKEK'
})

const errors = reactive({
  name: '',
  id: '',
  age: ''
})

const hasErrors = computed(() => {
  return errors.name !== '' || errors.id !== '' || errors.age !== ''
})

const validateForm = () => {
  if (patientInfo.name && /\d/.test(patientInfo.name)) {
    errors.name = 'İsim rakam içeremez'
  } else {
    errors.name = ''
  }

  if (patientInfo.id && !/^\d{11}$/.test(patientInfo.id)) {
    errors.id = 'TC 11 hane olmalıdır'
  } else {
    errors.id = ''
  }

  if (patientInfo.age !== '' && patientInfo.age < 0) {
    errors.age = 'Yaş negatif olamaz'
  } else {
    errors.age = ''
  }
}

const exportReport = () => {
  showPatientFormModal.value = true
}

const generateAnonymousReport = () => {
  patientInfo.name = 'ANONİM HASTA'
  patientInfo.id = '---'
  patientInfo.age = '---'
  startGenerationProcess()
}

const startGenerationProcess = () => {
  showPatientFormModal.value = false
  if (!store.analysisResult) return

  const reportId = `REF-${Math.random().toString(36).substring(7).toUpperCase()}`
  const date = new Date().toLocaleString('tr-TR')

  const reportHtml = `
    <!DOCTYPE html>
    <html lang="tr">
    <head>
      <meta charset="UTF-8">
      <title>Klinik Analiz Raporu - ${reportId}</title>
      <script src="https://cdn.tailwindcss.com"><\/script>
      <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap');
        body { font-family: 'Inter', sans-serif; -webkit-print-color-adjust: exact; margin: 0; padding: 0; color: #000; }
        @media print {
          .no-print { display: none; }
          @page { margin: 15mm; size: A4; }
        }
        .section-title { border-bottom: 2px solid #000; padding-bottom: 4px; margin-bottom: 16px; font-weight: 800; text-transform: uppercase; font-size: 11px; letter-spacing: 1px; }
        .data-table th { background: #f3f4f6; text-align: left; padding: 8px; font-size: 10px; border-bottom: 1px solid #000; }
        .data-table td { padding: 8px; font-size: 11px; border-bottom: 1px solid /deep/ #e5e7eb; }
        .report-explanation h3 {
          display: flex;
          align-items: center;
          font-size: 11px;
          font-weight: 800;
          text-transform: uppercase;
          border-bottom: 1px solid #000;
          padding-bottom: 4px;
          margin-top: 20px;
          margin-bottom: 10px;
          color: #000;
        }
        .report-explanation p { margin-bottom: 8px; }
        .report-explanation ul { list-style-type: disc; padding-left: 16px; margin-bottom: 12px; }
        .report-explanation li { margin-bottom: 4px; }
      </style>
    </head>
    <body class="bg-gray-100">
      <div class="max-w-[210mm] mx-auto bg-white p-[20mm] shadow-none min-h-screen">
        
        <!-- Hospital Header -->
        <div class="flex justify-between items-start mb-10">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 border-2 border-black flex items-center justify-center font-black text-xl">H</div>
            <div>
              <h1 class="text-lg font-black leading-none uppercase">DERMAI-FLEX TANI MERKEZİ</h1>
              <p class="text-[9px] font-medium text-gray-500 mt-1">Dijital Dermatoloji ve Analitik Görüntüleme Birimi</p>
            </div>
          </div>
          <div class="text-[9px] text-right font-medium text-gray-400 leading-tight">
            <p>Rapor No: ${reportId}</p>
            <p>Tarih: ${date}</p>
            <p>Protokol: PRT-${currentProtocol.value || Math.floor(Math.random() * 900000 + 100000)}</p>
          </div>
        </div>

        <!-- Patient Info -->
        <div class="grid grid-cols-2 gap-10 mb-10 border border-black p-5">
           <div class="space-y-2">
              <p class="text-[10px]"><span class="font-bold w-24 inline-block">HASTA ADI:</span> <span class="uppercase">${patientInfo.name || 'ANONİM HASTA'}</span></p>
              <p class="text-[10px]"><span class="font-bold w-24 inline-block">TC KİMLİK:</span> ${patientInfo.id || '---'}</p>
              <p class="text-[10px]"><span class="font-bold w-24 inline-block">YAŞ:</span> ${patientInfo.age || '---'}</p>
           </div>
           <div class="space-y-2">
              <p class="text-[10px]"><span class="font-bold w-24 inline-block">CİNSİYET:</span> ${patientInfo.gender}</p>
              <p class="text-[10px]"><span class="font-bold w-24 inline-block">GÖNDEREN BİRİM:</span> DERMATOLOJİ POLİKLİNİĞİ</p>
              <p class="text-[10px]"><span class="font-bold w-24 inline-block">İSTENEN TETKİK:</span> AI DESTEKLİ LABORATUVAR TAHLİL ANALİZİ</p>
           </div>
        </div>

        <!-- Section I: Findings -->
        <div class="mb-10">
          <h3 class="section-title">I. LABORATUVAR VE BULGU KAYITLARI</h3>
          <div class="border border-black p-5 bg-gray-50 text-[10px] leading-relaxed font-mono whitespace-pre-line text-justify max-h-[500px] overflow-hidden">
            ${store.analysisResult.ocr_text || 'Laboratuvar tahlil/metin bulgusu bulunamadı.'}
          </div>
          <p class="text-[9px] font-bold mt-2 text-center">YÜKLENEN TIBBİ RAPOR OCR VERİ KAYDI</p>
        </div>

        <!-- Section II: AI Reasoning -->
        <div class="mb-10">
          <h3 class="section-title">II. YAPAY ZEKA DESTEKLİ KLİNİK DEĞERLENDİRME (RAG SENTEZİ)</h3>
          <div class="text-[11px] leading-relaxed text-justify space-y-3 report-explanation">
            ${processExplanationForReport(store.analysisResult.explanation)}
          </div>
        </div>

        <!-- Section III: Conclusion -->
        <div class="mb-16">
          <h3 class="section-title">III. SONUÇ VE RİSK ANALİZİ</h3>
          <div class="flex items-center space-x-4 border-2 border-black p-5">
             <div class="text-[10px] font-bold uppercase">SİSTEMATİK RİSK SKORU:</div>
             <div class="text-2xl font-black">${store.analysisResult.risk_level.toUpperCase()}</div>
             <div class="flex-grow text-[9px] text-gray-500 italic pl-10">
                * Bu sonuç bir uzman görüşü yerine geçmez, sadece klinik karar destek amaçlı üretilmiştir.
             </div>
          </div>
        </div>

        <!-- Footer / Signature -->
        <div class="mt-auto border-t border-black pt-8">
           <div class="flex justify-between items-start">
              <div class="text-[8px] text-gray-400 max-w-sm">
                 Bu döküman elektronik ortamda DermAI-Flex Analiz Motoru tarafından üretilmiştir. 
                 Yasal Sorumluluk Reddi: ${store.analysisResult.disclaimer}
              </div>
              <div class="text-center w-64 space-y-4">
                 <div class="h-10"></div>
                 <div class="space-y-1">
                    <p class="text-[10px] font-bold">UZM. DR. [ONAYLAYAN HEKİM]</p>
                    <p class="text-[8px] font-medium text-gray-400 italic">Elektronik Olarak İmzalanmıştır</p>
                 </div>
              </div>
           </div>
        </div>

        <!-- No Print Controls -->
        <div class="no-print fixed bottom-8 right-8 flex space-x-3">
           <button onclick="window.close()" class="bg-gray-100 text-gray-600 font-bold py-3 px-6 rounded text-xs hover:bg-gray-200">İptal</button>
           <button onclick="window.print()" class="bg-black text-white font-bold py-3 px-8 rounded text-xs hover:opacity-90">RAPORU YAZDIR / PDF OLARAK KAYDET</button>
        </div>
      </div>
    </body>
    </html>
  `

  const printWindow = window.open('', '_blank')
  printWindow.document.write(reportHtml)
  printWindow.document.close()
  
  setTimeout(() => {
    printWindow.print()
    printWindow.close()
  }, 250)
}
</script>

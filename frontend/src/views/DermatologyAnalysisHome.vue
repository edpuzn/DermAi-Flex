<template>
  <div class="min-h-screen bg-gray-50 text-gray-900 font-sans pb-24">
    <!-- Header -->
    <header class="bg-white border-b border-gray-200 sticky top-0 z-10 shadow-sm">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex items-center justify-between">
        <div class="flex items-center space-x-3">
          <div class="bg-gradient-to-br from-indigo-500 to-indigo-700 p-2.5 rounded-lg text-white shadow-sm">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 3v2m6-2v2M9 19v2m6-2v2M5 9H3m2 6H3m18-6h-2m2 6h-2M7 19h10a2 2 0 002-2V7a2 2 0 00-2-2H7a2 2 0 00-2 2v10a2 2 0 002 2zM9 9h6v6H9V9z"></path></svg>
          </div>
          <div>
            <h1 class="text-xl font-bold text-gray-900 leading-tight tracking-tight">{{ $t('app.title') }}</h1>
            <p class="text-[10px] text-indigo-600 font-bold tracking-wider uppercase">{{ $t('app.subtitle') }}</p>
          </div>
        </div>
        <div class="flex items-center space-x-4">
          <div class="inline-flex items-center p-1 bg-gray-100/80 backdrop-blur-sm rounded-full border border-gray-200 shadow-inner">
            <button @click="$i18n.locale = 'tr'" :class="$i18n.locale === 'tr' ? 'bg-white text-indigo-600 shadow-sm' : 'text-gray-500 hover:text-gray-800'" class="px-3 py-1 text-xs font-bold rounded-full transition-all duration-300">TR</button>
            <button @click="$i18n.locale = 'en'" :class="$i18n.locale === 'en' ? 'bg-white text-indigo-600 shadow-sm' : 'text-gray-500 hover:text-gray-800'" class="px-3 py-1 text-xs font-bold rounded-full transition-all duration-300">EN</button>
          </div>
          <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-semibold bg-indigo-50 text-indigo-700 border border-indigo-100 shadow-sm hidden sm:inline-flex">
            <span class="w-2 h-2 bg-green-500 rounded-full mr-2 animate-pulse"></span>
            {{ $t('app.online') }}
          </span>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      <div class="text-center mb-10">
        <h2 class="text-3xl font-extrabold text-gray-900 sm:text-4xl tracking-tight">
          {{ $t('dashboard.title') }}
        </h2>
        <p class="mt-4 text-lg text-gray-500 max-w-2xl mx-auto leading-relaxed">
          {{ $t('dashboard.subtitle') }}
        </p>
      </div>

      <!-- Upload Grid -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <UploadCard 
          type="image" 
          :title="$t('dashboard.imgTitle')" 
          :description="$t('dashboard.imgDesc')"
          accept="image/jpeg, image/png"
          @file-selected="(f) => imageFile = f"
          @error="showError"
          :file="imageFile"
          @remove="imageFile = null"
        >
          <template #icon>
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
          </template>
        </UploadCard>
        
        <UploadCard 
          type="pdf" 
          :title="$t('dashboard.pdfTitle')" 
          :description="$t('dashboard.pdfDesc')"
          accept="application/pdf"
          @file-selected="(f) => pdfFile = f"
          @error="showError"
          :file="pdfFile"
          @remove="pdfFile = null"
        >
          <template #icon>
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
          </template>
        </UploadCard>
        
        <UploadCard 
          type="combined" 
          :title="$t('dashboard.multiTitle')" 
          :description="$t('dashboard.multiDesc')"
          accept="image/jpeg, image/png, application/pdf"
          @file-selected="handleCombinedSelected"
          @error="showError"
          :files="combinedFiles"
          @remove="(index) => combinedFiles.splice(index, 1)"
          :highlight="true"
        >
           <template #icon>
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"></path></svg>
          </template>
        </UploadCard>
      </div>
      
      <!-- Info Section -->
      <div class="bg-blue-50/50 border border-blue-100 rounded-xl p-5 mt-8 flex items-start gap-4 transition-all hover:bg-blue-50">
        <div class="mt-0.5 text-blue-500">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
        </div>
        <div>
          <h4 class="text-sm font-semibold text-blue-900">{{ $t('dashboard.howItWorksTitle') }}</h4>
          <p class="text-sm text-blue-800/80 mt-1 leading-relaxed">{{ $t('dashboard.howItWorksDesc') }}</p>
        </div>
      </div>

      <!-- Action Bar -->
      <ActionBar 
        :is-valid="canAnalyze" 
        :is-analyzing="isAnalyzing" 
        @analyze="runAnalysis" 
      />
      
      <!-- Toast/Error Messages -->
      <transition 
        enter-active-class="transform ease-out duration-300 transition" 
        enter-from-class="translate-y-2 opacity-0 sm:translate-y-0 sm:translate-x-2" 
        enter-to-class="translate-y-0 opacity-100 sm:translate-x-0" 
        leave-active-class="transition ease-in duration-100" 
        leave-from-class="opacity-100" 
        leave-to-class="opacity-0"
      >
        <div v-if="errorMsg" class="fixed top-24 right-4 z-50 rounded-lg bg-red-50 p-4 shadow-lg border border-red-200 max-w-sm w-full pointer-events-auto">
          <div class="flex">
            <div class="flex-shrink-0">
              <svg class="h-5 w-5 text-red-400" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd" /></svg>
            </div>
            <div class="ml-3">
              <p class="text-sm font-medium text-red-800">{{ errorMsg }}</p>
            </div>
            <div class="ml-auto pl-3">
              <button @click="errorMsg = ''" class="inline-flex rounded-md bg-red-50 text-red-500 hover:bg-red-100 focus:outline-none focus:ring-2 focus:ring-red-600 focus:ring-offset-2">
                <span class="sr-only">Dismiss</span>
                <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
              </button>
            </div>
          </div>
        </div>
      </transition>
    </main>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useI18n } from 'vue-i18n'
import UploadCard from '../components/UploadCard.vue'
import ActionBar from '../components/ActionBar.vue'

const { t } = useI18n()

// State
const imageFile = ref(null)
const pdfFile = ref(null)
const combinedFiles = ref([])

const isAnalyzing = ref(false)
const errorMsg = ref('')

// Computed validation
const canAnalyze = computed(() => {
  return imageFile.value !== null || 
         pdfFile.value !== null || 
         combinedFiles.value.length > 0
})

// Methods
const handleCombinedSelected = (files) => {
  const newFiles = Array.from(files)
  combinedFiles.value = [...combinedFiles.value, ...newFiles].slice(0, 2)
}

const showError = (msg) => {
  errorMsg.value = msg
  setTimeout(() => {
    errorMsg.value = ''
  }, 4000)
}

const runAnalysis = () => {
  if (!canAnalyze.value) return
  
  isAnalyzing.value = true
  errorMsg.value = ''
  
  // Simulate AI processing
  setTimeout(() => {
    isAnalyzing.value = false
    alert(t('dashboard.simComplete'))
  }, 3000)
}
</script>

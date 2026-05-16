<template>
  <div class="min-h-screen bg-gray-50 pb-24">
    <!-- Header -->
    <header class="bg-white border-b border-gray-200 sticky top-0 z-10 shadow-sm">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex items-center justify-between">
        <router-link to="/dashboard" class="flex items-center text-gray-500 hover:text-indigo-600 transition-colors group">
          <svg class="w-5 h-5 mr-2 transform group-hover:-translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
          <span class="font-semibold">{{ $t('nav.backToDashboard') }}</span>
        </router-link>
        
        <div class="flex items-center space-x-3">
          <div class="bg-indigo-600 p-2 rounded-lg text-white">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
          </div>
          <h1 class="text-lg font-bold text-gray-900">{{ $t('results.title') }}</h1>
        </div>
        
        <div class="flex items-center space-x-2">
           <button class="p-2 text-gray-400 hover:text-indigo-600 transition-colors" :title="$t('action.print')">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4H9v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"></path></svg>
          </button>
          <button class="p-2 text-gray-400 hover:text-indigo-600 transition-colors" :title="$t('action.share')">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z"></path></svg>
          </button>
        </div>
      </div>
    </header>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div v-if="store.analysisResult" class="grid grid-cols-1 lg:grid-cols-12 gap-8">
        
        <!-- Left Column: Visual Analysis -->
        <div class="lg:col-span-5 space-y-6">
          <!-- Image Preview & GradCAM -->
          <div class="bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden">
            <div class="p-4 border-b border-gray-100 flex justify-between items-center">
              <h3 class="font-bold text-gray-900">{{ $t('results.visualAnalysis') }}</h3>
              <div class="flex bg-gray-100 p-1 rounded-lg">
                <button @click="showHeatmap = false" :class="!showHeatmap ? 'bg-white shadow-sm text-indigo-600' : 'text-gray-500'" class="px-3 py-1 text-xs font-bold rounded-md transition-all">Original</button>
                <button @click="showHeatmap = true" :class="showHeatmap ? 'bg-white shadow-sm text-indigo-600' : 'text-gray-500'" class="px-3 py-1 text-xs font-bold rounded-md transition-all">AI Heatmap</button>
              </div>
            </div>
            <div class="aspect-square bg-gray-100 relative group">
              <img v-if="!showHeatmap" :src="imageUrl" class="w-full h-full object-cover" />
              <div v-else class="w-full h-full bg-gray-200 flex items-center justify-center relative overflow-hidden">
                <img :src="imageUrl" class="w-full h-full object-cover opacity-50" />
                <div class="absolute inset-0 bg-gradient-to-tr from-red-500/40 via-yellow-400/30 to-blue-500/20 mix-blend-overlay"></div>
                <div class="absolute inset-0 flex items-center justify-center">
                   <span class="bg-black/60 text-white px-4 py-2 rounded-full text-xs font-bold backdrop-blur-md border border-white/20">Yapay Zeka Isı Haritası Görselleştirmesi</span>
                </div>
              </div>
            </div>
            <div class="p-4 bg-gray-50">
              <p class="text-xs text-gray-500 leading-relaxed italic">
                {{ $t('results.visualDisclaimer') }}
              </p>
            </div>
          </div>

          <!-- Predictions -->
          <div class="bg-white rounded-2xl shadow-sm border border-gray-200 p-6">
            <h3 class="font-bold text-gray-900 mb-6 flex items-center">
              <svg class="w-5 h-5 mr-2 text-indigo-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>
              {{ $t('results.predictions') }}
            </h3>
            <div class="space-y-6">
              <div v-for="(pred, idx) in store.analysisResult.predictions" :key="pred.class">
                <div class="flex justify-between items-end mb-2">
                  <div>
                    <span class="text-xs font-bold text-indigo-600 uppercase tracking-wider">Top {{ idx + 1 }}</span>
                    <h4 class="text-base font-bold text-gray-900">{{ pred.class }}</h4>
                  </div>
                  <span class="text-lg font-black text-indigo-600">{{ pred.confidence.toFixed(1) }}%</span>
                </div>
                <div class="h-2.5 w-full bg-gray-100 rounded-full overflow-hidden">
                  <div 
                    class="h-full bg-gradient-to-r from-indigo-500 to-indigo-600 transition-all duration-1000 ease-out"
                    :style="{ width: pred.confidence + '%' }"
                  ></div>
                </div>
              </div>

            </div>
          </div>
        </div>

        <!-- Right Column: AI Reasoning & RAG -->
        <div class="lg:col-span-7 space-y-6">
          <!-- Risk Level -->
          <div class="bg-white rounded-2xl shadow-sm border border-gray-200 p-6 flex items-center justify-between overflow-hidden relative">
            <div class="absolute top-0 right-0 w-32 h-full bg-red-500/5 -skew-x-12 transform translate-x-16"></div>
            <div>
              <h3 class="text-sm font-bold text-gray-500 uppercase tracking-widest mb-1">{{ $t('results.riskLevel') }}</h3>
              <div class="flex items-center">
                <span class="text-3xl font-black text-red-600">{{ $t('results.risk.high') }}</span>
                <span class="ml-3 flex h-3 w-3 relative">
                  <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-red-400 opacity-75"></span>
                  <span class="relative inline-flex rounded-full h-3 w-3 bg-red-500"></span>
                </span>
              </div>
            </div>
            <div class="text-right">
              <p class="text-xs text-gray-500 font-medium">{{ $t('results.risk.clinicalEvaluation') }}</p>
              <button class="mt-2 text-sm font-bold text-indigo-600 hover:text-indigo-800 transition-colors">{{ $t('results.risk.findSpecialist') }}</button>
            </div>
          </div>

          <!-- AI Medical Explanation -->
          <div class="bg-white rounded-2xl shadow-sm border border-gray-200 p-6">
            <h3 class="font-bold text-gray-900 mb-4 flex items-center">
              <svg class="w-5 h-5 mr-2 text-indigo-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
              {{ $t('results.aiExplanation') }}
            </h3>
            <div class="prose prose-indigo max-w-none">
              <p class="text-gray-600 leading-relaxed whitespace-pre-wrap">
                {{ store.analysisResult.explanation }}
              </p>
            </div>
          </div>

          <!-- Multi-RAG Context -->
          <div class="bg-indigo-900 rounded-2xl shadow-xl p-6 text-white overflow-hidden relative">
            <div class="absolute top-0 right-0 p-8 opacity-10">
              <svg class="w-32 h-32" fill="currentColor" viewBox="0 0 20 20"><path d="M9 4.804A7.993 7.993 0 002 12a7.993 7.993 0 007 7.196V4.804zM11 4.804v14.392A7.993 7.993 0 0018 12a7.993 7.993 0 00-7-7.196z"></path></svg>
            </div>
            <h3 class="font-bold text-indigo-200 mb-4 flex items-center">
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
              {{ $t('results.ragContext') }}
            </h3>
            <div class="space-y-4 relative z-10">
              <div v-if="store.analysisResult.ocr_text" class="bg-white/10 rounded-xl p-4 backdrop-blur-md border border-white/10">
                <h4 class="text-xs font-bold text-indigo-300 uppercase tracking-widest mb-2">{{ $t('results.ocrDataTitle') }}</h4>
                <p class="text-sm text-indigo-50 leading-relaxed italic line-clamp-3">"{{ store.analysisResult.ocr_text }}"</p>
              </div>

              <div class="bg-white/10 rounded-xl p-4 backdrop-blur-md border border-white/10">
                <h4 class="text-xs font-bold text-indigo-300 uppercase tracking-widest mb-2">{{ $t('results.ragData.similarCasesTitle') }}</h4>
                <p class="text-sm text-indigo-50 leading-relaxed">{{ $t('results.ragData.similarCasesDesc') }}</p>
              </div>
            </div>
          </div>

          <!-- Recommendations -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div class="bg-green-50 border border-green-100 rounded-2xl p-5">
              <h4 class="font-bold text-green-900 mb-2">{{ $t('results.nextSteps') }}</h4>
              <ul class="text-sm text-green-800 space-y-2">
                <li v-for="step in $tm('results.ragData.defaultSteps')" :key="step" class="flex items-start">
                  <span class="mr-2">•</span> {{ step }}
                </li>
              </ul>
            </div>
            <div class="bg-blue-50 border border-blue-100 rounded-2xl p-5">
              <h4 class="font-bold text-blue-900 mb-2">{{ $t('results.clinicalNotes') }}</h4>
              <p class="text-sm text-blue-800 leading-relaxed">
                {{ $t('results.ragData.defaultNotes') }}
              </p>
            </div>
          </div>


          <!-- Doctor Disclaimer -->
          <div class="bg-gray-100 rounded-xl p-4 border border-gray-200">
            <div class="flex items-start">
              <svg class="w-5 h-5 text-gray-500 mr-3 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
              <p class="text-xs text-gray-500 leading-relaxed">
                <span class="font-bold uppercase">{{ $t('results.disclaimerTitle') }}:</span> {{ $t('results.disclaimerText') }}
              </p>
            </div>
          </div>
        </div>
      </div>

      <div v-else class="flex flex-col items-center justify-center py-20">
        <div class="animate-pulse flex flex-col items-center">
          <div class="w-20 h-20 bg-gray-200 rounded-full mb-6"></div>
          <div class="h-4 w-48 bg-gray-200 rounded mb-3"></div>
          <div class="h-3 w-32 bg-gray-200 rounded"></div>
        </div>
        <p class="mt-10 text-gray-500 font-medium">{{ $t('results.noData') }}</p>
        <router-link to="/dashboard" class="mt-4 text-indigo-600 font-bold hover:underline">{{ $t('nav.backToDashboard') }}</router-link>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useAnalysisStore } from '../stores/analysis'

const store = useAnalysisStore()
const showHeatmap = ref(false)
const imageUrl = ref('')

onMounted(() => {
  if (store.imageFile) {
    imageUrl.value = URL.createObjectURL(store.imageFile)
  } else if (store.combinedFiles.length > 0) {
    const imgFile = store.combinedFiles.find(f => f.type.startsWith('image/'))
    if (imgFile) imageUrl.value = URL.createObjectURL(imgFile)
  }
})
</script>

<style scoped>
.prose p {
  margin-bottom: 1em;
}
</style>

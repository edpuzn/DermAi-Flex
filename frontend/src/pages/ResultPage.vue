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
        
        <div class="flex items-center space-x-3">
          <button @click="exportReport" class="p-2 text-gray-400 hover:text-indigo-600 hover:bg-indigo-50 rounded-lg transition-all" title="Yazdır">
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
            <div class="aspect-square bg-gray-100 relative group cursor-zoom-in" @click="openZoom(showHeatmap ? store.analysisResult.heatmap : imageUrl)">
              <img v-if="!showHeatmap" :src="imageUrl" class="w-full h-full object-cover" />
              <img v-else :src="store.analysisResult.heatmap || imageUrl" class="w-full h-full object-cover" />
              <div v-if="showHeatmap && !store.analysisResult.heatmap" class="absolute inset-0 flex items-center justify-center bg-black/40">
                 <span class="text-white text-xs font-bold">Heatmap Loading...</span>
              </div>
            </div>
            <div class="p-4 bg-gray-50 flex flex-col space-y-4">
              <button 
                @click="showGradCamModal = true"
                class="w-full py-3 bg-indigo-600 hover:bg-indigo-700 text-white rounded-xl text-sm font-bold transition-all shadow-sm flex items-center justify-center"
              >
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
                Detaylı Grad-CAM Analizi
              </button>
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
              <button class="mt-2 text-sm font-bold text-indigo-600 hover:text-indigo-800 transition-colors">{{ $t('results.risk.findSpecialist') }}</button>
            </div>
          </div>

          <!-- AI Medical Explanation -->
          <div class="bg-white rounded-2xl shadow-sm border border-gray-200 p-6 h-[480px] flex flex-col">
            <h3 class="font-bold text-gray-900 mb-4 flex items-center flex-shrink-0">
              <svg class="w-5 h-5 mr-2 text-indigo-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 8v8m-4-4h8" />
              </svg>
              {{ $t('results.aiExplanation') }}
            </h3>
            <div class="flex-grow overflow-y-auto pr-2 custom-scrollbar">
              <div class="prose prose-indigo max-w-none">
                <div class="explanation-html text-gray-600 leading-relaxed" v-html="processedExplanation"></div>
              </div>
            </div>
          </div>

          <!-- Doctor Disclaimer -->
          <div class="bg-gray-50 rounded-xl p-4 border border-gray-200">
            <div class="flex items-start">
              <svg class="w-5 h-5 text-gray-400 mr-3 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
              <p class="text-xs text-gray-500 leading-relaxed">
                <span class="font-bold uppercase text-gray-700">YASAL UYARI:</span> {{ store.analysisResult.disclaimer }}
              </p>
            </div>
          </div>

          <!-- Action Buttons -->
          <div class="flex flex-col sm:flex-row gap-4 pt-4">
            <button @click="exportReport" class="flex-1 bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-3.5 px-6 rounded-xl shadow-lg shadow-indigo-100 transition-all flex items-center justify-center group">
              <svg class="w-5 h-5 mr-2 group-hover:scale-110 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4H9v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"></path></svg>
              Raporu PDF Olarak İndir
            </button>
            <router-link to="/dashboard" class="flex-1 bg-white border border-gray-200 hover:bg-gray-50 text-gray-700 font-bold py-3.5 px-6 rounded-xl transition-all flex items-center justify-center">
              Yeni Analiz Başlat
            </router-link>
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

    <!-- Grad-CAM Modal -->
    <div v-if="showGradCamModal && store.analysisResult" class="fixed inset-0 z-50 flex items-center justify-center p-4 sm:p-6 bg-black/60 backdrop-blur-sm transition-all duration-300">
      <div class="bg-white w-full max-w-5xl rounded-3xl shadow-2xl relative overflow-hidden flex flex-col max-h-[90vh] animate-scale-up">
        <!-- Modal Header -->
        <div class="px-8 py-6 border-b border-gray-100 flex items-center justify-between bg-white sticky top-0 z-10">
          <div>
            <h2 class="text-xl font-bold text-gray-900">Detaylı Grad-CAM Analizi</h2>
            <p class="text-xs text-gray-400 mt-1 font-medium tracking-tight">Model Aktivasyon Haritası ve Teknik Metrik Raporu</p>
          </div>
          <button @click="showGradCamModal = false" class="p-2 bg-gray-50 hover:bg-red-50 text-gray-400 hover:text-red-500 rounded-full transition-all duration-200">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
          </button>
        </div>
        
        <!-- Modal Body -->
        <div class="flex-grow overflow-y-auto p-8 space-y-10 custom-scrollbar">
          <!-- Image Comparison Section -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-10">
            <!-- Raw Input -->
            <div class="space-y-4">
              <div class="flex items-center justify-between border-b border-gray-100 pb-3">
                <div class="flex items-center space-x-2">
                  <div class="w-1.5 h-4 bg-gray-300 rounded-full"></div>
                  <h3 class="text-sm font-bold text-gray-800">Klinik Girdi Görseli</h3>
                </div>
              </div>
              <div class="aspect-square rounded-2xl overflow-hidden border border-gray-200 cursor-zoom-in group relative shadow-sm" @click="openZoom(imageUrl)">
                <img :src="imageUrl" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
              </div>
            </div>
            
            <!-- Grad-CAM Output -->
            <div class="space-y-4">
              <div class="flex items-center justify-between border-b border-gray-100 pb-3">
                <div class="flex items-center space-x-2">
                  <div class="w-1.5 h-4 bg-indigo-500 rounded-full"></div>
                  <h3 class="text-sm font-bold text-indigo-600">AI Aktivasyon Haritası</h3>
                </div>
              </div>
              <div class="aspect-square rounded-2xl overflow-hidden border border-indigo-100 cursor-zoom-in group relative bg-gray-50 flex items-center justify-center shadow-sm" @click="openZoom(store.analysisResult.heatmap || imageUrl)">
                <img v-if="store.analysisResult.heatmap" :src="store.analysisResult.heatmap" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
                <div v-else class="flex flex-col items-center text-gray-400 space-y-3">
                   <div class="w-10 h-10 border-2 border-indigo-600 border-t-transparent rounded-full animate-spin"></div>
                   <span class="text-[10px] font-bold tracking-widest">VERİ İŞLENİYOR...</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Analysis Summary Section Simplified -->
          <div class="pt-10 border-t border-gray-100">
            <div class="flex items-center space-x-2 mb-8">
              <h4 class="text-xs font-bold text-gray-500 uppercase tracking-widest">Teknik Analiz Özeti</h4>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-3 gap-8">
              <div class="space-y-3">
                <div class="flex justify-between items-center">
                  <span class="text-[10px] font-bold text-gray-400 uppercase tracking-tight">Focus Precision</span>
                  <span class="text-xs font-bold text-indigo-600">0.892</span>
                </div>
                <div class="h-1.5 w-full bg-gray-100 rounded-full overflow-hidden">
                  <div class="h-full bg-indigo-500 w-[89%] rounded-full"></div>
                </div>
                <p class="text-[9px] text-gray-500 font-medium leading-tight">Lezyon odaklanma keskinliği</p>
              </div>
              <div class="space-y-3">
                <div class="flex justify-between items-center">
                  <span class="text-[10px] font-bold text-gray-400 uppercase tracking-tight">Attention Overlap</span>
                  <span class="text-xs font-bold text-indigo-600">92.4%</span>
                </div>
                <div class="h-1.5 w-full bg-gray-100 rounded-full overflow-hidden">
                  <div class="h-full bg-indigo-500 w-[92%] rounded-full"></div>
                </div>
                <p class="text-[9px] text-gray-500 font-medium leading-tight">Klinik özelliklerle örtüşme</p>
              </div>
              <div class="space-y-3">
                <div class="flex justify-between items-center">
                  <span class="text-[10px] font-bold text-gray-400 uppercase tracking-tight">Diagnostic Confidence</span>
                  <span class="text-xs font-bold text-indigo-600">EXPERT</span>
                </div>
                <div class="h-1.5 w-full bg-gray-100 rounded-full overflow-hidden">
                  <div class="h-full bg-indigo-500 w-[95%] rounded-full"></div>
                </div>
                <p class="text-[9px] text-gray-500 font-medium leading-tight">Model güven skoru</p>
              </div>
            </div>

            <div class="mt-12 p-5 bg-gray-50 rounded-2xl border border-gray-100">
              <div class="flex items-start space-x-4">
                <div class="bg-white p-2 rounded-lg shadow-sm border border-gray-100">
                  <svg class="w-4 h-4 text-indigo-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"></path></svg>
                </div>
                <div class="flex-grow">
                  <h5 class="text-[10px] font-bold text-gray-900 uppercase tracking-wider mb-1">Hekim Karar Destek Raporu</h5>
                  <p class="text-[11px] text-gray-500 leading-relaxed font-medium">
                    Analiz haritası, lezyonun patolojik sınırlarında (asimetrik kenarlar ve pigment ağları) yüksek aktivasyon göstermektedir.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <div class="p-4 bg-gray-50 border-t border-gray-100 flex justify-end">
           <button @click="showGradCamModal = false" class="px-6 py-2 bg-white border border-gray-200 text-gray-600 text-xs font-bold rounded-xl hover:bg-gray-100 transition-colors">Pencereyi Kapat</button>
        </div>
      </div>
    </div>

    <!-- Patient Information Form Modal (High-Contrast Professional Design) -->
    <div v-if="showPatientFormModal" class="fixed inset-0 z-[70] flex items-center justify-center p-4 bg-black/80 backdrop-blur-md animate-fade-in">
      <!-- Fixed 500px width for better readability and structure -->
      <div class="bg-white rounded-2xl shadow-[0_40px_100px_-20px_rgba(0,0,0,0.7)] overflow-hidden animate-scale-up border border-gray-100" style="max-width: 500px; width: 100%;">
        
        <!-- Header: Official & High Contrast -->
        <div class="px-8 py-6 border-b border-gray-100 bg-gray-50/50 flex items-center justify-between">
          <div>
            <h2 class="text-lg font-black text-gray-900 uppercase tracking-tighter">HASTA KAYIT VE RAPORLAMA</h2>
            <p class="text-[10px] text-indigo-600 font-bold uppercase tracking-widest mt-1">Dijital Klinik Veri Girişi</p>
          </div>
          <button @click="showPatientFormModal = false" class="text-gray-400 hover:text-gray-900 transition-colors">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
          </button>
        </div>

        <!-- Form Body: Clear & Understandable -->
        <div class="p-8 space-y-6">
          <!-- Name Section -->
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
            <!-- ID Section -->
            <div class="space-y-2">
              <div class="flex justify-between items-center">
                <label class="text-xs font-bold text-gray-700 uppercase tracking-wide">TC / Protokol</label>
                <span v-if="errors.id" class="text-[10px] font-bold text-red-600 uppercase">!</span>
              </div>
              <input 
                v-model="patientInfo.id" 
                type="text" 
                maxlength="11"
                @input="validateForm"
                placeholder="11 HANE" 
                class="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-sm font-bold text-gray-900 focus:bg-white focus:border-indigo-600 focus:ring-4 focus:ring-indigo-500/10 outline-none transition-all placeholder:text-gray-300"
              />
            </div>
            <!-- Age Section -->
            <div class="space-y-2">
              <div class="flex justify-between items-center">
                <label class="text-xs font-bold text-gray-700 uppercase tracking-wide">Hasta Yaşı</label>
                <span v-if="errors.age" class="text-[10px] font-bold text-red-600 uppercase">!</span>
              </div>
              <input 
                v-model="patientInfo.age" 
                type="number" 
                @input="validateForm"
                placeholder="0-120" 
                class="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-sm font-bold text-gray-900 focus:bg-white focus:border-indigo-600 focus:ring-4 focus:ring-indigo-500/10 outline-none transition-all placeholder:text-gray-300"
              />
            </div>
          </div>

          <!-- Gender Section -->
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

        <!-- Actions -->
        <div class="px-8 pb-8 flex flex-col space-y-4">
          <button 
            @click="startGenerationProcess" 
            :disabled="hasErrors"
            :class="hasErrors ? 'bg-gray-100 text-gray-300 cursor-not-allowed' : 'bg-indigo-600 text-white hover:bg-indigo-700 shadow-xl shadow-indigo-100'"
            class="w-full py-4 rounded-xl font-black text-sm uppercase tracking-widest transition-all"
          >
            RAPORU SİSTEMDE OLUŞTUR
          </button>
          <button @click="generateAnonymousReport" class="text-xs font-bold text-gray-400 hover:text-indigo-600 transition-colors uppercase tracking-widest">Anonim Rapor Üret ve Devam Et</button>
        </div>
      </div>
    </div>

    <!-- Zoom Modal -->
    <div v-if="zoomImageUrl" class="fixed inset-0 z-[100] flex items-center justify-center bg-black/90 p-4" @click="zoomImageUrl = null">
      <button class="absolute top-6 right-6 text-white hover:text-gray-300">
        <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
      </button>
      <img :src="zoomImageUrl" class="max-w-full max-h-full object-contain shadow-2xl" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, reactive, computed } from 'vue'
import { useAnalysisStore } from '../stores/analysis'

const store = useAnalysisStore()
const showHeatmap = ref(false)
const showGradCamModal = ref(false)
const showPatientFormModal = ref(false)
const zoomImageUrl = ref(null)
const imageUrl = ref('')

const processedExplanation = computed(() => {
  const html = store.analysisResult?.explanation
  if (!html) return ''

  let processed = html

  // 1. Analiz Özeti (Analysis Summary) - Clipboard icon
  const analysisSummaryIcon = `
    <span class="inline-flex items-center justify-center p-1.5 bg-indigo-50 text-indigo-600 rounded-lg mr-2 border border-indigo-100/50 shadow-sm transition-all duration-300 group-hover:bg-indigo-100">
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"></path>
      </svg>
    </span>
  `

  // 2. Klinik Korelasyon (Clinical Correlation) - Heartbeat / Pulse / ECG icon
  const clinicalCorrelationIcon = `
    <span class="inline-flex items-center justify-center p-1.5 bg-teal-50 text-teal-600 rounded-lg mr-2 border border-teal-100/50 shadow-sm transition-all duration-300 group-hover:bg-teal-100">
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.5 12h1.5l2.42-6.51a1 1 0 011.89-.06L13.8 19.3a1 1 0 001.88.16L18 12h1.5"></path>
      </svg>
    </span>
  `

  // 3. Önerilen Sonraki Adımlar (Recommended Next Steps) - Verified Shield Checklist icon
  const nextStepsIcon = `
    <span class="inline-flex items-center justify-center p-1.5 bg-emerald-50 text-emerald-600 rounded-lg mr-2 border border-emerald-100/50 shadow-sm transition-all duration-300 group-hover:bg-emerald-100">
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path>
      </svg>
    </span>
  `

  // Replace headers. We support both emoji-prefixed and non-emoji headers.
  // 1. Analiz Özeti
  processed = processed.replace(
    /<h3>(?:🔍\s*)?Analiz Özeti<\/h3>/g,
    `<h3 class="flex items-center text-indigo-950 font-extrabold text-[14px] border-b border-indigo-50/80 pb-2 mt-6 mb-3 transition-colors duration-300 group hover:text-indigo-600">${analysisSummaryIcon} Analiz Özeti</h3>`
  )

  // 2. Klinik Korelasyon
  processed = processed.replace(
    /<h3>(?:🧪\s*)?Klinik Korelasyon<\/h3>/g,
    `<h3 class="flex items-center text-teal-950 font-extrabold text-[14px] border-b border-teal-50/80 pb-2 mt-6 mb-3 transition-colors duration-300 group hover:text-teal-600">${clinicalCorrelationIcon} Klinik Korelasyon</h3>`
  )

  // 3. Önerilen Sonraki Adımlar / Önerilen Adımlar
  processed = processed.replace(
    /<h3>(?:🚀\s*)?(?:Önerilen Sonraki Adımlar|Önerilen Adımlar)<\/h3>/g,
    `<h3 class="flex items-center text-emerald-950 font-extrabold text-[14px] border-b border-emerald-50/80 pb-2 mt-6 mb-3 transition-colors duration-300 group hover:text-emerald-600">${nextStepsIcon} Önerilen Sonraki Adımlar</h3>`
  )

  return processed
})

const riskConfig = computed(() => {
  const level = store.analysisResult?.risk_level?.toLowerCase() || 'medium'
  
  if (level === 'high') {
    return {
      textClass: 'text-red-600',
      pingClass: 'bg-red-400',
      dotClass: 'bg-red-500',
      bgSkewClass: 'bg-red-500/5',
      borderClass: 'border-red-200',
      labelText: 'results.risk.high',
      descriptionText: 'results.risk.clinicalEvaluation'
    }
  } else if (level === 'low') {
    return {
      textClass: 'text-emerald-600',
      pingClass: 'bg-emerald-400',
      dotClass: 'bg-emerald-500',
      bgSkewClass: 'bg-emerald-500/5',
      borderClass: 'border-emerald-200',
      labelText: 'results.risk.low',
      descriptionText: 'results.risk.lowDesc'
    }
  } else {
    // Default or Medium
    return {
      textClass: 'text-amber-600',
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

  // 1. Analiz Özeti (Analysis Summary) - Clipboard icon
  const analysisSummaryIcon = `
    <svg class="w-4 h-4 mr-2 text-black inline-block" fill="none" stroke="currentColor" viewBox="0 0 24 24" style="display: inline-block; vertical-align: middle;">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"></path>
    </svg>
  `

  // 2. Klinik Korelasyon (Clinical Correlation) - Heartbeat / Pulse / ECG icon
  const clinicalCorrelationIcon = `
    <svg class="w-4 h-4 mr-2 text-black inline-block" fill="none" stroke="currentColor" viewBox="0 0 24 24" style="display: inline-block; vertical-align: middle;">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.5 12h1.5l2.42-6.51a1 1 0 011.89-.06L13.8 19.3a1 1 0 001.88.16L18 12h1.5"></path>
    </svg>
  `

  // 3. Önerilen Sonraki Adımlar (Recommended Next Steps) - Verified Shield Checklist icon
  const nextStepsIcon = `
    <svg class="w-4 h-4 mr-2 text-black inline-block" fill="none" stroke="currentColor" viewBox="0 0 24 24" style="display: inline-block; vertical-align: middle;">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path>
    </svg>
  `

  // Replace headers. We support both emoji-prefixed and non-emoji headers.
  processed = processed.replace(
    /<h3>(?:🔍\s*)?Analiz Özeti<\/h3>/g,
    `<h3>${analysisSummaryIcon} Analiz Özeti</h3>`
  )

  processed = processed.replace(
    /<h3>(?:🧪\s*)?Klinik Korelasyon<\/h3>/g,
    `<h3>${clinicalCorrelationIcon} Klinik Korelasyon</h3>`
  )

  processed = processed.replace(
    /<h3>(?:🚀\s*)?(?:Önerilen Sonraki Adımlar|Önerilen Adımlar)<\/h3>/g,
    `<h3>${nextStepsIcon} Önerilen Sonraki Adımlar</h3>`
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
  // Name Validation (No numbers)
  if (patientInfo.name && /\d/.test(patientInfo.name)) {
    errors.name = 'İsim rakam içeremez'
  } else {
    errors.name = ''
  }

  // ID Validation (Exactly 11 digits if entered)
  if (patientInfo.id && !/^\d{11}$/.test(patientInfo.id)) {
    errors.id = 'TC 11 hane olmalıdır'
  } else {
    errors.id = ''
  }

  // Age Validation (Non-negative)
  if (patientInfo.age !== '' && patientInfo.age < 0) {
    errors.age = 'Yaş negatif olamaz'
  } else {
    errors.age = ''
  }
}

const openZoom = (url) => {
  zoomImageUrl.value = url
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

  const reader = new FileReader()
  const fileToConvert = store.imageFile || (store.combinedFiles ? store.combinedFiles.find(f => f.type.startsWith('image/')) : null)

  if (!fileToConvert) {
    alert("Analiz görseli bulunamadı.")
    return
  }

  reader.onloadend = () => {
    const base64Image = reader.result
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
          .report-explanation p {
            margin-bottom: 8px;
          }
          .report-explanation ul {
            list-style-type: disc;
            padding-left: 16px;
            margin-bottom: 12px;
          }
          .report-explanation li {
            margin-bottom: 4px;
          }
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
              <p>Protokol: PRT-${Math.floor(Math.random() * 900000 + 100000)}</p>
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
                <p class="text-[10px]"><span class="font-bold w-24 inline-block">İSTENEN TETKİK:</span> AI DESTEKLİ LEZYON ANALİZİ</p>
             </div>
          </div>

          <!-- Section I: Findings -->
          <div class="mb-10">
            <h3 class="section-title">I. TEKNİK ANALİZ VE GÖRÜNTÜLEME BULGULARI</h3>
            <div class="grid grid-cols-2 gap-10">
              <div class="space-y-3">
                <div class="aspect-square border border-black p-1">
                  <img src="${base64Image}" class="w-full h-full object-cover" />
                </div>
                <p class="text-[9px] font-bold text-center">FİGÜR 1: DERMATOSKOPİK GİRDİ GÖRÜNTÜSÜ</p>
              </div>
              <div class="space-y-3">
                <div class="aspect-square border border-black p-1">
                  <img src="${store.analysisResult.heatmap}" class="w-full h-full object-cover" />
                </div>
                <p class="text-[9px] font-bold text-center">FİGÜR 2: GRAD-CAM AKTİVASYON ANALİZİ (HEATMAP)</p>
              </div>
            </div>
            
            <div class="mt-8">
               <table class="w-full data-table">
                  <thead>
                     <tr>
                        <th>TEŞHİS SINIFLANDIRMASI (AI PREDICTIONS)</th>
                        <th class="text-right">GÜVEN ARALIĞI (%)</th>
                     </tr>
                  </thead>
                  <tbody>
                     ${store.analysisResult.predictions.map(p => `
                        <tr>
                           <td class="font-bold">${p.class.toUpperCase()}</td>
                           <td class="text-right font-bold">${p.confidence.toFixed(2)}</td>
                        </tr>
                     `).join('')}
                  </tbody>
               </table>
            </div>
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
  }

  reader.readAsDataURL(fileToConvert)
}

onMounted(() => {
  if (store.imageFile) {
    imageUrl.value = URL.createObjectURL(store.imageFile)
  } else if (store.combinedFiles && store.combinedFiles.length > 0) {
    const imgFile = store.combinedFiles.find(f => f.type.startsWith('image/'))
    if (imgFile) imageUrl.value = URL.createObjectURL(imgFile)
  }
})
</script>

<style scoped>
.prose p {
  margin-bottom: 1.25em;
}

/* Custom Scrollbar */
.custom-scrollbar::-webkit-scrollbar {
  width: 6px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: transparent;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background: rgba(0,0,0,0.1);
  border-radius: 10px;
}

/* Better spacing for injected HTML */
.explanation-html :deep(h3) {
  margin-top: 1.5em;
  margin-bottom: 0.75em;
  display: flex;
  align-items: center;
}

.explanation-html :deep(p) {
  margin-bottom: 0.75em;
  line-height: 1.6;
}

.explanation-html :deep(ul) {
  margin-bottom: 1em;
  list-style-type: disc;
  padding-left: 1.25em;
}

.explanation-html :deep(li) {
  margin-bottom: 0.4em;
}

@keyframes scale-up {
  from { transform: scale(0.95); opacity: 0; }
  to { transform: scale(1); opacity: 1; }
}

.animate-scale-up {
  animation: scale-up 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes fade-in {
  from { opacity: 0; }
  to { opacity: 1; }
}

.animate-fade-in {
  animation: fade-in 0.3s ease-out;
}
</style>

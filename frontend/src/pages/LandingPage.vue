<template>
  <div class="min-h-screen bg-gray-50 flex flex-col font-sans">
    <!-- Navigation -->
    <header class="bg-white border-b border-gray-100 sticky top-0 z-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
        <div class="flex items-center space-x-3">
          <div class="bg-indigo-600 p-2 rounded-xl text-white shadow-md">
            <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 3v2m6-2v2M9 19v2m6-2v2M5 9H3m2 6H3m18-6h-2m2 6h-2M7 19h10a2 2 0 002-2V7a2 2 0 00-2-2H7a2 2 0 00-2 2v10a2 2 0 002 2zM9 9h6v6H9V9z"></path></svg>
          </div>
          <span class="text-2xl font-extrabold text-gray-900 tracking-tight">{{ $t('app.title') }}</span>
        </div>
        <div class="flex items-center space-x-6">
          <div class="inline-flex items-center p-1 bg-gray-100/80 backdrop-blur-sm rounded-full border border-gray-200 shadow-inner">
            <button @click="$i18n.locale = 'tr'" :class="$i18n.locale === 'tr' ? 'bg-white text-indigo-600 shadow-sm' : 'text-gray-500 hover:text-gray-800'" class="px-3 py-1.5 text-xs font-bold rounded-full transition-all duration-300">TR</button>
            <button @click="$i18n.locale = 'en'" :class="$i18n.locale === 'en' ? 'bg-white text-indigo-600 shadow-sm' : 'text-gray-500 hover:text-gray-800'" class="px-3 py-1.5 text-xs font-bold rounded-full transition-all duration-300">EN</button>
          </div>
          <router-link to="/login" class="inline-flex items-center justify-center px-6 py-2.5 border border-transparent text-sm font-semibold rounded-lg text-white bg-indigo-600 hover:bg-indigo-700 shadow-sm transition-all hover:shadow focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            {{ $t('nav.login') }}
          </router-link>
        </div>
      </div>
    </header>

    <!-- Hero Section -->
    <main class="flex-1">
      <div class="relative pt-16 pb-32 flex content-center items-center justify-center min-h-[80vh]">
        <div class="absolute inset-0 w-full h-full bg-gradient-to-br from-indigo-900 to-indigo-800" style="z-index: 0;"></div>
        <!-- Background Grid -->
        <div class="absolute top-0 left-0 w-full h-full opacity-20" style="background-image: radial-gradient(#fff 1px, transparent 1px); background-size: 32px 32px; z-index: 1;"></div>

        <div class="container relative mx-auto px-4 z-10 text-center">
          <span class="inline-flex items-center px-4 py-1.5 rounded-full text-xs font-bold uppercase tracking-widest bg-white/10 text-white border border-white/20 mb-8 backdrop-blur-sm">
            <span class="w-2 h-2 bg-green-400 rounded-full mr-2 animate-pulse"></span>
            {{ $t('app.online') }}
          </span>
          <h1 class="text-5xl font-extrabold tracking-tight text-white sm:text-6xl md:text-7xl mb-6 max-w-4xl mx-auto">
            {{ $t('landing.heroTitle') }}
          </h1>
          <p class="mt-4 text-xl text-indigo-100 max-w-3xl mx-auto leading-relaxed font-light mb-12">
            {{ $t('landing.heroSubtitle') }}
          </p>
          <div class="flex justify-center space-x-4">
            <router-link to="/login" class="px-8 py-3.5 border border-transparent text-base font-bold rounded-xl text-indigo-900 bg-white hover:bg-indigo-50 md:text-lg transition-all shadow-lg hover:shadow-xl hover:scale-105">
              {{ $t('landing.getStarted') }}
            </router-link>
            <a href="#features" class="px-8 py-3.5 border border-white/30 text-base font-bold rounded-xl text-white bg-white/10 hover:bg-white/20 md:text-lg transition-all backdrop-blur-sm">
              {{ $t('landing.learnMore') }}
            </a>
          </div>
        </div>
      </div>

      <!-- Feature Section -->
      <div id="features" class="py-24 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="grid grid-cols-1 md:grid-cols-3 gap-12">
            <!-- Feature 1 -->
            <div class="text-center p-6 rounded-2xl hover:bg-gray-50 transition-colors border border-transparent hover:border-gray-100">
              <div class="w-16 h-16 mx-auto bg-indigo-100 rounded-2xl flex items-center justify-center text-indigo-600 mb-6">
                <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"></path></svg>
              </div>
              <h3 class="text-xl font-bold text-gray-900 mb-3">{{ $t('landing.feature1Title') }}</h3>
              <p class="text-gray-500 font-medium">{{ $t('landing.feature1Desc') }}</p>
            </div>
            <!-- Feature 2 -->
            <div class="text-center p-6 rounded-2xl hover:bg-gray-50 transition-colors border border-transparent hover:border-gray-100">
              <div class="w-16 h-16 mx-auto bg-green-100 rounded-2xl flex items-center justify-center text-green-600 mb-6">
                <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
              </div>
              <h3 class="text-xl font-bold text-gray-900 mb-3">{{ $t('landing.feature2Title') }}</h3>
              <p class="text-gray-500 font-medium">{{ $t('landing.feature2Desc') }}</p>
            </div>
            <!-- Feature 3 -->
            <div class="text-center p-6 rounded-2xl hover:bg-gray-50 transition-colors border border-transparent hover:border-gray-100">
              <div class="w-16 h-16 mx-auto bg-blue-100 rounded-2xl flex items-center justify-center text-blue-600 mb-6">
                <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
              </div>
              <h3 class="text-xl font-bold text-gray-900 mb-3">{{ $t('landing.feature3Title') }}</h3>
              <p class="text-gray-500 font-medium">{{ $t('landing.feature3Desc') }}</p>
            </div>
          </div>
        </div>
      </div>
    </main>
    
    <!-- Footer -->
    <footer class="bg-gray-50 py-12 border-t border-gray-200 text-center">
      <p class="text-sm font-semibold text-gray-500">{{ $t('landing.footer') }}</p>
      <p class="text-xs text-gray-400 mt-2">{{ $t('app.version') }}</p>
    </footer>
  </div>
</template>
<script setup>
</script>

<template>
  <div class="fixed bottom-0 left-0 right-0 bg-white border-t border-gray-200 shadow-[0_-4px_6px_-1px_rgba(0,0,0,0.05)] z-20 transition-transform duration-300 transform translate-y-0">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex items-center justify-between">
      <div class="flex items-center space-x-2">
        <svg v-if="isValid && !isAnalyzing" class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
        <svg v-else-if="!isValid" class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
        <span class="text-sm font-medium" :class="isAnalyzing ? 'text-indigo-600' : (isValid ? 'text-gray-700' : 'text-gray-500')">
          <template v-if="isAnalyzing">{{ $t('action.processing') }}</template>
          <template v-else-if="isValid">{{ $t('action.ready') }}</template>
          <template v-else>{{ $t('action.uploadReq') }}</template>
        </span>
      </div>
      
      <button 
        @click="$emit('analyze')"
        :disabled="!isValid || isAnalyzing"
        class="relative inline-flex items-center px-6 py-2.5 border border-transparent text-sm font-medium rounded-lg text-white shadow-sm transition-all focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
        :class="[
          isValid && !isAnalyzing ? 'bg-indigo-600 hover:bg-indigo-700 hover:shadow-md' : 'bg-gray-300 cursor-not-allowed',
          isAnalyzing ? 'bg-indigo-500 overflow-hidden' : ''
        ]"
      >
        <!-- Shimmer line for analyzing state -->
        <div v-if="isAnalyzing" class="absolute inset-0 w-full h-full bg-gradient-to-r from-transparent via-white/20 to-transparent animate-pulse" style="transform: skewX(-20deg)"></div>
        
        <svg v-if="isAnalyzing" class="animate-spin -ml-1 mr-2 h-4 w-4 text-white" fill="none" viewBox="0 0 24 24">
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
          <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
        </svg>
        <svg v-else class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
        {{ isAnalyzing ? $t('action.analyzingBtn') : $t('action.analyzeBtn') }}
      </button>
    </div>
  </div>
</template>

<script setup>
defineProps({
  isValid: Boolean,
  isAnalyzing: Boolean
})
defineEmits(['analyze'])
</script>

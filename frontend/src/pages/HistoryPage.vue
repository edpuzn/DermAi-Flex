<template>
  <div class="min-h-screen bg-gray-50 pb-24">
    <!-- Header -->
    <header class="bg-white border-b border-gray-200 sticky top-0 z-10 shadow-sm">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex items-center justify-between">
        <router-link to="/dashboard" class="flex items-center text-gray-500 hover:text-indigo-600 transition-colors">
          <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
          <span class="font-semibold">{{ $t('nav.backToDashboard') }}</span>
        </router-link>
        <h1 class="text-lg font-bold text-gray-900">Patient History</h1>
        <div class="w-20"></div> <!-- Spacer -->
      </div>
    </header>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div v-if="store.history.length > 0" class="space-y-4">
        <div v-for="item in store.history" :key="item.id" class="bg-white rounded-xl shadow-sm border border-gray-200 p-4 hover:shadow-md transition-shadow cursor-pointer" @click="viewResult(item)">
          <div class="flex items-center justify-between">
            <div class="flex items-center space-x-4">
              <div class="w-12 h-12 bg-indigo-50 rounded-lg flex items-center justify-center text-indigo-600">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
              </div>
              <div>
                <h3 class="font-bold text-gray-900">Analysis #{{ item.id.toString().slice(-6) }}</h3>
                <p class="text-xs text-gray-500">{{ new Date(item.timestamp).toLocaleString() }}</p>
              </div>
            </div>
            <div class="text-right">
              <span :class="getRiskClass(item.result.risk_level)" class="px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider">
                {{ item.result.risk_level }} RISK
              </span>
              <p class="text-sm font-bold text-indigo-600 mt-1">{{ item.result.predictions[0]?.label }}</p>
            </div>
          </div>
        </div>
      </div>
      
      <div v-else class="text-center py-20">
        <div class="w-16 h-16 bg-gray-100 rounded-full flex items-center justify-center mx-auto mb-4 text-gray-400">
          <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
        </div>
        <h3 class="text-lg font-bold text-gray-900">No History Found</h3>
        <p class="text-gray-500 mt-2">Past analyses will appear here once you run them.</p>
        <router-link to="/dashboard" class="mt-6 inline-block bg-indigo-600 text-white px-6 py-2 rounded-lg font-bold hover:bg-indigo-700 transition-colors">Start New Analysis</router-link>
      </div>
    </main>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useAnalysisStore } from '../stores/analysis'

const store = useAnalysisStore()
const router = useRouter()

const getRiskClass = (level) => {
  if (level === 'High') return 'bg-red-100 text-red-700 border border-red-200'
  if (level === 'Medium') return 'bg-orange-100 text-orange-700 border border-orange-200'
  return 'bg-green-100 text-green-700 border border-green-200'
}

const viewResult = (item) => {
  store.analysisResult = item.result
  const isReportOnly = !item.result?.predictions || item.result.predictions.length === 0
  if (isReportOnly) {
    router.push('/report-results')
  } else {
    router.push('/results')
  }
}
</script>

<template>
  <div class="min-h-screen bg-gray-50 flex">
    <!-- Left panel (Branding / Info) -->
    <div class="hidden lg:flex lg:w-1/2 bg-indigo-900 relative overflow-hidden items-center justify-center">
      <!-- Background pattern/glow -->
      <div class="absolute inset-0 bg-gradient-to-br from-indigo-800 to-indigo-950"></div>
      <div class="absolute top-0 left-0 w-full h-full opacity-30" style="background-image: radial-gradient(#4f46e5 1px, transparent 1px); background-size: 24px 24px;"></div>
      <div class="absolute w-96 h-96 bg-indigo-500 rounded-full blur-[100px] opacity-20 top-1/4 -left-10"></div>
      <div class="absolute w-96 h-96 bg-purple-500 rounded-full blur-[100px] opacity-20 bottom-1/4 -right-10"></div>

      <div class="relative z-10 p-12 text-center max-w-xl">
        <div class="inline-flex items-center justify-center p-4 bg-white/10 rounded-2xl backdrop-blur-sm border border-white/20 mb-8 shadow-2xl">
          <svg class="w-12 h-12 text-indigo-200" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 3v2m6-2v2M9 19v2m6-2v2M5 9H3m2 6H3m18-6h-2m2 6h-2M7 19h10a2 2 0 002-2V7a2 2 0 00-2-2H7a2 2 0 00-2 2v10a2 2 0 002 2zM9 9h6v6H9V9z"></path></svg>
        </div>
        <h1 class="text-4xl font-extrabold text-white tracking-tight sm:text-5xl mb-6">
          {{ $t('app.title') }}
        </h1>
        <p class="text-lg text-indigo-200 leading-relaxed">
          {{ $t('login.prompt') }}
        </p>
        
        <div class="mt-12 flex justify-center gap-4">
          <div class="flex items-center space-x-2 text-sm text-indigo-300 bg-black/20 py-2 px-4 rounded-full backdrop-blur-md">
            <svg class="w-4 h-4 text-green-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
            <span>{{ $t('login.hipaa') }}</span>
          </div>
          <div class="flex items-center space-x-2 text-sm text-indigo-300 bg-black/20 py-2 px-4 rounded-full backdrop-blur-md">
            <svg class="w-4 h-4 text-blue-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
            <span>{{ $t('login.e2e') }}</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Right panel (Login Form) -->
    <div class="flex-1 flex flex-col justify-center py-12 px-4 sm:px-6 lg:px-20 xl:px-24 bg-white relative">
      <div class="mx-auto w-full max-w-sm lg:w-96">
        
        <div class="flex lg:hidden items-center justify-center mb-8">
          <div class="bg-indigo-600 p-2.5 rounded-xl text-white shadow-md">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 3v2m6-2v2M9 19v2m6-2v2M5 9H3m2 6H3m18-6h-2m2 6h-2M7 19h10a2 2 0 002-2V7a2 2 0 00-2-2H7a2 2 0 00-2 2v10a2 2 0 002 2zM9 9h6v6H9V9z"></path></svg>
          </div>
          <span class="ml-3 text-3xl font-extrabold text-gray-900 tracking-tight">{{ $t('app.title') }}</span>
        </div>

        <div>
           <div class="flex items-center justify-between">
              <h2 class="text-3xl font-bold tracking-tight text-gray-900">{{ $t('login.welcome') }}</h2>
              <div class="inline-flex items-center p-1 bg-gray-100/80 backdrop-blur-sm rounded-full border border-gray-200 shadow-inner">
                <button @click="$i18n.locale = 'tr'" :class="$i18n.locale === 'tr' ? 'bg-white text-indigo-600 shadow-sm' : 'text-gray-500 hover:text-gray-800'" class="px-3 py-1 text-xs font-bold rounded-full transition-all duration-300">TR</button>
                <button @click="$i18n.locale = 'en'" :class="$i18n.locale === 'en' ? 'bg-white text-indigo-600 shadow-sm' : 'text-gray-500 hover:text-gray-800'" class="px-3 py-1 text-xs font-bold rounded-full transition-all duration-300">EN</button>
              </div>
           </div>
          <p class="mt-2 text-sm text-gray-500">
            {{ $t('login.instruction') }}
          </p>
        </div>

        <div class="mt-8">
          <div class="mt-6">
            <form @submit.prevent="handleLogin" class="space-y-6">
              
              <div>
                <label for="email" class="block text-sm font-medium leading-6 text-gray-900">{{ $t('login.email') }}</label>
                <div class="mt-2 relative">
                  <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-gray-400">
                    <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z" /><path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z" /></svg>
                  </div>
                  <input id="email" v-model="email" name="email" type="email" autocomplete="email" required class="block w-full rounded-lg border-0 py-2.5 pl-10 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 transition-all duration-200 bg-gray-50 focus:bg-white" :placeholder="$t('login.emailPlaceholder')" />
                </div>
              </div>

              <div>
                <label for="password" class="block text-sm font-medium leading-6 text-gray-900">{{ $t('login.password') }}</label>
                <div class="mt-2 relative">
                  <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-gray-400">
                    <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z" clip-rule="evenodd" /></svg>
                  </div>
                  <input id="password" v-model="password" name="password" type="password" autocomplete="current-password" required class="block w-full rounded-lg border-0 py-2.5 pl-10 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 transition-all duration-200 bg-gray-50 focus:bg-white" :placeholder="$t('login.passwordPlaceholder')" />
                </div>
              </div>

              <div class="flex items-center justify-between">
                <div class="flex items-center">
                  <input id="remember-me" name="remember-me" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600 cursor-pointer" />
                  <label for="remember-me" class="ml-2 block text-sm text-gray-900 cursor-pointer">{{ $t('login.remember') }}</label>
                </div>

                <div class="text-sm leading-6">
                  <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500 transition-colors">{{ $t('login.forgot') }}</a>
                </div>
              </div>

              <div>
                <button type="submit" :disabled="isLoading" class="flex w-full justify-center rounded-lg bg-indigo-600 px-3 py-2.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 transition-all duration-200 relative overflow-hidden disabled:opacity-70 disabled:cursor-not-allowed">
                  <span v-if="!isLoading">{{ $t('login.signin') }}</span>
                  <div v-else class="flex items-center">
                    <svg class="animate-spin -ml-1 mr-2 h-4 w-4 text-white" fill="none" viewBox="0 0 24 24">
                      <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                      <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                    </svg>
                    {{ $t('login.authenticating') }}
                  </div>
                </button>
              </div>
            </form>

            <div class="mt-8 pt-6 border-t border-gray-100">
              <div class="flex items-center justify-between text-xs text-gray-400">
                <div class="flex items-center space-x-2">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                  <span>{{ $t('app.version') }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const email = ref('')
const password = ref('')
const isLoading = ref(false)

const handleLogin = async () => {
  if (!email.value || !password.value) return
  isLoading.value = true
  await new Promise(resolve => setTimeout(resolve, 1200))
  isLoading.value = false
  router.push('/dashboard')
}
</script>

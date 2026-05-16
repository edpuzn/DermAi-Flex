<template>
  <div class="min-h-screen bg-[#0a0a0c] flex flex-col justify-center py-12 sm:px-6 lg:px-8 font-sans relative overflow-hidden">
    
    <!-- Premium Mesh Gradient Background -->
    <div class="absolute inset-0 z-0">
      <div class="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] bg-indigo-600/20 blur-[120px] rounded-full animate-pulse"></div>
      <div class="absolute bottom-[-10%] right-[-10%] w-[40%] h-[40%] bg-purple-600/10 blur-[120px] rounded-full"></div>
    </div>

    <div class="sm:mx-auto sm:w-full sm:max-w-md relative z-10">
      <div class="flex justify-center mb-6">
        <div class="bg-gradient-to-br from-indigo-500 to-indigo-700 p-4 rounded-3xl text-white shadow-[0_0_40px_rgba(79,70,229,0.3)] transform hover:scale-110 transition-all duration-500 cursor-pointer">
          <svg class="w-12 h-12" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 3v2m6-2v2M9 19v2m6-2v2M5 9H3m2 6H3m18-6h-2m2 6h-2M7 19h10a2 2 0 002-2V7a2 2 0 00-2-2H7a2 2 0 00-2 2v10a2 2 0 002 2zM9 9h6v6H9V9z"></path>
          </svg>
        </div>
      </div>
      <h2 class="text-center text-4xl font-black text-white tracking-tight drop-shadow-sm">
        {{ $t('login.title') }}
      </h2>
      <p class="mt-3 text-center text-sm text-gray-400 font-medium">
        {{ $t('login.subtitle') }}
      </p>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-md px-4 sm:px-0 relative z-10">
      <!-- Glassmorphism Card -->
      <div class="bg-white/[0.03] backdrop-blur-2xl py-10 px-8 shadow-[0_20px_50px_rgba(0,0,0,0.3)] rounded-[2.5rem] border border-white/10 sm:px-12 transition-all hover:border-white/20">
        
        <form class="space-y-7" @submit.prevent="handleLogin">
          <div>
            <label for="username" class="block text-[10px] font-black text-indigo-400 uppercase tracking-[0.2em] mb-2 ml-1">
              {{ $t('login.username') }}
            </label>
            <div class="relative group">
              <input 
                id="username" 
                v-model="username" 
                type="text" 
                required 
                class="block w-full px-5 py-4 bg-white/5 border border-white/10 rounded-2xl text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500/50 focus:border-indigo-500/50 transition-all hover:bg-white/[0.07]"
                placeholder="admin"
              />
              <div class="absolute inset-y-0 right-0 pr-4 flex items-center pointer-events-none text-gray-500 group-focus-within:text-indigo-400 transition-colors">
                <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>
              </div>
            </div>
          </div>

          <div>
            <label for="password" class="block text-[10px] font-black text-indigo-400 uppercase tracking-[0.2em] mb-2 ml-1">
              {{ $t('login.password') }}
            </label>
            <div class="relative group">
              <input 
                id="password" 
                v-model="password" 
                type="password" 
                required 
                class="block w-full px-5 py-4 bg-white/5 border border-white/10 rounded-2xl text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500/50 focus:border-indigo-500/50 transition-all hover:bg-white/[0.07]"
                placeholder="••••••••"
              />
              <div class="absolute inset-y-0 right-0 pr-4 flex items-center pointer-events-none text-gray-500 group-focus-within:text-indigo-400 transition-colors">
                <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 00-2 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
              </div>
            </div>
          </div>

          <div v-if="auth.error" class="bg-red-500/10 border border-red-500/20 text-red-400 px-5 py-4 rounded-2xl text-xs font-bold flex items-center gap-3 animate-shake">
            <svg class="w-5 h-5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
            {{ $t('login.error') }}
          </div>

          <div class="pt-2">
            <button 
              type="submit" 
              :disabled="auth.isLoading"
              class="w-full relative group overflow-hidden py-4 px-4 rounded-2xl bg-indigo-600 text-sm font-black text-white shadow-[0_10px_30px_rgba(79,70,229,0.4)] hover:shadow-[0_15px_40px_rgba(79,70,229,0.6)] transition-all duration-300 transform active:scale-[0.98] disabled:opacity-50"
            >
              <div class="absolute inset-0 bg-gradient-to-r from-indigo-500 to-purple-600 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
              <span class="relative z-10 flex justify-center items-center">
                <template v-if="auth.isLoading">
                  <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  {{ $t('login.processing') }}
                </template>
                <template v-else>{{ $t('login.submit') }}</template>
              </span>
            </button>
          </div>
        </form>

        <!-- Demo Info Glass Box -->
        <div class="mt-10 p-5 rounded-2xl bg-white/[0.02] border border-white/5 text-center">
          <p class="text-[9px] font-black text-gray-500 uppercase tracking-[0.3em] mb-3">{{ $t('login.demoAccess') }}</p>
          <div class="flex justify-center gap-4">
            <div class="text-[10px] text-gray-400">
              {{ $t('login.demoUser') }}: <span class="text-indigo-400 font-bold">admin</span>
            </div>
            <div class="w-px h-3 bg-white/10 mt-0.5"></div>
            <div class="text-[10px] text-gray-400">
              {{ $t('login.demoPass') }}: <span class="text-indigo-400 font-bold">admin123</span>
            </div>
          </div>
        </div>
      </div>
      
      <p class="mt-10 text-center text-[10px] text-gray-500 font-bold uppercase tracking-[0.2em]">
        &copy; 2026 DermAI-Flex Laboratory. {{ $t('app.version') }}
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const router = useRouter()
const auth = useAuthStore()

const username = ref('')
const password = ref('')

const handleLogin = async () => {
  const success = await auth.login(username.value, password.value)
  if (success) {
    router.push('/')
  }
}
</script>

<style scoped>
.animate-shake {
  animation: shake 0.5s cubic-bezier(.36,.07,.19,.97) both;
}

@keyframes shake {
  10%, 90% { transform: translate3d(-1px, 0, 0); }
  20%, 80% { transform: translate3d(2px, 0, 0); }
  30%, 50%, 70% { transform: translate3d(-4px, 0, 0); }
  40%, 60% { transform: translate3d(4px, 0, 0); }
}

input::placeholder {
  color: rgba(107, 114, 128, 0.5);
}
</style>

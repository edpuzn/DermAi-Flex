import { defineStore } from 'pinia'
import axios from 'axios'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: JSON.parse(localStorage.getItem('user')) || null,
    token: localStorage.getItem('token') || null,
    error: null,
    isLoading: false
  }),
  
  getters: {
    isAuthenticated: (state) => !!state.token
  },
  
  actions: {
    async login(username, password) {
      this.isLoading = true
      this.error = null
      try {
        const apiBase = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api'
        const response = await axios.post(`${apiBase}/auth/login`, {
          username,
          password
        })
        
        this.user = { username: response.data.username }
        this.token = response.data.access_token
        
        localStorage.setItem('user', JSON.stringify(this.user))
        localStorage.setItem('token', this.token)
        
        return true
      } catch (err) {
        this.error = err.response?.data?.detail || 'Giriş başarısız'
        return false
      } finally {
        this.isLoading = false
      }
    },
    
    logout() {
      this.user = null
      this.token = null
      localStorage.removeItem('user')
      localStorage.removeItem('token')
    }
  }
})

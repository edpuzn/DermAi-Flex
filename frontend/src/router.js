import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from './pages/LandingPage.vue'
import LoginPage from './pages/LoginPage.vue'
import Dashboard from './pages/Dashboard.vue'
import ResultPage from './pages/ResultPage.vue'
import HistoryPage from './pages/HistoryPage.vue'

import { useAuthStore } from './stores/auth'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: LandingPage
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginPage
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: { requiresAuth: true }
  },
  {
    path: '/results',
    name: 'Results',
    component: ResultPage,
    meta: { requiresAuth: true }
  },
  {
    path: '/history',
    name: 'History',
    component: HistoryPage,
    meta: { requiresAuth: true }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const auth = useAuthStore()
  if (to.meta.requiresAuth && !auth.isAuthenticated) {
    next('/login')
  } else if (to.path === '/login' && auth.isAuthenticated) {
    next('/dashboard')
  } else {
    next()
  }
})

export default router



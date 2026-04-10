import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from './views/LandingPage.vue'
import Login from './views/Login.vue'
import Dashboard from './views/DermatologyAnalysisHome.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: LandingPage
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

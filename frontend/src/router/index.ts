import { createRouter, createWebHistory } from 'vue-router'
import Chat from '@/views/Chat.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Chat
    }
  ]
})

export default router

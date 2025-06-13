import { createRouter, createWebHistory } from 'vue-router'
import Player from '@/views/Player.vue'

const routes = [
  { path: '/', component: Player }
]

export const router = createRouter({
  history: createWebHistory(),
  routes
})
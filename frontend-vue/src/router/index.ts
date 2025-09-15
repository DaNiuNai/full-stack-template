import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/stores/user'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', component: () => import('@/views/root.vue') },
    { path: '/login', component: () => import('@/views/login.vue') },
    { path: '/register', component: () => import('@/views/register.vue') },
  ],
})

// 访问拦截，只要没有token，且访问的是非登录页，就拦截到登录
router.beforeEach((to, from, next) => {
  const ignoredPaths = ['/login', '/register', '/'] // 定义需要忽略的路径
  const useStore = useUserStore()
  if (ignoredPaths.includes(to.path)) {
    next() // 直接放行
  } else {
    // 检查用户是否已登录
    if (!useStore.accessToken) {
      next('/login') // 如果需要认证但用户未登录，则重定向到登录页
    } else {
      next() // 放行
    }
  }
})

export default router

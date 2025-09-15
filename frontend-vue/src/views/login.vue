<script setup>
import { ref } from 'vue'
import { userLoginService } from '@/api/userBase'
import router from '@/router'
import { useUserStore } from '@/stores/user'

const username = ref('')
const password = ref('')

const userStore = useUserStore()

const login = async () => {
  const res = await userLoginService({ username: username.value, password: password.value })
  alert("登录成功")
  userStore.setAccessToken(res.access_token)
  router.push('/')
}
</script>
<template>
  <input type="text" placeholder="请输入用户名" v-model="username" />
  <input type="password" placeholder="请输入密码" v-model="password" />
  <button @click="login">登录</button>
</template>
<style scoped lang="scss"></style>

<script setup>
import { ref } from 'vue'
import { userRegisterService } from '@/api/userBase'
import router from '@/router'

const username = ref('')
const password = ref('')
const email = ref('')

const register = async () => {
  const res = await userRegisterService({
    username: username.value,
    password: password.value,
    email: email.value,
  })
  alert(res.data.message)
  router.push('/login')
}
</script>
<template>
  <input type="text" placeholder="请输入用户名" v-model="username" />
  <input type="password" placeholder="请输入密码" v-model="password" />
  <input type="text" placeholder="请输入邮箱" v-model="email" />
  <button @click="register">注册</button>
</template>
<style scoped lang="scss"></style>

<script setup>
import { userInfoService } from '@/api/userBase'

const getUserInfo = async () => {
  const res = await userInfoService()
  console.log(res.data)
}
</script>
<template>
  <button @click="$router.push('/login')">跳转到登录页</button>
  <button @click="$router.push('/register')">跳转到注册页</button>
  <button @click="getUserInfo">获取用户信息</button>
</template>
<style scoped lang="scss"></style>

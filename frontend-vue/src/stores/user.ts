import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useUserStore = defineStore(
  'user',
  () => {
    const accessToken = ref('')
    const setAccessToken = (newToken: string) => {
      accessToken.value = newToken
    }

    const removeAccessToken = () => {
      accessToken.value = ''
    }

    return {
      accessToken,
      setAccessToken,
      removeAccessToken,
    }
  },
  {
    persist: true,
  },
)

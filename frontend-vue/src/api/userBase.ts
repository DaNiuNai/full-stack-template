import requests from './requests'

//注册
export const userRegisterService = ({ username, password, email }: { username: string; password: string; email: string }) => {
  return requests.post('/user/register', { username, password, email })
}

//登录
export const userLoginService = ({ username, password }: { username: string; password: string }) => {
  return requests.post('/user/login', { username, password })
}

//获取用户信息
export const userInfoService = () => {
  return requests.get('/user/info')
}

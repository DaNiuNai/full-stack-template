from pydantic import BaseModel


# 用户-登录
class UserLogin(BaseModel):
    username: str
    password: str


# 用户-注册
class UserRegister(BaseModel):
    username: str
    password: str
    email: str

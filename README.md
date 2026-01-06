# FastAPI全栈模板

## 介绍

这个项目主要是用最简单的方法搭建一套可以快速开始开发的项目模板

包含用户注册登录、用户信息查询等基础功能，基于postgresql、sqlite数据库，使用JWT令牌进行用户认证和授权

为了保证工程足够简洁，前端我们把CSS部分留空了，只保留最基本的样式

JWT令牌会被Pinia自动持久化保存，并在每一次请求时添加到请求头`Authorization:Bearer {token}`中

## 技术栈

Vue前端：

- pnpm
- Vue3
- Vue Router
- TypeScript
- Pinia
- Pinia持久化插件
- Axios
- Sass

FastAPI后端：

- Python3.12
- FastAPI：后端框架
- SQLModel：数据库ORM
- python-jose：JWT令牌
- passlib：密码加密
- psycopg2: PostgreSQL数据库驱动

## 快速启动

```bash
git clone https://github.com/DaNiuNai/full-stack-template
```

### FastAPI后端

修改后端目录中的.env文件中的数据库配置

注意：如果你使用的不是sqlite，那么后端不会自动创建数据库，请自行创建，当创建完成后运行后端程序会自动创建表

python环境使用uv进行管理

```bash
cd backend-fastapi
uv run main.py
```

### Vue前端

```bash
cd frontend-vue
pnpm install
pnpm run dev
```

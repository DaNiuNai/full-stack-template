# FastAPI全栈模板

## 介绍

这个项目主要是用最简单的方法搭建一套可以快速开始开发的项目模板

包含用户注册登录、用户信息查询等基础功能

## 技术栈

前端：

- pnpm
- Vue3
- Vue Router
- TypeScript
- Pinia
- Pinia持久化插件
- Axios
- Sass

后端：

- Python3.12
- FastAPI：后端框架
- SQLModel：数据库ORM
- python-jose：JWT令牌
- passlib：密码加密

## 快速启动

```bash
git clone <仓库地址>
```

### 后端

python环境使用uv进行管理

```bash
cd backend
uv run main.py
```

### 前端

```bash
cd frontend
pnpm install
pnpm run dev
```

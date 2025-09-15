from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.core.config import settings
from src.core.database import create_db_and_tables
from src.api import router as api_router
from src.models.response import Message


app = FastAPI(title="fastapi-template-api")


# 配置 CORS 中间件，允许前端跨域请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许的来源列表，"*" 表示允许所有来源
    # allow_origins=["http://localhost:5173"],
    allow_credentials=True,  # 允许携带认证信息（cookies, authorization headers等）
    allow_methods=[
        "*"
    ],  # 允许的 HTTP 方法列表，"*" 表示允许所有方法 (GET, POST, OPTIONS等)
    allow_headers=["*"],  # 允许的请求头部列表，"*" 表示允许所有头部
)

# 挂载 API 路由
app.include_router(api_router)


# 根路由
@app.get("/")
def read_root():
    return Message(message="ok")


# 创建数据库和表
create_db_and_tables()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=settings.SERVER_HOST, port=settings.SERVER_PORT)

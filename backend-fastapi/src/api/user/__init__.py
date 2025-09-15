from fastapi import APIRouter
from . import base  # 相对导入同级目录下的模块

router = APIRouter(prefix="/user")

router.include_router(base.router)

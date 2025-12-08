from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import select

from src.models.response import Message
from src.models.request import UserRegister, UserLogin
from src.models.mapping import User
from src.core.database import DatabaseSessionDepends
from src.core.config import settings, log
from src.utils.auth import (
    get_password_hash,
    verify_password,
    create_jwt_token,
    get_current_user,
)

router = APIRouter()


@router.post("/register")
def user_register(
    user_create: UserRegister,
    db: DatabaseSessionDepends,
):
    """用户注册"""
    if not settings.USER_REGISTER:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="用户注册已禁用",
        )

    # 检查必填字段是否为空
    user_data = user_create.model_dump()
    for field, value in user_data.items():
        if not value:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"{field}不能为空",
            )

    # 检查用户名是否已存在
    existing_user = db.exec(
        select(User).where(User.username == user_create.username)
    ).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="用户名已被注册",
        )

    # 检查邮箱是否已存在
    existing_email = db.exec(
        select(User).where(User.email == user_create.email)
    ).first()
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="邮箱已被注册",
        )

    # 对密码进行哈希处理
    hashed_password = get_password_hash(user_create.password)

    # 创建新的数据库用户对象
    db_user = User(
        username=user_create.username,
        hashed_password=hashed_password,
        email=user_create.email,
    )

    # 将新用户添加到数据库会话并提交
    db.add(db_user)
    db.commit()
    log.info(f"新用户注册: {user_create.username}")

    return Message(message="注册成功")


@router.post("/login")
def user_login(
    user_login: UserLogin,
    db: DatabaseSessionDepends,
):
    """处理用户登录请求，验证成功后，返回 JWT Token"""
    # 1. 根据用户名从数据库查找用户
    user = db.exec(select(User).where(User.username == user_login.username)).first()

    # 2. 验证用户是否存在以及密码是否正确
    if not user or not verify_password(user_login.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="用户不存在或密码不正确",
        )

    # 3. 创建 JWT Token
    jwt_token = create_jwt_token(data=str(user.id))

    log.debug(f"用户: {user.username} 登录成功，生成 JWT Token: {jwt_token}")

    return {"access_token": jwt_token}


@router.get("/info")
def user_info(current_user: User = Depends(get_current_user)):
    """获取用户信息"""
    current_user.hashed_password = "xxxxxx"  # 隐藏密码
    return current_user

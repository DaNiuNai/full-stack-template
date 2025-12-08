from passlib.hash import pbkdf2_sha256
from datetime import timedelta, datetime, timezone
from jose import jwt
from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer

from src.core.database import DatabaseSessionDepends
from src.models.mapping import User
from src.core.config import settings


# 创建 OAuth2 密码授权方案
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """比较明文密码和哈希密码是否匹配"""
    return pbkdf2_sha256.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """对明文密码进行哈希处理"""
    return pbkdf2_sha256.hash(password)


def create_jwt_token(
    data: str, expire_minutes: int | float = settings.JWT_TOKEN_EXPIRE_MINUTES
) -> str:
    """根据给定的数据和过期时间创建JWT"""
    expire = datetime.now(timezone.utc) + timedelta(minutes=expire_minutes)
    to_encode = {"sub": str(data), "exp": expire}
    # 使用密钥和算法对数据进行编码，生成JWT字符串
    encoded_jwt = jwt.encode(
        to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )
    return encoded_jwt


def verify_jwt_token(token: str) -> str:
    """验证JWT Token并返回解码后的数据"""
    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
        )
        data = payload.get("sub")
        if data is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="登录异常"
            )
        return data
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="登录过期")


def get_token_from_header(token: str = Depends(oauth2_scheme)) -> str:
    """从请求头中提取JWT"""
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="未登录")
    return token


def get_current_user_id(token: str = Depends(get_token_from_header)) -> int:
    """FastAPI 依赖函数，用于获取当前JWT中的用户id"""
    data = verify_jwt_token(token)
    return int(data)


def get_current_user(
    db: DatabaseSessionDepends, user_id: str = Depends(get_current_user_id)
) -> User:
    """FastAPI 依赖函数，用于获取当前认证用户"""
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="用户不存在")
    return user

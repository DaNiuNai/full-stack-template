from sqlmodel import SQLModel, Field
from datetime import datetime, timezone
from typing import Optional


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, max_length=256)  # 用户名
    hashed_password: str  # 密码
    email: str = Field(unique=True, max_length=256)  # 邮箱
    registered_time: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), nullable=False
    )  # 注册时间

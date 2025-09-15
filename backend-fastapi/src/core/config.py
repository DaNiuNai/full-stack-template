import logging

from pydantic_settings import BaseSettings

# 配置类
class Settings(BaseSettings):
    LOG_LEVEL: str = "INFO"

    SERVER_HOST: str = "127.0.0.1"
    SERVER_PORT: int = 8080

    DATABASE_URL: str = "sqlite:///sqlite.db"
    SQL_ECHO: bool = False

    RESOURCES_DIR_PATH: str = "resources"

    JWT_SECRET_KEY: str = "your_jwt_secret_key"
    JWT_ALGORITHM: str = "HS256"
    JWT_TOKEN_EXPIRE_MINUTES: int = 525600  # JWT Token 的有效期（分钟）

    USER_REGISTER: bool = True

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# 实例化配置
settings = Settings()

# 设置日志等级
def configure_logging(log_level: str, app_name: str = "your_app_name") -> logging.Logger:
    """配置并返回应用程序的具名日志器。"""
    app_logger = logging.getLogger(app_name)
    # 如果已经有处理器了，说明已经配置过了，直接返回，避免重复添加处理器
    if not app_logger.handlers:
        app_logger.setLevel(log_level)  # 设置应用程序内部日志
        # 创建一个控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
        console_handler.setFormatter(formatter)
        app_logger.addHandler(console_handler)
        # app_logger.propagate = False

    return app_logger


log = configure_logging(settings.LOG_LEVEL)
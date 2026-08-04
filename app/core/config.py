from pydantic_settings import BaseSettings,SettingsConfigDict
from pathlib import Path


# 获取当前config.py所在目录
# config_dir = Path(__file__)
# 获取项目根目录，在当前目录的上一级目录
PROJECT_ROOT=  Path(__file__).parent.parent.parent
class Settings(BaseSettings):
    APP_NAME: str
    # 数据库配置
    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DATABASE: str
    # 日志配置
    LOG_PATH: str
    LOG_LEVEL: str


    # 配置文件路径
    # PROJECT_ROOT.joinpath(".env")表示在项目根目录下获取.env文件，用于存储环境变量。
    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT.joinpath(".env"),
        env_file_encoding="utf-8",extra="ignore"
    )
# 创建一个Settings对象，用于存储环境变量。
settings = Settings()

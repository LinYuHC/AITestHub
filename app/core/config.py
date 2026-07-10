from pydantic_settings import BaseSettings,SettingsConfigDict
from pathlib import Path


# 获取当前config.py所在目录
# config_dir = Path(__file__)
# 项目根目录，在当前目录的上一级目录
project_root =  Path(__file__).parent.parent.parent
class Settings(BaseSettings):
    APP_NAME: str

    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DATABASE: str

    model_config = SettingsConfigDict(env_file=project_root.joinpath(".env"),env_file_encoding="utf-8",extra="ignore")
settings = Settings()

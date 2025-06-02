from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List


class Settings(BaseSettings):
    TRACKED_SYMBOLS: List[str] = ["AUDUSD", "DXY", "EURUSD", "GBPUSD", "NZDUSD", "USDCAD", "USDCHF", "USDJPY", "GBPCHF"]
    WEBHOOK_URL: str
    PROJECT_NAME: str = "Trading Signal"
    DEBUG: bool = False
    DATABASE_URL: str = "sqlite:///./default.db"
    ALLOWED_ORIGINS: List[str] = ["*"]
    API_KEY: str = ""
    ACCOUNT: int
    PASSWORD: str
    SERVER: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()

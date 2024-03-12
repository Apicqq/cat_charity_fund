from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = "QRKot"
    description: str = ("API для приложения Благотворительного "
                        "фонда поддержки котиков QRKot")
    database_url: str = "sqlite+aiosqlite:///./fastapi.db"
    secret: str = "VeryDamnSecretSecret"

    class Config:
        env_file = ".env"


settings = Settings()

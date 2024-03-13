from typing import Optional

from pydantic import BaseSettings, EmailStr

from app.services.constants import ConfigConstants as Cconst


class Settings(BaseSettings):
    app_title: str = Cconst.APP_TITLE
    description: str = Cconst.DESCRIPTION
    database_url: str = Cconst.DATABASE_URL
    secret: str = Cconst.SECRET
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = ".env"


settings = Settings()

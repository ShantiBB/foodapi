import os

from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

ALLOWED_HOSTS = [host for host in os.getenv("ALLOWED_HOSTS").split(", ")]

class Settings(BaseSettings):
    django_key: str = os.getenv("DJANGO_KEY")
    debug_mode: bool = True if os.getenv("DEBUG_MODE") == "True" else False
    allowed_hosts: list[str] = []

    class Config:
        env_file = ".env"


settings = Settings()

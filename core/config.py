from typing import ClassVar
import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load .env file (Make sure this file exists)
load_dotenv()

class Settings(BaseSettings):
    # MONGODB_URL: str
    # BASE_URL: str
    # DATABASE_NAME: str
    # SECRET_KEY: str

    GEMINI_API_KEY: str
    ELEVEN_LAB_API_KEY: str
    GROQ_API_KEY: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

settings = Settings()

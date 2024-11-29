import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Configuration class
    """

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    CSRF_TRUSTED_ORIGINS: str = os.getenv("CSRF_TRUSTED_ORIGINS")


config = Config()

import os

from dotenv import load_dotenv


def get_env(key: str):
    load_dotenv()
    return os.getenv(key)

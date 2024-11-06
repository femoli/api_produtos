import os


class Settings:
    BASE_URL_MAINFRAME = os.getenv(
        "BASE_URL_MAINFRAME", "http://localhost:8001/XPTO")


settings = Settings()

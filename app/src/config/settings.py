import os


class Settings:
    API_BASE_URL = os.getenv("API_BASE_URL", "https://api.example.com")
    MF_ENDPOINT = os.getenv("MF_ENDPOINT", "https://mainframe.example.com")
    BFF_ENDPOINT = os.getenv("BFF_ENDPOINT", "https://bff.example.com")
    XPTO_TRANSACTION = "XPTO"


settings = Settings()

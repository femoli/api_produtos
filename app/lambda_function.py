from fastapi import FastAPI
from mangum import Mangum
from src.adapters.entrypoints.api.router import router

app = FastAPI()
app.include_router(router)

handler = Mangum(app)

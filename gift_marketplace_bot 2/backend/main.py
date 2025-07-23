from fastapi import FastAPI
from bot.main import start_bot
import asyncio

app = FastAPI()

@app.get("/products")
async def get_products():
    return [{"id": 1, "name": "🎁 Подарок 1"}, {"id": 2, "name": "🎁 Подарок 2"}]

@app.on_event("startup")
async def startup():
    asyncio.create_task(start_bot())
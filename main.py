from aiogram import Bot, Dispatcher, types, F
from fastapi import FastAPI, Request
from aiogram.types import Update
from aiogram.webhook.aiohttp_server import SimpleRequestHandler

import asyncio
TOKEN = "8439567445:AAHnQ3OK-27cLIz5xTrUlM6_gzZlESVUhdw"
bot = Bot(token=TOKEN)
dp = Dispatcher()
WEBHOOK_URL = f"https://mybot-9m40.onrender.com/webhook"
app = FastAPI()

types.ContentType

@dp.message(F.text=='/start')
async def start(message: types.Message):
    await message.answer(text="Assalamu alaykum bratiiiim!")


@dp.message(F.text=='/location')
async def photo_handler(message: types.Message):
    latitude = 44.287382516166296
    longitude = 65.2055360005088
    await message.answer_location(latitude=latitude, longitude=longitude)

@dp.message(F.text=='/contact')
async def photo_handler(message: types.Message):
    await message.answer_contact(phone_number='+998994786207', first_name="Hech kimsan")


@dp.message(F.voice)
async def voice_handler(message: types.Message):
    print(message.voice)
    await message.answer_voice(voice=message.voice.file_id)

@dp.message(F.contact)
async def contact_handler(message: types.Message):
    print(message.contact)
    await message.answer_contact(phone_number=message.contact.phone_number, first_name=message.contact.first_name)

@app.post(WEBHOOK_PATH)
async def webhook(request: Request):
    data = await request.json()
    update = Update(**data)
    await dp.feed_update(bot, update)
    return {"ok": True}

@app.on_event("startup")
async def on_startup():
    await bot.set_webhook(WEBHOOK_URL)



import os
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message,
    CallbackQuery,
)
from pyrogram import Client, filters
from pyrogram.errors import MessageNotModified
from dotenv import load_dotenv
from pyromod import listen 

load_dotenv()


Bot = Client(
    name="confess",
    bot_token=os.environ.get("BOT_TOKEN", "5699253839:AAG3OLhh8YcuVskn0tkrOrYZZ-Nbon_4Faw"),
    api_id=int(os.environ.get("API_ID", "25753386")),  # type: ignore
    api_hash=os.environ.get("API_HASH", "a23259feb6493d32fce2ed8ec3350546"),
    sleep_threshold=3600,
)


@Bot.on_message(filters.command(["start"]))
async def start(_, update: Message):
    await update.reply_text(
        f"Hello {update.from_user.mention}, I am a telegram bot module for counting total number of clicks on a button.\n\nMade By @phobiakaliann"
    )


@Bot.on_message(filters.command(["confes"]))
async def confess(_, update: Message):
    user_id = update.chat.id
    nama = await Bot.ask(user_id, 'Masukan Nama kamu', filters=filters.text)
    tujuan = await Bot.ask(user_id, 'Kepada siapa yang ingin kamu confess?', filters=filters.text)
    isi = await bot.ask(user_id, 'apa yang ingin kamu sampaikan', filters=filters.text)
    await Bot.send_message(user_id, f"📬 <b>Confess</b>\n\nFrom : {nama}\nTo : {tujuan}\nIsi : {isi}")

Bot.run()

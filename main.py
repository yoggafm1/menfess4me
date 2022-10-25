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
    api_id=int(os.environ.get("API_ID", "23693414")),  # type: ignore
    api_hash=os.environ.get("API_HASH", "7886b6a15d0a1a06c7feeaeeb6ad6210"),
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
    LOG = -1001661793479
    nama = await Bot.ask(user_id, 'Masukan Nama kamu', filters=filters.text)
    tujuan = await Bot.ask(user_id, 'Kepada siapa yang ingin kamu confess?', filters=filters.text)
    isi = await Bot.ask(user_id, 'apa yang ingin kamu sampaikan', filters=filters.text)
    await Bot.send_message(LOG, f"📬 <b>Confess</b>\n\n<b>From :</b> <i>{nama}</i>\n<b>To :</b> <i>{tujuan}</i>\n<b>Isi :</b> <i>{isi}</i>")

Bot.run()

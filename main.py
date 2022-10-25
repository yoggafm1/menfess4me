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
)


@Bot.on_message(filters.command(["start"]))
async def start(_, update: Message):
    await update.reply_text(
        f"Hello {update.from_user.mention}, I am a telegram bot module for counting total number of clicks on a button.\n\nMade By @phobiakaliann"
    )
    
LOG=-1001661793479

@Bot.on_message(filters.command(["confes"]))
async def confess(client: Client, update: Message):
    user_id = update.chat.id
    confess = await client.ask(user_id, 'Masukan format\n`From: (nama kmu/anonim)\nTo : (Wajib)\nIsi: (wajib)`')
    await client.send_message(LOG, f"📬 <b>Confess</b>\n\n{confess.text}")

Bot.run()

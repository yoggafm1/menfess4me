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
        f"Hello {update.from_user.mention}, Ini adalah bot confess milik @pintarmutualan\nJika kalian ingin confess silakan ketik /confes dan ikutin langkah-langkahnya nanti otomatis akan terkirim ke @fvconfess"
    )
    
LOG=-1001661793479

@Bot.on_message(filters.command(["confes"]))
async def confess(client: Client, update: Message):
    user_id = update.chat.id
    nama = await client.ask(user_id, 'Ketik Nama kamu', filters=filters.text, timeout=30)
    tujuan = await client.ask(user_id, 'ketik nama crush kamu', filters=filters.text, timeout=30)
    isi = await client.ask(user_id, 'ketik apa yang ingin kamu sampaikan', filters=filters.text, timeout=30)
    report = await client.send_message(LOG, f"📬 <b>Confess</b>\n\n<b>From :</b> <i>{nama.text}</i>\n<b>To :</b> <i>{tujuan.text}</i>\n<b>Isi :</b> <i>{isi.text}</i>")
    await client.send_message(user_id, f"https://t.me/dankdnkaknd/{report.message_id}")
    
Bot.run()

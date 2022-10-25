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
    bot_token=os.environ.get("BOT_TOKEN", "5626754813:AAEJN4QevmwDmpkeliXjpF7GR4ABnR9rAi4"),
    api_id=int(os.environ.get("API_ID", "23693414")),  # type: ignore
    api_hash=os.environ.get("API_HASH", "7886b6a15d0a1a06c7feeaeeb6ad6210"),
)


@Bot.on_message(filters.command(["start"]))
async def start(_, update: Message):
    await update.reply_text(
        f"Hello {update.from_user.mention}, Ini adalah bot confess milik @pintarmutualan\nJika kalian ingin confess silakan ketik /confes dan ikutin langkah-langkahnya nanti otomatis akan terkirim ke @fvconfess"
    )
    
LOG=-1001593451768

@Bot.on_message(filters.command(["confes"]))
async def confess(client: Client, update: Message):
    user_id = update.chat.id
    nama = await client.ask(user_id, '🗣 <b>Ketik Nama kamu</b>\n\n<b>Informasi :</b> __Pakai nama kamu,Jika ingin privasi nama silakan gunakan `Anonim` saja__', filters=filters.text, timeout=30)
    await nama.delete()
    tujuan = await client.ask(user_id, '🗣 <b>Ketik Nama Crush kamu</b>\n\n<b>Informasi :</b> __Wajib pakai username/nama__', filters=filters.text, timeout=30)
    await tujuan.delete()
    isi = await client.ask(user_id, f"🗣 <b>Ketik apa yang ingin kamu sampaikan kepada {tujuan.text}</b>", filters=filters.text, timeout=30)
    await isi.delete()
    report = await client.send_message(LOG, f"<b>From :</b> <i>{nama.text}</i>\n<b>To :</b> <i>{tujuan.text}</i>\n<b>Isi :</b> <i>{isi.text}</i>")
    await client.send_message(user_id, f"✅ **Sudah terkirim**", 
                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("➡ View", url=f"https://t.me/fvconfess/{report.id}")]]),
                              disable_web_page_preview=True,
                             )
    
Bot.run()

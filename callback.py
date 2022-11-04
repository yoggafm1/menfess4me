from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from pyrogram.errors import MessageNotModified
from pyromod import listen 
from main import *
PVA=-1001847941518
@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
  await query.message.delete()
  await Bot.send_photo(query.chat.id,
                       photo=KONTOL,
                       caption=Start_text,
                       reply_markup=InlineKeyboardMarkup(
                         [
                           [
                             InlineKeyboardButton("⛔️ Rules", callback_data="rules"),
                             InlineKeyboardButton("Penjelasan 📝", callback_data="penjelasan"),
                           ],
                           [
                             InlineKeyboardButton("🔰 Menu 🔰", callback_data="menu_home"),
                           ],
                         ]
                       ),
                      )

  
RULES_TEXT = """🗣️ RULES Official Fantasy

❌ PROMOSI TANPA IZIN
❌ UP 18+ TANPA IZIN
❌ JUALAN TANPA IZIN
❌ UP LINK TANPA IZIN

🗣️ RESIKO AUTO BAN"""

@Client.on_callback_query(filters.regex("rules"))
async def rulescb(_, query: CallbackQuery):
  await query.message.delete()
  await Bot.send_photo(query.chat.id,
                       photo=KONTOL,
                       caption=RULES_TEXT,
                       reply_markup=InlineKeyboardMarkup(
                         [
                           [
                             InlineKeyboardButton("🔙 Back", callback_data="cbstart"),
                           ],
                         ]
                       ),
                      )  
PENJELASAN_TEXT = """
<b>APA ITU MENFESS?</b>
📝 Berdasarkan penelusuran di media sosial, istilah menfess kerap digunakan ketika seseorang ingin mengungkapkan sesuatu kepada orang lain atau semua orang secara anonim

<b>APA ITU BIRO JODOH?</b>
📝 Berdasarkan Kamus besar, istilah biro jodoh adalah badan usaha jasa untuk menjodohkan pria atau wanita.

<b>APA ITU KRITIK?<b>
📝 Kritik itu adalah kecaman atau tanggapan, kadang-kadang disertai uraian dan pertimbangan baik buruk thd suatu hasil karya, pendapat, dsb; (nomina).
""""
@Client.on_callback_query(filters.regex("penjelasan"))
async def penjelasan(_, query: CallbackQuery):
  await query.message.delete()
  await Bot.send_photo(query.chat.id,
                       photo=KONTOL,
                       caption=PENJELASAN_TEXT,
                       reply_markup=InlineKeyboardMarkup(
                         [
                           [
                             InlineKeyboardButton("🔙 Back", callback_data="cbstart"),
                           ],
                         ]
                       ),
                      )    
HOME_TEXT = """
<b>📪 Confess - Untuk Confess.
💞 Biro Jodoh - untuk mengikuti biro jodoh.
🗣 Kritik - Untuk mengkritik admin.</b>

<i>Klik tombol dibawah sesuai yang kamu mau</i>
"""
@Client.on_callback_query(filters.regex("menu_home"))
async def menu_home(_, query: CallbackQuery):
  await query.message.delete()
  await Bot.send_photo(query.chat.id,
                       photo=KONTOL,
                       caption=HOME_TEXT,
                       reply_markup=InlineKeyboardMarkup(
                         [
                           [
                             InlineKeyboardButton("🗣 Kritik", callback_data="cbkritik"),
                             InlineKeyboardButton("Confess 📪", callback_data="cbstart"),
                           ],
                           [
                             InlineKeyboardButton("💞 Biro Jodoh 💞", callback_data="cbstart"),
                           ],
                         ]
                       ),
                      )     
  
@Client.on_callback_query(filters.regex("cbkritik"))
async def cbkritik(client, query: CallbackQuery):
  await query.message.delete()  
  user_id = query.from_user.id
  Tujuan = await client.ask(user_id, '🗣 <b>Silakan ketik apa yang kamu ingin sampaikan kepada admin.</b>', filters=filters.text, timeout=30)
  if (tujuan.text == "/start"
      or tujuan.text == "/confes"
      or tujuan.text == "/kritik"
      or tujuan.text == "/help"
     ):
    kri = await client.ask(user_id, '<b>⚠️ Terjadi kesalahan.</b>\n__Ketikan apa yang kamu ingin katakan kepada admin__')
  else:
    kri = tujuan
  await client.send_message(PVA, f"from {query.from_user.mention}\nisi : {kri.text}")
  await client.send_message(query.from_user.id, "Kritik kamu telah terkirim")
  

  
  
  
  

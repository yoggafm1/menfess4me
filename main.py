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
    bot_token=os.environ.get("BOT_TOKEN", "5609275386:AAEZyazPN9u8ai9G5Kg4xuUvR9UTgfY0y3k"),
    api_id=int(os.environ.get("API_ID", "26560795")),  # type: ignore
    api_hash=os.environ.get("API_HASH", "9149c43550bd4c5dbeda468900c93901"),
)
KR=-1001839097484
Start_text = """<i>Hallo! [Anonim 4Me](https://t.me/Anonim4Mebot) akan membantumu untuk mengirimkan pesan secara anonim ke Grup & Channel.

Sebelum menggunakan silakan baca rules terlebih dahulu ya🥰</i>

<b>👤 Anon Grup </b>- <i>Untuk Pesan Anon Grup</i>
<b>🎮 Arena 4Me </b>- <i>Untuk Pesan Arena 4Me</i>
<i>Klik tombol dibawah sesuai yang kamu mau</i>

<b>Butuh bantuan? Hubungi</b> @Chat4Robot"""
KONTOL = "https://telegra.ph/file/3d0fa0a56b2e91d1b06d9.jpg"
HOME_TEXT = """
<b>📪 Confess - Untuk Confess.
🗣 Kritik - Untuk mengkritik admin.</b>
<i>Klik tombol dibawah sesuai yang kamu mau</i>
"""

@Bot.on_message(filters.command(["start"]))
async def start(_, update: Message):
    await update.reply_photo(
        photo=KONTOL,
        caption=Start_text,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⛔️ Rules", callback_data="rules"),
                    InlineKeyboardButton("Penjelasan 📝", callback_data="penjelasan"),
                ],
                 [
                             InlineKeyboardButton("👤 Anonim Grup", callback_data="cbkritik"),
                     ],
	               [
                             InlineKeyboardButton("🎮 Arena 4Me", callback_data="cbconfess"),
                ],
            ]
        )
    )
    
RULES_TEXT = """📢 Peraturan Anonim 4Me

1. dilarang dm berisikan hal yg mengundang war (bersifat menjatuhkan suatu fandom, grup, agama, suku maupun ras)
2. dilarang mengirim menfess yang memuat data pribadi secara terang-terangan sekalipun data pribadi sendiri seperti nomor hp
3. dilarang berjualan barang apapun

📢 Owner/Admin tidak akan ikut campur dan tau menau tentang menfess yang masuk serta tidak akan membeberkan siapa si pengirim menfess terkecuali kalau pengirim melanggar RULES yang sudah dibuat diatas dan akan mendapatkan kosekuensinya

•PELANGGARAN RINGAN AKAN DITEGUR
•PELANGGARAN BERAT AKAN DI POST DAN DI BLOK PERMANEN"""

@Bot.on_callback_query(filters.regex("rules"))
async def rulescb(_, query: CallbackQuery):
  await query.message.delete()
  await Bot.send_photo(query.message.chat.id,
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
<b>Apa Itu Menfess ?</b>
<b>•</b> Menfess adalah singkatan dalam bahasa Inggris dari "mention confess" yang memiliki makna kurang lebih "surat kaleng" atau "pesan anonim".

<b>Apa Itu Anonim ?</b>
<b>•</b> Arti anonim adalah tanpa nama atau identitas atau tidak dikenali.
"""
@Bot.on_callback_query(filters.regex("penjelasan"))
async def penjelasan(_, query: CallbackQuery):
  await query.message.delete()
  await Bot.send_photo(query.message.chat.id,
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
    
@Bot.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
  await query.message.delete()
  await Bot.send_photo(query.message.chat.id,
                       photo=KONTOL,
                       caption=Start_text,
                       reply_markup=InlineKeyboardMarkup(
                         [
                           [
                             InlineKeyboardButton("⛔️ Rules", callback_data="rules"),
                             InlineKeyboardButton("Penjelasan 📝", callback_data="penjelasan"),
                           ],
                           [
                             InlineKeyboardButton("👤 Anonim Grup", callback_data="cbkritik"),
                           ],
	                       [
                             InlineKeyboardButton("🎮 Arena 4Me", callback_data="cbconfess"),
                            ],
                         ]
                       ),
                      )
    
@Bot.on_callback_query(filters.regex("home_ban"))
async def home_ban(_, query: CallbackQuery):
  await query.message.delete()
  await Bot.send_photo(query.message.chat.id,
                       photo=KONTOL,
                       caption=HOME_TEXT,
                       reply_markup=InlineKeyboardMarkup(
                         [
                           [
                             InlineKeyboardButton("🗣 Kritik", callback_data="cbkritik"),
                             InlineKeyboardButton("Confess 📪", callback_data="cbconfess"),
                           ]
                         ]
                       ),
                      ) 
PVA=-1001854811904
ADI=-1001792566616    
@Bot.on_callback_query(filters.regex("cbkritik"))
async def cbkritik(client, query: CallbackQuery):
  await query.message.delete()  
  user_id = query.from_user.id
  Tujuan = await client.ask(user_id, '🗣 <b>Silakan ketik apa yang kamu ingin sampaikan di Anon Grup</b>', filters=filters.text, timeout=30)
  if "/" in Tujuan.text:
    kri = await client.ask(user_id, '<b>⚠️ Terjadi kesalahan.</b>\n__Ketikan apa yang kamu ingin katakan  di Anon Grup__')
  else:
    kri = Tujuan
  await client.send_message(PVA, f" {kri.text}")
  await client.send_message(ADI, f"<b>•Dari: </b> {query.from_user.first_name} [<pre>{query.from_user.id}</pre>]\n<b>•Pesan: </b> <i>{kri.text}</i>")
  await client.send_message(query.from_user.id, "Pesan kamu telah terkirim")
    
LOG=-1001502192084
ADM=-1001792566616

@Bot.on_callback_query(filters.regex("cbconfess"))
async def cbconfess(client, query: CallbackQuery):
    await query.message.delete()  
    user_id = query.from_user.id
    nama = await client.ask(user_id, '🗣 <b>Ketik Nama kamu</b>\n\n<b>Informasi :</b> __Pakai nama kamu,Jika ingin privasi nama silakan gunakan /secret saja__', filters=filters.text, timeout=30)
    if "/" in nama.text:
        nama = "secret"
    else:
        nama = nama.text
    tujuan = await client.ask(user_id, '🗣 <b>Ketik Nama Crush kamu</b>\n\n<b>Informasi :</b> __Wajib pakai username/nama__', filters=filters.text, timeout=30)
    if "/" in tujuan.text:
        to = await client.ask(user_id, '<b>⚠️ Terjadi kesalahan.</b>\n__Ketik nama crush kamu__', filters=filters.text, timeout=30)
        if "/" in to.text:
            return await client.send_message(user_id, 'Sepertinya anda masih bodoh, silakan bertanya kepada @Chat4Robot')
        else:
            to = to
    else:
        to = tujuan
    isi = await client.ask(user_id, f"🗣 <b>Ketik apa yang ingin kamu sampaikan kepada {to.text}</b>", filters=filters.text, timeout=30)
    if "/" in isi.text:
        confesss = await client.ask(user_id, '<b>⚠️ Terjadi kesalahan.</b>\n__Ketik apa yang kamu ingin sampaikan kepada crush__', filters=filters.text, timeout=30)

    else:
        
        confesss = isi
    report = await client.send_message(LOG, f"<b>From :</b> <i>{nama}</i>\n<b>To :</b> <i>{to.text}</i>\n<b>Isi :</b> <i>{confesss.text}</i>", disable_web_page_preview=True)
    await client.send_message(user_id, f"Terima kasih telah menggunakan bot ini, pesan Anda akan segera dikirim.", 
                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("➡ Lihat Pesan", url=f"https://t.me/arena4me/{report.id}")]]),
                              disable_web_page_preview=True,
                             )
    await client.send_message(ADM, f"<b>•Dari: </b> {query.from_user.first_name} [<pre>{query.from_user.id}</pre>]\n<b>•Pesan: </b> <i>{confesss.text}</i>\n  <a href='https://t.me/c/1874589177/{report.id}'>Lihat Pesan</a>")

    
    
Bot.run()


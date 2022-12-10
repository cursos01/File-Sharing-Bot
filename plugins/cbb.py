#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n○ Cursos : <code>Ingenieriacivil</code>\n○ Facebook : <a href='https://www.facebook.com/profile.php?id=100069992134197/'>Facebook</a>\n○ Descargas Bibliocad : <a href='https://youtu.be/gBm6BOMu-_0'>Click Aqui</a>\n○ Canal : @cursocivil\n○ Admi Grupo : @Comun_Ing_Arq_bot</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

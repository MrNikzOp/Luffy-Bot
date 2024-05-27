from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from plugins.config import Config
from plugins.script import Translation
from plugins.functions.forcesub import handle_force_subscribe


# Invite command handler
@Client.on_message(filters.private & filters.command("invite"))
async def about(client, message):
    if Config.CHANNEL:
      fsub = await handle_force_subscribe(client, message)
      if fsub == 400:
        return
  #  await message.reply_photo(photo)  
    await message.reply_text(
        text=Translation.ABOUT_TXT,
        disable_web_page_preview=True,
        reply_markup=BUTTONS)

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from plugins.config import Config
from plugins.script import Translation
from plugins.functions.forcesub import handle_force_subscribe

PIC = "https://telegra.ph/file/72b1efaa44944d2b9e1b9.jpg"

# Invite command handler
@Client.on_message(filters.private & filters.command("invite"))
async def about(client, message):
    if Config.CHANNEL:
      fsub = await handle_force_subscribe(client, message)
      if fsub == 400:
        return
  #  await message.reply_photo(photo)  
    await message.reply_photo(
        photo=PIC,
        caption=Translation.ABOUT_TXT,
        disable_web_page_preview=True,
        reply_markup=BUTTONS
    )

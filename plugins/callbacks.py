import os
from plugins.functions.display_progress import progress_for_pyrogram, humanbytes
from plugins.config import Config
from plugins.script import Translation
from pyrogram import Client, types
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from plugins.database.database import db
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@Client.on_callback_query()
async def button(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=Translation.START_TEXT.format(update.from_user.mention),
            reply_markup=Translation.START_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "premium":
        await update.message.edit_text(
            text=Translation.DETAILS_TEXT.format(update.from_user.mention),
            reply_markup=Translation.PREMIUM_BUTTONS,
            disable_web_page_preview=True
        )
      elif update.data == "about":
        await update.message.edit_text(
            text=Translation.ABOUT_TEXT,
            reply_markup=Translation.ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "qr":
        await update.message.edit_text(
            text=Translation.QR_TEXT,
            reply_markup=Translation.ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    elif "close" in update.data:
        await update.message.delete(True)

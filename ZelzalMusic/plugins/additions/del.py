import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from ZelzalMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZelzalMusic import app




########################### بوت حذف
@app.on_message(filters.command(["حذف", "عاوز احذف", "بوت حذف"], ""))
async def svksksa(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/a6137caa707bdb1247d7c.jpg",
        caption=f"""[خش احذف محدش هيمسك فيك يصحبي 🖤]""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• اضـغـط للـدخول للـبوت", url=f"https://t.me/LC6BOT")
                ]
           ]
        ),
    )
   

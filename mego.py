import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZelzalMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZelzalMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["مجودة","ماجدد","ماجد","ماقد","ماجد الهكر","ماقدد","الهكور","هكر القلوب","ماقد","مجود","مجودهه","مجوده","ماجد الهكر","مجودةةة"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/e8f0760f4b5a1bea717cd.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪𝙈 𝘼 𝙂 𝙄 𝘿 ❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @M_8_9 ❫
◉ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 : ❪ @V_C_B.t.me ❫
◉ 𝙱𝙸𝙾    : ❪هذا المُستخدم بانتظار جبر الله وكلهُ يقين 💖 
](https://t.me/Q_E_M❫""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "𝙈 𝘼 𝙂 𝙄 𝘿", url=f"https://t.me/M_8_9"),
            ]
        ]
         ),
     )
  

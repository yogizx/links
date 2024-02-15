#(©)NovaXTG

import asyncio
import aiohttp
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
from bot import Bot
from config import *
from helper_func import encode
from shortzy import Shortzy
from shortlink import get_shortlink

@Bot.on_message(filters.private & (filters.document | filters.video | filters.audio | filters.photo) & ~filters.command(['start','users','post','broadcast','batch','genlink','stats','combine','saami']))
async def channel_post(client: Client, message: Message):
    reply_text = await message.reply_text("Please Wait...!", quote = True)
    try:
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except Exception as e:
        print(e)
        await reply_text.edit_text("Something went Wrong..!")
        return
    converted_id = post_message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    media = message.document or message.video or message.audio or message.photo
    filesize = humanbytes(media.file_size) if media.file_size else ""
    filename = media.file_name if media.file_name else ""
    link = await get_shortlink(f"https://t.me/{client.username}?start={base64_string}")
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("💸 Yᴏᴜ ᴄᴀɴ sʜᴀʀᴇ ᴛʜɪs ᴛᴏ ᴀɴʏ ᴄʜᴀᴛs 💸", url=f'https://telegram.me/share/url?url={link}')]])
    
    await reply_text.edit(f"<b>🦋 ꜰ ɪ ʟ ᴇ    ɴ ᴀ ᴍ ᴇ 🦋 </b>\n <b><i>{filename} </i></b>\n\n <b>🎁 ꜰ ɪ ʟ ᴇ    ꜱ ɪ ᴢ ᴇ 🎁 </b> <b><i>{filesize} </i></b>\n\n <b>⚡️ ᴅ ᴏ ᴡ ɴ ʟ ᴏ ᴀ ᴅ    ʟ ɪ ɴ ᴋ ⚡️</b>\n <i>{link}</i>\n\n <b>🔮 ʜ ᴏ ᴡ   ᴛ ᴏ   ᴏ ᴘ ᴇ ɴ   ʟ ɪ ɴ ᴋ 🔮</b> /n <b>https://t.me/How_To_Download_Video_tnlink</b> \n\n  <b>🎭 ᴛʜᴇᴀᴛʀᴇ  ʀᴇʟᴇᴀꜱᴇ  ᴄʜᴀɴɴᴇʟ 🎭</b> \n <b>https://t.me/+roeQbRbbk1NiMWM9</b> \n\n <b> 🍿 ᴏᴛᴛ ʀᴇʟᴇᴀꜱᴇ ᴄʜᴀɴɴᴇʟ 🍿<\b> \n <b>https://t.me/+m-vtWbQbJKYzMmQ9</b> \n\n <a href=https://t.me/moviemaster_yogi><b>©️ мσνιє мαѕтєя™️</b></a></b>", reply_markup=reply_markup, disable_web_page_preview = True)
    if not DISABLE_CHANNEL_BUTTON:
        await post_message.edit_reply_markup(reply_markup)

@Bot.on_message(filters.channel & (filters.document | filters.video | filters.audio | filters.photo) & filters.incoming & filters.chat(CHANNEL_ID))
async def new_post(client: Client, message: Message):

    if DISABLE_CHANNEL_BUTTON:
        return

    converted_id = message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    media = message.document or message.video or message.audio or message.photo
    filesize = humanbytes(media.file_size) if media.file_size else ""
    filename = media.file_name if media.file_name else ""
    link = await get_shortlink(f"https://t.me/{client.username}?start={base64_string}")
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("💸 Yᴏᴜ ᴄᴀɴ sʜᴀʀᴇ ᴛʜɪs ᴛᴏ ᴀɴʏ ᴄʜᴀᴛs 💸", url=f'https://telegram.me/share/url?url={link}')]])
    try:
        await message.edit_reply_markup(reply_markup)
    except Exception as e:
        print(e)
        pass
    

def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'

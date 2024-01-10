#(©)NovaXTG

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot
from database.database import *
import asyncio
import aiohttp
from config import *
import os
from shortlink import get_shortlink
from shortzy import Shortzy
from helper_func import encode, get_message_id

CMD = ["/", "."]

@Bot.on_message(filters.private  & filters.command('post'))
async def post(client: Client, message: Message):
    try:
        num_files = await client.ask(text="<b>ʜᴏᴡ ᴍᴀɴʏ ғɪʟᴇs ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ ɪɴ ᴏɴᴇ ᴛᴇxᴛ⁉</b>", chat_id=message.from_user.id, filters=filters.text, timeout=60)
        num_files = int(num_files.text)  # Convert the user's response to an integer
    except:
        return
    
    media_list = []
    for i in range(num_files):
        try:
            forward_message = await client.ask(text=f"<b>⏩ ғᴏʀᴡᴀʀᴅ ᴛʜᴇ ɴᴏ : {i+1} ғɪʟᴇ ғᴏʀ ʏᴏᴜʀ ᴘᴏsᴛ ᴛᴇxᴛ\n\n🚸 ɴᴏᴛᴇ : ᴏɴʟʏ ʏᴏᴜ ᴄᴀɴ ғᴏʀᴡᴀʀᴅ ғɪʟᴇs ғʀᴏᴍ ᴅʙ ᴄʜᴀɴɴᴇʟ (ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ᴛᴀɢ!!)</b>", chat_id=message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        media = forward_message.document or forward_message.video
        filename = media.file_name if media.file_name else ""
        filename_without_underscores = filename.replace("_", " ")
        filename_words = filename_without_underscores.split()[:5]
        shortened_filename = ' '.join(filename_words)
        file_size = humanbytes(media.file_size) if media.file_size else ""
        msg_id = await get_message_id(client, forward_message)
        if msg_id:
            media_list.append((media, file_size, msg_id))
    
    links = []
    for i, (media, file_size, msg_id) in enumerate(media_list):
        string = f"get-{msg_id * abs(client.db_channel.id)}"
        base64_string = await encode(string)
        link = await get_shortlink(f"https://telegram.me/{client.username}?start={base64_string}")
        links.append(f"<b>{file_size} :</b> <i>{link}</i>")
    
    link_lines = '\n\n'.join(links)
    caption = f"<b>{shortened_filename} 👇🏻👇🏻</b>\n\n<i>🔻 Direct Telegram Files 🔻</i>\n\n{link_lines}\n\n<b></b>"
    
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Copy Text", callback_data='copy')]])
    await message.reply_text(caption, quote=True, reply_markup=None)


@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('batch'))
async def batch(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(text = "Forward the First Message from DB Channel (with Quotes)..\n\nor Send the DB Channel Post Link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        else:
            await first_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue

    while True:
        try:
            second_message = await client.ask(text = "Forward the Last Message from DB Channel (with Quotes)..\nor Send the DB Channel Post link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        else:
            await second_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue


    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = f"https://telegram.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("💸 Yᴏᴜ ᴄᴀɴ sʜᴀʀᴇ ᴛʜɪs ᴛᴏ ᴀɴʏ ᴄʜᴀᴛs 💸", url=f'https://telegram.me/share/url?url={link}')]])
    await second_message.reply_text(f"<b>🦋 ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ : </b><i><b>{link}</b></i>\n\n<i>© @leomoviestamil</i>", quote=True, reply_markup=reply_markup)
    
@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('genlink'))
async def link_generator(client: Client, message: Message):
    while True:
        try:
            channel_message = await client.ask(text = "Forward Message from the DB Channel (with Quotes)..\nor Send the DB Channel Post link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        msg_id = await get_message_id(client, channel_message)
        if msg_id:
            break
        else:
            await channel_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is not taken from DB Channel", quote = True)
            continue

    base64_string = await encode(f"get-{msg_id * abs(client.db_channel.id)}")
    link = f"https://telegram.me/{client.username}?start={base64_string}"
    await channel_message.reply_text(f"<b>ʏᴏᴜʀ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ❗️</b>\n\n<b>💎 ғɪʟᴇ ɴᴀᴍᴇ : </b> \n\n<b>💫 ғɪʟᴇ sɪᴢᴇ : </b>\n\n<b>🦋 ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ : </b><i><b>{link}</b></i>\n\n<i>© @Monaserials</i>", quote=True, reply_markup=reply_markup)

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('combine'))
async def combine(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(text = "Forward the First one", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        media1 = first_message.document or first_message.video
        filename = media1.file_name if media1.file_name else ""
        filename_without_underscores = filename.replace("_", " ")
        filename_words = filename_without_underscores.split()[:5]
        shortened_filename = ' '.join(filename_words)
        filesize1 = humanbytes(media1.file_size) if media1.file_size else ""
        f1_msg_id = await get_message_id(client, first_message)
        if f1_msg_id:
            break
        else:
            await first_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue

    while True:
        try:
            second_message = await client.ask(text = "Forward the second one", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        media2 = second_message.document or second_message.video
        filesize2 = humanbytes(media2.file_size) if media2.file_size else ""
        f2_msg_id = await get_message_id(client, second_message)
        if f2_msg_id:
            break
        else:
            await second_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue

    while True:
        try:
            third_message = await client.ask(text = "Forward the 3rd", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        media3 = third_message.document or third_message.video
        filesize3 = humanbytes(media3.file_size) if media3.file_size else ""
        f3_msg_id = await get_message_id(client, third_message)
        if f3_msg_id:
            break
        else:
            await third_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue

    while True:
        try:
            fourth_message = await client.ask(text = "Forward the 4th", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        media4 = fourth_message.document or fourth_message.video
        filesize4 = humanbytes(media4.file_size) if media4.file_size else ""
        f4_msg_id = await get_message_id(client, fourth_message)
        if f4_msg_id:
            break
        else:
            await fourth_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue

    while True:
        try:
            fifth_message = await client.ask(text = "Forward the 5th", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        media5 = fifth_message.document or fifth_message.video
        filesize5 = humanbytes(media5.file_size) if media5.file_size else ""
        f5_msg_id = await get_message_id(client, fifth_message)
        if f5_msg_id:
            break
        else:
            await fifth_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue


    string1 = f"get-{f1_msg_id * abs(client.db_channel.id)}"
    string2 = f"get-{f2_msg_id * abs(client.db_channel.id)}"
    string3 = f"get-{f3_msg_id * abs(client.db_channel.id)}"
    string4 = f"get-{f4_msg_id * abs(client.db_channel.id)}"
    string5 = f"get-{f5_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string1)
    base65_string = await encode(string2)
    base66_string = await encode(string3)
    base67_string = await encode(string4)
    base68_string = await encode(string5)
    link1 = f"https://telegram.me/{client.username}?start={base64_string}"
    link2 = f"https://telegram.me/{client.username}?start={base65_string}"
    link3 = f"https://telegram.me/{client.username}?start={base66_string}"
    link4 = f"https://telegram.me/{client.username}?start={base67_string}"
    link5 = f"https://telegram.me/{client.username}?start={base68_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("💸 Yᴏᴜ ᴄᴀɴ sʜᴀʀᴇ ᴛʜɪs ᴛᴏ ᴀɴʏ ᴄʜᴀᴛs 💸", url=f'https://telegram.me/share/url?url={link1}')]])
    await second_message.reply_text(f"<b>{shortened_filename} Tamil\n\n<a href=https://t.me/tnlinkdown/9>( How to get Telegram Direct Files ) </a>\n\n🔻 Direct Telegram Files 🔻\n\n{filesize1} : {link1}\n\n{filesize2} : {link2}\n\n{filesize3} : {link3}\n\n{filesize4} : {link4}\n\n{filesize5} : {link5}\n\n©@RolexMoviesOXO 🍃</b>", quote=True, reply_markup=None)

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

@Bot.on_message(filters.command("tutorial", CMD))
async def tutorial(_, message):
    video=(TUTORIAL_VIDEO)

    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("⊝ Close ⊝", callback_data='close')]
        ]
    )
    await message.reply_video(video=TUTORIAL_VIDEO, reply_markup=keyboard)  

import logging
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, ConversationHandler, CallbackContext
from telegram import Update
import asyncio
import aiohttp
from bot import Bot
from config import *

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define states for the conversation
CHOOSING, ADDING_FILES = range(2)

# Dictionary to store file URLs
files = {}

# Handler for the /start command
async def stat(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("Hello! How many files are you willing to add?")
    return CHOOSING

# Handler for the number of files chosen by the user
async def set_number_of_files(update: Update, context: CallbackContext) -> int:
    num_files = int(update.message.text)
    context.user_data['num_files'] = num_files
    context.user_data['current_file'] = 1
    update.message.reply_text(f"Great! Please provide URL for file 1:")
    return ADDING_FILES

# Handler for adding files and generating short links
async def add_file(update: Update, context: CallbackContext) -> int:
    file_url = update.message.text
    short_url = get_shortlink(file_url)  # Implement your own URL shortening logic
    files[context.user_data['current_file']] = short_url
    context.user_data['current_file'] += 1

    if context.user_data['current_file'] > context.user_data['num_files']:
        update.message.reply_text("Here are the shortened links:")
        for file_num, short_link in files.items():
            update.message.reply_text(f"File {file_num}: {short_link}")
        return ConversationHandler.END
    else:
        update.message.reply_text(f"Please provide URL for file {context.user_data['current_file']}:")
        return ADDING_FILES

# Function to shorten a given URL (implement your own logic here)
async def get_shortlink(link):
    url = 'https://tnshort.net/api'
    params = {'api': SHORTENER_API, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True, ssl=False) as response:
            data = await response.json()
            return data["shortenedUrl"]

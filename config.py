#(©)NovaXTG




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6584881333:AAE06ytyO50SO2AdWejrZl9c-CWuWMhm8Ok")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "25393663"))

BOT_USERNAME = os.environ.get("BOT_USERNAME", "Movie_Master_YBot") #without @
BOT_NAME = os.environ.get("BOT_NAME", "ᏢᎡθғᎬꕶꕶθᎡ")

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "46fb840e6cb4b84d582c44ebbf703251")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002105263806"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5324568283"))

#Port
PORT = os.environ.get("PORT", "8080")

#Shortener
SHORTENER_WEBSITE = os.environ.get('SHORTENER_WEBSITE', 'tnshort.net')
SHORTENER_API = os.environ.get('SHORTENER_API', '48f168b19c165cd387c5a51c97cf73e6bf18ab0b')
TUTORIAL_VIDEO = os.environ.get("TUTORIAL_VIDEO", "https://telegra.ph/file/35bfe15a705d870a47f85.mp4")
#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Yogesh:Yogesh313$@cluster0.lptftko.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Yogesh")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001981811019"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Hᴇʟʟᴏ {first}🦋 ɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀꜰᴜʟ Fɪʟᴇ ᴛᴏ ʟɪɴᴋ + ꜰɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ. sᴇɴᴅ ᴀɴʏ ғɪʟᴇ ᴛᴏ ᴍᴇ, ɪ ᴡɪʟʟ ɢɪᴠᴇ ᴅɪʀᴇᴄᴛ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ ʟɪɴᴋ. ʀᴀʀᴇ ᴍᴏᴠɪᴇ ᴘᴏsᴛ ᴏᴘᴛɪᴏɴ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ 🥂</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5324568283").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>Pʟᴇᴀsᴇ ɪᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ ❗️</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>ɴᴀᴍᴇ</b> : {filename}\n\n 💢 𝐌𝐚𝐢𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 :- https://t.me/moviemaster_yogi \n\n 🎁 𝐌𝐨𝐯𝐢𝐞 𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐆𝐫𝐨𝐮𝐩 :- https://t.me/HDmoviesparadise \n\n ©️ @мσνιє_мαѕтєя\n\n ⚠️ɴᴏᴛᴇ: ᴀꜰᴛᴇʀ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴛʜᴇ ꜰɪʟᴇꜱ, ꜱᴀᴠᴇ ᴛʜᴇ ꜰɪʟᴇ ᴛᴏ ɢᴀʟʟᴇʀʏ ᴀɴᴅ ᴄʟɪᴄᴋ ᴛʜᴇ ᴅᴇʟᴇᴛᴇ ʙᴜᴛᴛᴏɴ, ᴅᴏɴ'ᴛ ᴄʟɪᴄᴋ ʙᴇꜰᴏʀᴇ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴛʜᴇ ꜰɪʟᴇꜱ, ɪꜰ ᴜ ᴅᴏɴ'ᴛ ᴡᴀɴᴛ ᴛʜɪꜱ ꜰɪʟᴇ ᴘʟᴇᴀꜱᴇ ᴄʟɪᴄᴋ ᴅᴇʟᴇᴛᴇ ʙᴜᴛᴛᴏɴ")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b>⚠ ᴅᴏɴ'ᴛ sᴇɴᴅ ᴀ ᴍᴇssᴀɢᴇs, ɪᴛs ᴏɴʟʏ sᴜᴘᴘᴏʀᴛs ᴅᴏᴄᴜᴍᴇɴᴛ | ᴠɪᴅᴇᴏs | ᴘʜᴏᴛᴏs</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(5324568283)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

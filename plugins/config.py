import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):

    BOT_TOKEN = "5371407126:AAGZW4aUbyKo_ZWBGq7ejQB6y4a5Z8_a53Y"

    API_ID = 15682957

    API_HASH = "00b8b3714cee0ba2941091b7cc5578e7"

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1098983599").split())

    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "")

    MAX_FILE_SIZE = 4194304000

    TG_MAX_FILE_SIZE = 4194304000

    FREE_USER_MAX_FILE_SIZE = 4194304000

    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")

    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    OUO_IO_API_KEY = ""

    MAX_MESSAGE_LENGTH = 4096

    PROCESS_MAX_TIMEOUT = 0

    DEF_WATER_MARK_FILE = "op"

    DATABASE_URL = "mongodb+srv://telugumovies:telugumovies@cluster0.npql0xh.mongodb.net/?retryWrites=true&w=majority"

    SESSION_NAME = os.environ.get("SESSION_NAME", "UrlUploaderProh_bot")

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100))

    LOGGER = logging

    OWNER_ID = 1098983599

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "UrlUploaderProh_bot")

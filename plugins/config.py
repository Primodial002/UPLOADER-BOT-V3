import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):

    BOT_TOKEN = "5398983539:AAEp3HnhnzwgxvA8YMkgRXajVFjOmZgeVyc"

    API_ID = 5986296

    API_HASH = "7e38dc5d2f8302364f8051a68afae05b"
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

    SESSION_NAME = "MyFirstQueue_Bot"

    LOG_CHANNEL = -1001566282612

    LOGGER = logging

    OWNER_ID = 1098983599

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
    
    BOT_USERNAME = "MyFirstQueue_Bot"

import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6475853194:AAGee7E3blzvEnY_bUCFFq0-cWskzyXsfK8")
    
    API_ID = int(os.environ.get("API_ID", "4888076"))
    
    API_HASH = os.environ.get("API_HASH", "8b9b8214d84305d5ba8042c93575ea84")

    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://UploadLinkToFileBot:UploadLinkToFileBot@cluster0.1gybihh.mongodb.net/?retryWrites=true&w=majority")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "UploadLinkToFileBot")
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002145935116"))
    
    LOGGER = logging

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002145935116")

    OWNER_ID = int(os.environ.get("OWNER_ID", "5656422326"))
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "LuffyBot")
                                  

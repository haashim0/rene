# (c) @AbirHasan2005

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = int(os.environ.get("API_ID", "14505719"))
    API_HASH = os.environ.get("API_HASH", "620f0a2aa2cd1474a4953619b3e3643d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5945219564:AAHMjrNCDXTgfBT-HuBmxjDN_0RHOORYqbA")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", "5291606032"))
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "1354643852").split()))
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://Haashim:Haashim@mfile0.t9hxg.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001855524980"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))

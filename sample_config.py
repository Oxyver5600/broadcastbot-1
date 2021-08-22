#  !/usr/bin/env python3
#  Author   : Renjith Mangal| shabib-k

import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):
    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", ""))
    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "")
    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "")
    # List of admin user ids for special functions(
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
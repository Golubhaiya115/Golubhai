import re
import sys
import os
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID=24469836
API_HASH="af2b67f144d86a69ffaf612df13e875d"
BOT_TOKEN= os.getenv("BOT_TOKEN", "7528496902:AAHjZSzck4ZrCsAmiPN9ZJINrQQt51SFb24")
OWNER_USERNAME= os.getenv("OWNER_USERNAME", "owner_username")
OWNER_ID= os.getenv("OWNER_ID", 544633527)
WELCOME_MSG = os.getenv("WELCOME_MSG", "Welcome to the group! I'm here to assist you.")
CUSTOM_MSG = os.getenv("CUSTOM_MSG", "Lets get started!\nI am #1 bot in the world\nI can serve you unlimited entertainment\n")
BUTTON_TYPE = "list"
BUTTON_MODE = "inline"

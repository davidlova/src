from pyrogram import Client
from telethon.sync import TelegramClient
import logging
import sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 8405475
API_HASH = "2575cc32b15cc2002fc1903324217d62"
BOT_TOKEN = "6302165581:AAEkmZAWucqjnkEtNSPbZY1AFHHB1FoDbxs"
SESSION = "BQC6JkIkHLfGZpi8gnxgY_IyjkTBiKXNqRuVQyXG0bV_LRh_HFgj91EEkMU0sGlLC5T7N9NVzlfCfMG8025sqEwbJ8GoDLUV0eAegMvVFzmjNReePmgnoNwfRpeMFbMv4V26a-AZIGRUJsQr2S8VAmFoBY-zxvkv8u6Hs4a5p-P_PXyutZDPSNn-bfrrqVxpGCi8QpqQjPaCfo-xnDWExz4TWFIJ6X6mZ8s-kRCNvmrV0pGvLFojD4tqUAA54A2qI0dv04GlcPumYPiNCGQPCYQdFY4LiRHKPkjBHh0xWsRv7SN2pHrRxd1-_3o1QbZPYjUzyH_PavVAOAAAAAXTGvwYA"
FORCESUB = "sachme001"
AUTH = 108380022

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

userbot = Client("saverestricted", api_hash=API_HASH, api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)

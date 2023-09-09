from pyrogram import Client
from telethon.sync import TelegramClient
import logging
import sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 24490919
API_HASH = "d1b3b15126c47dd4cb491553ee1db910"
BOT_TOKEN = "6349275069:AAHK2HGHZMiWasUM2V3CwXOVLmRB4doZJug"
SESSION = "BQC6JkIkHIf9kfu-QdCKLfGZpi8gnxgY_IyjkTBiKXNqRuVQyXG0bV_LRh_HFgj91EEkMU0sGlLC5T7N9NVzlfCfMG8025sqEwbJ8GoDLUV0eAegMvVFzmjNReePmgnoNwfRpeMFbMv4V26a-AZIGRUJsQr2S8VAmFoBY-zxvkv8u6Hs4a5p-P_PXyutZDPSNn-bfrrqVxpGCi8QpqQjPaCfo-xnDWExz4TWFIJ6X6mZ8s-kRCNvmrV0pGvLFojD4tqUAA54A2qI0dv04GlcPumYPiNCGQPCYQdFY4LiRHKPkjBHh0xWsRv7SN2pHrRxd1-_3o1QbZPYjUzyH_PavVAOAAAAAXTGvwYA"
FORCESUB = "batchingupdate"
AUTH = 6062037731

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

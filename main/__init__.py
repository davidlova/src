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
SESSION = "BQCAQeMAEtZVTWucMbrIF9LHsTsvL4qHSirMLUmRnlA0LxN0lW-XysncHYCN9_EQBB4ntr1cr_xuyAtOS9b0os9H5PTjWMyYH-EpsO7QI_lQ_bNVf8RWGrP_cJ79gmA5IRYvyF9JppWLGVP7DxuavMC1xHRWE81-BzaNwNBpmIqDI8b2N7WwkoC-fXPXspNSakd1hlVxP1AAi9gH7ZP2uygVFJOOlzkO8mLHrRAJTZIEjU-bw3RDfKbdp9TTggtdRkPi1FH2_nhevRbHWY9BWEwmj5dWamF9kQfrxYWcmjqSrhdzihtBBEUiawtyj_5dm2W_OsFVrIonE6ALOfZB3s9wTOV8wAAAAAAGdb92AA"
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

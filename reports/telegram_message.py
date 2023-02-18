import os
import telegram
from telegram import InputMediaDocument
# from telegram.constants import MAX_MESSAGE_LENGTH

# Set up the Telegram bot API key and chat ID
bot = telegram.Bot(token='6252169122:AAFqOmh5PUSl0r1mLcPXBdF2IPjH5tZJaIU')
chat_id = -1001801058956

# Send the report file to Telegram
with open('report.html', 'rb') as report:
    media = InputMediaDocument(report, filename='report.html')
    bot.send_media_group(chat_id=chat_id, media=[media], disable_notification=True)
import os
import telebot
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get('S_TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.from_user.id, 'Стикером бью стикер!')


@bot.message_handler(content_types=['sticker'])
def return_file(message):

    bot.send_sticker(message.from_user.id, message.sticker.file_id)
    print(message)


bot.infinity_polling()
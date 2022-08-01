import os
import telebot
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

TOKEN = os.environ.get('S_TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.from_user.id, 'С тебя стикер, с меня файл')


@bot.message_handler(content_types=['sticker'])
def return_file(message):
    file_info = bot.get_file(message.sticker.file_id)
    download_path = bot.download_file(file_info.file_path)
    src = os.environ.get('STICKER_ADDRESS') + file_info.file_path
    with open(src, 'wb') as new_file:
        new_file.write(download_path)
        new_file.close()

    img_exp = ".png"

    name = os.path.splitext(src)[1]

    img = Image.open(src)
    img.load()
    img.save(name + img_exp)
    os.remove(src)

    png_file = open(name + img_exp, 'rb')
    bot.send_photo(message.from_user.id, png_file)

    png_file.close()
    os.remove(name+img_exp)


bot.infinity_polling()
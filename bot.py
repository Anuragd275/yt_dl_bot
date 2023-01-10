import telebot
import time
import os
from app import *

TOKEN = "5823709070:AAH3K8f36_ZTi-XoYzrWBb8QA9wIkb8CPbU"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start", "help"])
def welcome_message(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Hi, I can do something for you :)")
    bot.send_message(chat_id, "send /video <video link> to proceed")

@bot.message_handler(commands=["video"])
def video_dwonloader(message):
    chat_id = message.chat.id
    message_text = message.text
    splitted_message = message_text.split()
    link = splitted_message[-1]
    video_details = video_info(link)
    bot.send_message(chat_id, f"Here's what Youtube gave me \n\n{video_details}")
    file_title = title_finder(link)
    bot.send_message(chat_id, f"Sending...{file_title}")
    the_audio_file = audio_dl(link)
    audio_to_send = open(f'{file_title}.mp4', 'rb')
    bot.send_audio(chat_id, audio_to_send)

bot.infinity_polling()
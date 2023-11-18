import telebot
from app import *

TOKEN = "6977590067:AAGYgmFWZTk3RsnDricMtwRr10LEsPWSius"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start", "help"])
def welcome_message(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Hi, I can download YouTube videos for you :)")
    bot.send_message(chat_id, "Send /video <video resolution>  <video link> to download video")
    bot.send_message(chat_id, "Send /audio <video url> to download audio")

# Handeling audio requests

@bot.message_handler(commands=["audio"])
def audio_dwonloader(message):
    chat_id = message.chat.id
    message_text = message.text
    splitted_message = message_text.split()
    link = splitted_message[-1]
    video_details = video_info(link)
    file_title = title_finder(link)
    the_audio_file = audio_dl(link)
    new = replace_characters(file_title)
    audio_to_send = open(f'{new}.mp4', 'rb')
    bot.send_audio(chat_id, audio_to_send, caption=video_details)

# Handeling video requests 
@bot.message_handler(commands=["video"])
def video_downloader(message):
    chat_id = message.chat.id
    message_text = message.text
    splitted_message = message_text.split()
    link = splitted_message[-1]
    res = splitted_message[-2]
    video_details = video_info(link)
    bot.send_message(chat_id, f"Here's what Youtube gave me \n\n{video_details}")
    file_title = title_finder(link)
    new = replace_characters(file_title)
    if res == "360":
        bot.send_message(chat_id,"Downloading in 360p resolution")
        result_video_file = video_dl_360(link)
        result_video_file_to_send = open(f'{new}.mp4', 'rb')
        bot.send_video(chat_id, result_video_file_to_send)
    elif res == "720":
        bot.send_message(chat_id,"Downloading in 720p resolution")
        result_video_file = video_dl_720(link)
        result_video_file_to_send = open(f'{new}.mp4', 'rb')
        bot.send_video(chat_id, result_video_file_to_send)
    elif res == "1080":
        bot.send_message(chat_id,"Downloading in 1080p resolution")
        result_video_file = video_dl_1080(link)
        result_video_file_to_send = open(f'{new}.mp4', 'rb')
        bot.send_video(chat_id, result_video_file_to_send)
    else:
        bot.send_message("Invalid resolution selection ;_;")


# Handle other commands
@bot.message_handler(commands=["help"])
def help_message(message):
    chat_id = message.chat.id
    text = "If you are facing problem while using this bot, refer to this post for more example"
    bot.send_message(chat_id, text)

@bot.message_handler(commands=["about"])
def about_message(message):
    chat_id = message.chat.id
    text = "This project was started as a side project, then it got picked for a full fledged project by my friends, and here we are..."
    bot.send_message(chat_id, text)


bot.infinity_polling()

from pytube import YouTube
from pytube import YouTube
import os
import telebot


BOT_TOKEN = ""

bot = telebot.TeleBot(BOT_TOKEN)


from pytube import YouTube


def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")
    print(youtubeObject.title)
    return youtubeObject.title


@bot.message_handler(
    regexp=r"(?:https?://)?(?:www\.)?(?:youtube\.com(?:\S+?(?:(?:&|\?)v=|/embed/|/watch\?v=))|(?:youtu\.be/))([\w\-]{11})"
)
def download_video(message):
    file_name = Download(message.text)
    bot.reply_to(message, file_name)
    bot.send_video(chat_id=message.chat.id, video=open(f"{file_name}.mp4", "rb"))
    os.remove(f"{file_name}.mp4")
    with open("file_downloaded.txt", "a") as myfile:
        myfile.write(f"{file_name}\n")


@bot.message_handler(func=lambda message: True)
def send_link(message):
    bot.send_message(message.chat.id, "Send youtube link!")


bot.infinity_polling()

from pytube import YouTube
from pytube import YouTube
import os
import telebot


BOT_TOKEN = ""

bot = telebot.TeleBot(BOT_TOKEN)


def Download():
    yt = YouTube(str(input("Enter the URL of the video you want to download: \n>> ")))

    print("Select download format:")
    print("1: Video file with audio (.mp4)")
    print("2: Audio only (.mp3)")

    media_type = input(">> ")

    if media_type == "1":
        video = yt.streams.first()

    elif media_type == "2":
        video = yt.streams.filter(only_audio=True).first()

    else:
        print("Invalid selection.")

    print("Enter the destination (leave blank for current directory)")
    destination = str(input(">> ")) or "."

    out_file = video.download(output_path=destination)

    if media_type == "1":
        new_file = "new" + ".mp4"
        os.rename(out_file, new_file)

    elif media_type == "2":
        new_file = "new" + ".mp3"
        os.rename(out_file, new_file)


Download()

# @bot.message_handler(commands=["start"])
# def greetings(message):
#     bot.send_message(
#         message.chat.id,
#         f"Salam {message.from_user.first_name}, istediyiniz videonu yükləmək ücün link atın.",
#     )


# @bot.message_handler(
#     regexp=r"(?:https?://)?(?:www\.)?(?:youtube\.com(?:\S+?(?:(?:&|\?)v=|/embed/|/watch\?v=))|(?:youtu\.be/))([\w\-]{11})"
# )
# def download_video(message):
#     bot.send_animation(
#         chat_id=message.chat.id,
#         animation="CAACAgIAAxkBAAJZ82Xpl6dZmSIS86Tp0xJ9M0ubChr-AAJJCQACfAUHG46I2MbTgE4MNAQ",
#     )
#     file_name = Download(message.text)
#     bot.reply_to(message, file_name)
#     bot.send_video(chat_id=message.chat.id, video=open(f"{file_name}.mp4", "rb"))
#     os.remove(f"{file_name}.mp4")
#     with open("file_downloaded.txt", "a") as myfile:
#         myfile.write(f"{file_name}\n")


# @bot.message_handler(func=lambda message: True)
# def send_link(message):
#     bot.send_message(message.chat.id, "Youtube link at!")


# bot.infinity_polling()

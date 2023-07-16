import telebot
from pytube import YouTube

# Telegram Bot API token
TOKEN = '6155572608:AAHvgfPspZODyTZTDmO4QuIf0iSaI3p_Yn0'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to the YouTube Video Downloader Bot!")


@bot.message_handler(func=lambda message: True)
def download_video(message):
    url = message.text.strip()

    try:
        # Download YouTube video
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download()

        # Sending the video file
        with open(video.default_filename, 'rb') as video_file:
            bot.send_video(message.chat.id, video_file)

        bot.reply_to(message, "Video downloaded and sent successfully!")
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {str(e)}")


bot.polling()

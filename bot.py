import os
import telebot
import threading
from flask import Flask
from deep_translator import GoogleTranslator

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route("/")
def home():
    return "bot is running"


def run():
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", 10000))
    )


@bot.message_handler(func=lambda message: True)
def translate(message):
    try:
        text = message.text

        result = GoogleTranslator(
            source="auto",
            target="vi"
        ).translate(text)

        bot.reply_to(message, result)

    except:
        bot.reply_to(message, "번역 오류")


threading.Thread(target=run).start()

bot.infinity_polling()

import os
import telebot
from deep_translator import GoogleTranslator

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

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

bot.infinity_polling()
from flask import Flask
from threading import Thread
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

def run():
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )

Thread(target=run).start()

bot.infinity_polling()

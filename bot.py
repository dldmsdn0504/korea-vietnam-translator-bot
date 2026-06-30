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
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return "bot is running"

def run():
    app.run(host="0.0.0.0", port=10000)

threading.Thread(target=run).start()

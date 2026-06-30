import os
import threading
import telebot
from flask import Flask
from deep_translator import GoogleTranslator


app = Flask(__name__)


@app.route("/")
def home():
    return "OK"


def flask_run():
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )


TOKEN = os.environ.get("TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message: True)
def translate(message):
    bot.reply_to(message, "테스트 성공")

threading.Thread(
    target=flask_run,
    daemon=True
).start()


print("BOT START")

bot.infinity_polling()


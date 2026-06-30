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
    try:
        if "가" <= message.text <= "힣":
    target = "vi"
else:
    target = "ko"

result = GoogleTranslator(
    source="auto",
    target=target
).translate(message.text)

        bot.reply_to(message, result)

    except Exception as e:
        bot.reply_to(message, "번역 오류")


threading.Thread(
    target=flask_run,
    daemon=True
).start()


print("BOT START")

bot.infinity_polling()


import os
import telebot
from flask import Flask
from deep_translator import GoogleTranslator
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return "OK"

TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)

def run_bot():
    print("BOT START")
    bot.infinity_polling(skip_pending=True, timeout=60, long_polling_timeout=60)

@bot.message_handler(func=lambda message: True)
def translate(message):
    try:
        text = message.text

        if any("가" <= ch <= "힣" for ch in text):
            result = GoogleTranslator(source="auto", target="vi").translate(text)
        else:
            result = GoogleTranslator(source="auto", target="ko").translate(text)

        bot.reply_to(message, result)

    except Exception as e:
        print(e)
        bot.reply_to(message, "번역 오류")

threading.Thread(target=run_bot).start()

app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
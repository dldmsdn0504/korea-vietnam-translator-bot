import os
import telebot
from flask import Flask
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route("/")
def home():
    return "OK"

def run_flask():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

TOKEN = os.environ.get("TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def translate(message):
    try:
        text = message.text

        # 한국어 → 베트남어
        if any("가" <= ch <= "힣" for ch in text):
            target = "vi"
        else:
            target = "ko"

        result = GoogleTranslator(
            source="auto",
            target=target
        ).translate(text)

        bot.reply_to(message, result)

    except:
        bot.reply_to(message, "번역 오류")

import threading

threading.Thread(target=run_flask, daemon=True).start()

print("BOT START")

bot.infinity_polling()
import os
import telebot
from flask import Flask
from deep_translator import GoogleTranslator
import threading

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

        if not text:
            return

        if any("가" <= ch <= "힣" for ch in text):
            result = GoogleTranslator(source="auto", target="vi").translate(text)
        else:
            result = GoogleTranslator(source="auto", target="ko").translate(text)

        bot.reply_to(message, result)

    except Exception as e:
        print(e)
        bot.reply_to(message, "번역 오류")

threading.Thread(target=run_flask, daemon=True).start()

print("BOT START")

bot.infinity_polling()
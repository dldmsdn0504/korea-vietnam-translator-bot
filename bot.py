import os
import telebot
from flask import Flask
from googletrans import Translator
import threading

# Flask (Render 유지용)
app = Flask(__name__)

@app.route("/")
def home():
    return "OK"

def run_flask():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

# Telegram bot token
TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)

# 번역기
translator = Translator()

# 메시지 처리
@bot.message_handler(func=lambda message: True)
def translate(message):
    try:
        text = message.text

        if not text:
            bot.reply_to(message, "내용이 없습니다")
            return

        # 한국어 → 베트남어
        if any("가" <= ch <= "힣" for ch in text):
            result = translator.translate(text, dest="vi").text
        else:
            result = translator.translate(text, dest="ko").text

        bot.reply_to(message, result)

    except Exception as e:
        print(e)
        bot.reply_to(message, "번역 오류")

# Flask 실행
threading.Thread(target=run_flask, daemon=True).start()

print("BOT START")

# Bot 실행
bot.infinity_polling()
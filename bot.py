import telebot
from deep_translator import GoogleTranslator

TOKEN = "여기에_새_토큰_입력"

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

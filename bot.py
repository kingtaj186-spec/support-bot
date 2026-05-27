import telebot

8639142062:AAH64905mBNa5ATD_DVqr9kDcXrL-3zTJ9w = "توکن ربات"

OWNER_ID = 7909484213

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):

    text = """
سلام!
در زمان هایی که امیرحسین نیست میتونید با استفاده از من پیام خودرا بفرستید،مستقیما به گوشی ایشان ارسال میکنم

اتحادیه: BIG ZED
"""

    bot.send_message(message.chat.id, text)

    try:
        bot.send_message(
            OWNER_ID,
            f"کاربر جدید:\nآیدی: @{message.from_user.username}\nآیدی عددی: {message.chat.id}"
        )
    except:
        pass


@bot.message_handler(func=lambda m: True)
def forward_message(message):

    user = message.from_user.username

    text = f"""
پیام جدید

از: @{user}

متن:
{message.text}
"""

    bot.send_message(OWNER_ID, text)


bot.infinity_polling()

import telebot
from telebot import types

bot = telebot.TeleBot('8166655284:AAE-FiUhNO837oYZL037Bt7JPl-tE4LNwEc')
@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)

import telebot
from telebot import types

bot = telebot.TeleBot('8166655284:AAE-FiUhNO837oYZL037Bt7JPl-tE4LNwEc')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Начать пользоватся")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Нажми кнопку: Начать пользоватся", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Начать пользоватся':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Заказать бит')
        btn2 = types.KeyboardButton('Связь с админом')
        btn3 = types.KeyboardButton('Правила')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'Нажимай на кнопки!', reply_markup=markup) #ответ бота


    elif message.text == 'Заказать бит':
        bot.send_message(message.from_user.id, 'Чтобы заказать бит пиши [ему](https://t.me/sdscoop)', parse_mode='Markdown')

    elif message.text == 'Связь с админом':
        bot.send_message(message.from_user.id, 'Наш [админ](https://t.me/sdscoop)', parse_mode='Markdown')

    elif message.text == 'Правила':
        bot.send_message(message.from_user.id, 'Скоро будут', parse_mode='Markdown')


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть

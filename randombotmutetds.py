import telebot
from telebot import formatting
import random
from telebot import types

click = '👆 Рандом'
about_me = '🔒 Информация'
clicker10 = '👆 Число до 10'
clicker100 = '👆 Число до 100'
clicker1000 = '👆 Число до 1000'
back = '↪ Назад'

bot = telebot.TeleBot('7033556396:AAEli2iqNBjrPdH8PMVo70Ly5EUORJhdpq0', parse_mode='HTML')

@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем две кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        clickbut=types.KeyboardButton(click)
        about_me_but=types.KeyboardButton(about_me)
        reset_but=types.KeyboardButton('/reset')
        markup.add(clickbut)
        markup.add(about_me_but)
        markup.add(reset_but)
        bot.send_message(m.chat.id, 'сгенерируй рандомное число!',  reply_markup=markup)
# Получение сообщений от юзера
@bot.message_handler(commands=["reset"])
def start(m, res=False):
        # Добавляем две кнопки
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            clickbut=types.KeyboardButton(click)
            about_me_but=types.KeyboardButton(about_me)
            reset_but=types.KeyboardButton('/reset')
            markup.add(clickbut)
            markup.add(about_me_but)
            markup.add(reset_but)
            bot.send_message(m.chat.id, 'Перезагрузка!',  reply_markup=markup)
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == back :
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            clickbut=types.KeyboardButton(click)
            about_me_but=types.KeyboardButton(about_me)
            reset_but=types.KeyboardButton('/reset')
            markup.add(clickbut)
            markup.add(about_me_but)
            markup.add(reset_but)
            bot.send_message(message.chat.id, 'Вы вернулись назад!',  reply_markup=markup)
    elif message.text.strip() == click :
    # Если юзер прислал 1, выдаем ему случайный факт
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            clicker10_but=types.KeyboardButton(clicker10)
            clicker100_but=types.KeyboardButton(clicker100)
            clicker1000_but=types.KeyboardButton(clicker1000)
            backbut=types.KeyboardButton(back)
            markup.add(clicker10_but)
            markup.add(clicker100_but)
            markup.add(clicker1000_but)
            markup.add(backbut)
            bot.send_message(message.chat.id, 'Выбери',  reply_markup=markup)
    elif message.text.strip() == about_me :
            mess_about_me = "👋 Привет! ✨ Это простой выбор чисел. Создал: @realmutetds"
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Мой сайт", url='https://mutetds.space/')
            markup.add(button1)
            bot.send_message(message.chat.id, mess_about_me.format(message.from_user), reply_markup=markup)
    elif message.text.strip() == clicker10 :
            answer10 = str(random.randrange(1, 10))
            bot.send_message(message.chat.id, answer10)
    elif message.text.strip() == clicker100 :
            answer100 = str(random.randrange(1, 100))
            bot.send_message(message.chat.id, answer100)
    elif message.text.strip() == clicker1000 :
            answer1000 = str(random.randrange(1, 1000))
            bot.send_message(message.chat.id, answer1000)
# Запускаем бота
bot.polling(none_stop=True, interval=0)
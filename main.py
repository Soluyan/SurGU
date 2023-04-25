import sqlite3
import telebot
from telebot import types

bot = telebot.TeleBot('6229843041:AAH4pl13ZxJlsKUn-pSSw9xtN9GPYC1GIUM')

name_new=None


@bot.message_handler(commands = ['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()

    key_new = types.InlineKeyboardButton(text='Добавить',callback_data='new')
    keyboard.add(key_new)

    key_get = types.InlineKeyboardButton(text='Вывести',callback_data='get')
    keyboard.add(key_get)

    key_get_all = types.InlineKeyboardButton(text='Вывести всю информацию', callback_data='all')
    keyboard.add(key_get_all)

    bot.send_message(message.from_user.id,"Привет, Выберите действие",reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call:True)


def db_data(call):
    if call.data == "new":
        msg = bot.send_message(call.message.chat.id, "Введите Имя")
        bot.register_next_step_handler(msg, db_name_new)

    if call.data == "get":
        conn = sqlite3.connect('base.db', check_same_thread=False)
        cur = conn.cursor()
        cur.execute('Select SUM(Value),Name FROM Dolgi Group By Name')
        get_new = cur.fetchall()

        info = ''
        for el in get_new:
            info += f'Имя: {el[1]}, Долг: {el[0]}\n'

        cur.close()
        conn.close()

        bot.send_message(call.message.chat.id, info)

    if call.data == "all":
        conn = sqlite3.connect('base.db', check_same_thread=False)
        cur = conn.cursor()
        cur.execute('Select Name,Value,Date from Dolgi')
        get_new = cur.fetchall()

        info = ''
        for el in get_new:
            info += f'Имя: {el[0]}, Долг: {el[1]}, Дата: {el[2]}\n'

        cur.close()
        conn.close()

        bot.send_message(call.message.chat.id, info)

@bot.message_handler(func=lambda message: True, content_types=['text'])

def db_name_new(message):
    global name_new
    name_new = message.text.strip()
    bot.send_message(message.chat.id, "Введите Cумму")
    bot.register_next_step_handler(message, db_value_new)
def db_value_new(message):
    value_new = message.text.strip()

    conn = sqlite3.connect('base.db', check_same_thread=False)
    cur = conn.cursor()
    cur.execute(f'INSERT INTO Dolgi (Name, Value) VALUES ("{name_new}", "{value_new}")')
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, "Запись создана")



bot.polling(none_stop=True, interval=0)


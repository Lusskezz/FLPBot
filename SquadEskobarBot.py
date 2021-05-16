# -*- coding: utf-8 -*-

import telebot
from telebot import types

ADMIN_ID = 1681752351 # * Manager id
DEVELOPER_ID = 498095526 # * Lusskezz id
BOT_TOKEN = '1521194402:AAET36-5pO0xWGDAtFGTtAIWc9IjLt_Nt4o' # * Ключ для доступа к боту @SquadEskobarBot

bot = telebot.TeleBot(BOT_TOKEN)

username = ''
ages = ''
verticles = ''
his_PP = ''


# ! Функция отправки заявки администратору (ADMIN_ID - числовой tg-айди пользователя)
def send_questionary(message):
    bot.send_message(DEVELOPER_ID, f'Имя пользователя: @{username}\nЛет в сфере арбитража: {ages}\nНа каких вертикалях работает: {verticles}\nС какими ПП приходилось работать: {his_PP}')


# ! Скрипт приветствия
@bot.message_handler(commands=['start'])
def start_message(message):

    # * Генерация клавиатуры
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('✅ Пройти анкетирование')

    # * Выводим приветствия бота
    bot.send_message(message.chat.id, 'Заполни небольшую анкету, что бы мы решить - добавлять тебя к нам или нет.', parse_mode="Markdown", reply_markup = keyboard)
    


# ! Cлушатель кнопки
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text.lower() == '✅ пройти анкетирование':

        # * Запускаем тестирование
        global username
        username = message.from_user.username
        bot.send_message(message.chat.id, 'Сколько лет в сфере арбитража?', parse_mode="Markdown")
        bot.register_next_step_handler(message, get_ages)

    # TODO: Функции бана (реализуется в будущем)
    # elif message.text.lower() == 'ban':
    #     bot.send_message(message.chat.id, 'Хозяин, дайте мне его *числовой* айди, я его захуярю сучару такую ебаную нахуй!!11!1!1!!11!!1', parse_mode="Markdown")
    #     bot.register_next_step_handler(message, ban_user)

# ! Функции тестирования
def get_ages(message):
    global ages
    ages = message.text
    bot.send_message(message.chat.id, 'На каких вертикалях работаешь?', parse_mode="Markdown")
    bot.register_next_step_handler(message, get_verticles)
def get_verticles(message):
    global verticles
    verticles = message.text
    bot.send_message(message.chat.id, 'С какими ПП приходилось работать?', parse_mode="Markdown")
    bot.register_next_step_handler(message, get_his_PP)
def get_his_PP(message):
    global his_PP
    his_PP = message.text
    bot.send_message(message.chat.id, 'Спасибо за анкету!\nЕсли ты нам подходишь, то с тобой скоро свяжутся!', parse_mode="Markdown")
    send_questionary(message)

# TODO: Функции бана (реализуется в будущем)
# def ban_user(message):
#         global username
#         global user_id
#     bot.kick_chat_member()


bot.polling(none_stop=True, timeout=123)
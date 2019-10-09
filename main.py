# -*- coding: utf-8 -*-

import telebot
import config
import datetime


bot = telebot.TeleBot(config.api_key)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет, ты написал мне /start')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text == 'Время':
        bot.send_message(message.chat.id, datetime.now() )

try:
    bot.polling(none_stop=True, interval=0)
except Exception:
    pass
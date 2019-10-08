# -*- coding: utf-8 -*-

import telebot
import api_key

token=api_key.apikey
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет, ты написал мне /start')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')

try:
    bot.polling(none_stop=True, interval=0)
except Exception:
    pass
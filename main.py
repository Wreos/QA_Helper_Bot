import telebot

bot = telebot.TeleBot('726216745:AAFW4QEbfgACybljnePahzixRCfu00eknpg')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет, ты написал мне /start')

bot.polling()
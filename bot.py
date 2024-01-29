import json
import telegram
import telebot

API_KEY = '5002084399:AAFfs_igtCahn5xj0mQImIcc_fV1QsE-uE8'
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message, "Hola")

@bot.message_handler(commands=['yo'])
def buenas(message):
    bot.send_message(message.chat.id, "Buenas tardes")
bot.polling( )
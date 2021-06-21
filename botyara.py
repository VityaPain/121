from telebot import types
import telebot
bot = telebot.TeleBot('1845531182:AAEfio3OuQQHBPCq8hgdRmdeDbm54mY2p2w')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')


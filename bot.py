import telebot
from telebot import types
import config
import random
from func import solution
from func import joke


bot = telebot.TeleBot(config.TOKEN)

# приветствие
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    # клавиатура(снизу)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Делать/Не делать")
    item2 = types.KeyboardButton("Агрессия")
    item3 = types.KeyboardButton("Анекдот")

    markup.add(item1,item2,item3)

    bot.reply_to(message, f'Ну привет кожаный мешок, {message.from_user.first_name}',reply_markup=markup)


# работа с клавой
@bot.message_handler(content_types=['text'])
def chat(message):
    if message.chat.type == 'private':
        if message.text == 'Делать/Не делать':
            bot.send_message(message.chat.id, str(solution()))
        elif message.text == 'Агрессия':
            bot.send_message(message.chat.id, 'Твой рот ебал')
        elif message.text == 'Анекдот':
            bot.send_message(message.chat.id, str(joke()))
        else:
            bot.send_message(message.chat.id, 'Чо ты высрал???')



# запуск
bot.polling(none_stop=True)
#1922448950:AAEueQO_WmyT1wYrHbyaNV-FmeSirZ6zYy0

import telebot
import random
from telebot import types

token='1922448950:AAEueQO_WmyT1wYrHbyaNV-FmeSirZ6zYy0'
bot = telebot.TeleBot(token)
dict = {1: 'Кони одинаково дохнут и от работы и от перекура. В общем, совершенно не приспособленное животное, ни к работе, ни к отдыху',
     2: 'Объявление. Цирк примет на работу еще 10 воздушных гимнастов',
     3: 'В древности гонца вешали, если он приносил голосовое сообщение',
     4: 'Сидя на двух диетах похудеешь быстрее. И голодать не будешь!',
     5: 'Путь к сердцу мужчины лежит через просто оставьте его в покое'}


def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    drink_btn = types.InlineKeyboardButton(text="Хочу пить", callback_data='1')
    eat_btn = types.InlineKeyboardButton(text="Хочу есть", callback_data='2')
    progul_btn = types.InlineKeyboardButton(text="Хочу гулять", callback_data='3')
    sleep_btn = types.InlineKeyboardButton(text="Хочу спать", callback_data='4')
    smile_btn = types.InlineKeyboardButton(text="Хочу шутку", callback_data='5')
    keyboard.add(drink_btn)
    keyboard.add(eat_btn)
    keyboard.add(progul_btn)
    keyboard.add(sleep_btn)
    keyboard.add(smile_btn)
    return keyboard

@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard=create_keyboard()
    bot.send_message(
        message.chat.id,
        "Добрый день! Выберите, что Вы хотите",
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    keyboard = create_keyboard()
    if call.message:
        if call.data=="1":
            img = open('9-17.jpg','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Картинка воды",
                reply_markup=keyboard)
            img.close()
        if call.data == "2":
            img = open('darzoves2.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Картинка еда",
                reply_markup=keyboard)
            img.close()
        if call.data == '3':
            img = open('progul.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="А давай пойдем погуляем в парк. Там сейчас очень хорошо.",
                reply_markup=keyboard)
            img.close()
        if call.data == '4':
            img = open('sleep.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Ну если хочется то конечно нужно. Сладких снов и спокойной ночи.",
                reply_markup=keyboard)
            img.close()
        if call.data == '5':
            keys = list(dict.values())
            z = keys[random.randint(0,4)]
            img = open('smile.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption=z,
                reply_markup=keyboard)
            img.close()

if __name__=="__main__":
    bot.polling(none_stop=True)
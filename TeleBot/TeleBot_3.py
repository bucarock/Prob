#5319917471:AAH4pevNsobgVitg3rJkDpl2r9DbT23jrak

import telebot
import random
from telebot import types
from datetime import datetime
vrem = datetime.now()
c = vrem.hour
d = vrem.minute


token='5319917471:AAH4pevNsobgVitg3rJkDpl2r9DbT23jrak'
bot = telebot.TeleBot(token)
dict = {1: 'Кони одинаково дохнут и от работы и от перекура. В общем, совершенно не приспособленное животное, ни к работе, ни к отдыху',
     2: 'Объявление. Цирк примет на работу еще 10 воздушных гимнастов',
     3: 'В древности гонца вешали, если он приносил голосовое сообщение',
     4: 'Сидя на двух диетах похудеешь быстрее. И голодать не будешь!',
     5: 'Путь к сердцу мужчины лежит через просто оставьте его в покое'}


def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    sonya_btn = types.InlineKeyboardButton(text="Я проспала?", callback_data='1')
    eat_btn = types.InlineKeyboardButton(text="Хочу есть", callback_data='2')
    progul_btn = types.InlineKeyboardButton(text="Хочу гулять", callback_data='3')
    sleep_btn = types.InlineKeyboardButton(text="Хочу спать", callback_data='4')
    smile_btn = types.InlineKeyboardButton(text="Хочу шутку", callback_data='5')
    keyboard.add(sonya_btn)
    keyboard.add(eat_btn)
    keyboard.add(progul_btn)
    keyboard.add(sleep_btn)
    keyboard.add(smile_btn)
    return keyboard

@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard = create_keyboard()
    img = open('sonya.jpg','rb')
    bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption="А давай пойдем погуляем в парк. Там сейчас очень хорошо.")
    bot.send_message(
        message.chat.id,
        "Приветики! Я твой Котёнок, и я буду тебе помагать",
        reply_markup=keyboard)
    img.close()


@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    keyboard = create_keyboard()
    if call.message:
        if call.data=="1":
            img = open('sonya.jpg','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Картинка еда",
                reply_markup=keyboard)
            img.close()

        #здесь добавить текст нормальный. чтобы можно было вставить время с,d. или IF и прочее. в этот же ответ.

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
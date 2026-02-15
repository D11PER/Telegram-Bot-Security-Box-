import random
import telebot
from telebot import types
bot = telebot.TeleBot("8062836171:AAEktoWzS2es66Dz7KXYt4swFb3r60n0AbQ")

list_items = ['a','b','c','d','e','f',
        'z','g','v','1','2','3',
        '8','9','6','7','@','#',
        '-','%','$',"!"     
        ] 



@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Hi lets creat a password")
    markup.add(btn)
    bot.send_message(message.chat.id, 'Hi lets creat a password', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_massages(massage):

    if massage.text == 'Hi lets creat a password':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Telegram Password")
        btn2 = types.KeyboardButton("Gmail Password")
        
      
        markup.add(btn1, btn2)
        bot.send_message(massage.from_user.id, 'Ok lets make it' , reply_markup= markup)

    elif massage.text == "Telegram Password":
        take_items = random.randint(7,12)
        pass_word = random.choices(list_items,k=take_items)
        bot.send_message(massage.chat.id, f"Your Telegram password: {''.join(pass_word)}")

    elif massage.text == "Gmail Password":
        take_items = random.randint(6,10)
        pass_word = random.choices(list_items, k=take_items)
        bot.send_message(massage.chat.id, f"Your Gmail password: {''.join(pass_word)}") 
bot.polling(none_stop=True)
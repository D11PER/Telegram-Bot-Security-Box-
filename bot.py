import random
import telebot
from telebot import types
bot = telebot.TeleBot("--Token--")

## random list:
list_items = ['a','b','c','d','e','f',
        'z','g','v','1','2','3',
        '8','9','6','7','@','#',
        '-','%','$',"!"     
        ] 


## function start
@bot.message_handler(commands=['start'])
def start(messege):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("OK")
    markup.add(btn)
    bot.send_message(messege.chat.id, 'Hi lets creat a password', reply_markup=markup)

## function lenght
@bot.message_handler(commands=['length'])
def choose_length(messege):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn7 = types.KeyboardButton("7")
    btn8 = types.KeyboardButton("8")
    btn9 = types.KeyboardButton("9")
    btn10 = types.KeyboardButton("10")
    markup.add(btn7, btn8, btn9, btn10)
    bot.send_message(messege.chat.id, 'Choose a password length:', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_massages(massage):

 ## Added new btn    
    if massage.text == 'lenght':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("7")
        btn2 = types.KeyboardButton("8")
        btn3 = types.KeyboardButton("9")
        btn4 = types.KeyboardButton("10")

        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(massage.from_user.id, 'Your lenght: ' , reply_markup= markup)

## Choose Telegram or Gmail password
    if massage.text == 'OK':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Telegram Password")
        btn2 = types.KeyboardButton("Gmail Password")

        markup.add(btn1, btn2)
        bot.send_message(massage.from_user.id, 'Ok lets make it' , reply_markup= markup)   


    if massage.text == 'Telegram Password' or massage.text == 'Gmail Password':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn7 = types.KeyboardButton("7")
        btn8 = types.KeyboardButton("8")
        btn9 = types.KeyboardButton("9")
        btn10 = types.KeyboardButton("10")

        markup.add(btn7, btn8, btn9, btn10)
        bot.send_message(massage.from_user.id, 'Ok lets make it' , reply_markup= markup)  


## Telegarm and Gamil Password: choice 7 , 8 , 9 , 10 (Logic structure )
######################################################################################
    if massage.text == '7': ## if btn7 = 7
     pass_word = random.choices(list_items, k=7)   
     bot.send_message(massage.chat.id, f"Your  password: {''.join(pass_word)}") 

    if massage.text == '8':  ## if btn8 = 8
     pass_word = random.choices(list_items, k=8)   
     bot.send_message(massage.chat.id, f"Your  password: {''.join(pass_word)}") 

    if massage.text == '9':  ## if btn9 = 9
     pass_word = random.choices(list_items, k=9)   
     bot.send_message(massage.chat.id, f"Your  password: {''.join(pass_word)}") 

    if massage.text == '10':  ## if btn10 = 10
     pass_word = random.choices(list_items, k=10)   
     bot.send_message(massage.chat.id, f"Your  password: {''.join(pass_word)}") 

bot.polling(none_stop=True)

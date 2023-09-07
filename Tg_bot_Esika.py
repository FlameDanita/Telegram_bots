import time, threading, schedule
import telebot #pip install pyTelegramBotAPI
import API
import emoji

chat_ids = {"Danita" : 692791213,
            "FlameDarya" : 539280636,
            "Fobos" : 809542339} 
sticker_ids = {"Хитрая_Миён" : "CAACAgIAAxkBAAEFFjBisMOr40zNs3hZ57qW8ySateZbuwAC0RUAAhl7sUiGNg3U3z0OIygE",
               "Привет_Ариша" : "CAACAgIAAxkBAAEFFjJisMSiGLk0SwZGM6C4QE_LSMVk_wACYSQAAp7OCwABKLgYIbi2x0ooBA"}

def start_bot():
    token = API.get_tg_TOKEN()
    bot = telebot.TeleBot(token, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
    
    bot.send_message(chat_ids['Danita'], emoji.emojize('Расчет завершен, дорогой друг :smirk::heartbeat:', language='alias'))
    bot.send_sticker(chat_ids['Danita'], sticker_ids['Хитрая_Миён'])

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "Привет, добро пожаловать!)\n" +
                            "Набери /help и узнаешь доступные команды <3")

    @bot.message_handler(func=lambda m: True)
    def echo_all(message):
        bot.reply_to(message, "Не знаю таких команд, чел :/")

    bot.infinity_polling()

def calculate_complite_bot():
    token = API.get_tg_TOKEN()
    bot = telebot.TeleBot(token, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
    
    bot.send_message(chat_ids['Danita'], emoji.emojize('Расчет завершен, дорогой друг :smirk::heartbeat:', language='alias'))
    bot.send_sticker(chat_ids['Danita'], sticker_ids['Хитрая_Миён'])

    @bot.message_handler(commands=['off'])
    def stop_command(message):
        bot.reply_to(message, 'Выключаюсь...')
        bot.stop_polling()
    
    @bot.message_handler(func=lambda m: True)
    def echo_all(message):
        bot.reply_to(message, "Не знаю таких команд, чел :/")

    bot.infinity_polling()

def fobos_pc():
    flag = True
    token = API.get_tg_TOKEN()
    bot = telebot.TeleBot(token, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
    bot.send_message(chat_ids['Danita'], emoji.emojize('Эсика активированна, приветствую, дорогой друг :smirk::heartbeat:', language='alias'))
    bot.send_sticker(chat_ids['Danita'], sticker_ids['Хитрая_Миён'])
    bot.send_message(chat_ids['Danita'], emoji.emojize('Fobos PC complited :white_check_mark:', language='alias'))
    bot.send_message(chat_ids['Fobos'], emoji.emojize('Fobos PC complited :white_check_mark:', language='alias'))

    @bot.message_handler(commands=['off'])
    def stop_command(message):
        bot.reply_to(message, 'Выключаюсь...')
        flag = False
        time.sleep(1)
        bot.stop_polling()

    @bot.message_handler(func=lambda m: True)
    def echo_all(message):
        bot.reply_to(message, "Не знаю таких команд :/")

def fobos_laptop():
    flag = True
    token = API.get_tg_TOKEN()
    bot = telebot.TeleBot(token, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
    bot.send_message(chat_ids['Danita'], emoji.emojize('Эсика активированна, приветствую, дорогой друг :smirk::heartbeat:', language='alias'))
    bot.send_sticker(chat_ids['Danita'], sticker_ids['Хитрая_Миён'])
    bot.send_message(chat_ids['Danita'], emoji.emojize('Fobos laptop complited :white_check_mark:', language='alias'))
    bot.send_message(chat_ids['Fobos'], emoji.emojize('Fobos laptop complited :white_check_mark:', language='alias'))

    @bot.message_handler(commands=['off'])
    def stop_command(message):
        bot.reply_to(message, 'Выключаюсь...')
        flag = False
        time.sleep(1)
        bot.stop_polling()

    @bot.message_handler(func=lambda m: True)
    def echo_all(message):
        bot.reply_to(message, "Не знаю таких команд :/")

    if flag:
        bot.infinity_polling(interval=1)
    

 
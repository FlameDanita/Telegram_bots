import telebot #pip install pyTelegramBotAPI
import API
import time, threading, schedule
def start_bot():
    token = API.get_tg_TOKEN()
    bot = telebot.TeleBot(token, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "Привет, добро пожаловать!)\n" +
                            "Набери /help и узнаешь доступные команды <3")

    @bot.message_handler(func=lambda m: True)
    def echo_all(message):
        bot.reply_to(message, "Не знаю таких команд, чел :/")

    bot.infinity_polling()

def stop_bot():
    token = API.get_tg_TOKEN()
    bot = telebot.TeleBot(token, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
    bot.stop_polling()
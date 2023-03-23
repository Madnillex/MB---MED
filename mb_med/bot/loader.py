from telebot import TeleBot
from config import TOKEN
from telebot import custom_filters

my_bot = TeleBot(TOKEN)


my_bot.add_custom_filter(custom_filters.ChatFilter())


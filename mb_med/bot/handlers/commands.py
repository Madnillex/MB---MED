from telebot.types import Message

from ..loader import my_bot
from ..keyboards.inline import get_admin_btns
from config import ADMINS
from ..models import TelegramUsers


@my_bot.message_handler(commands=['start', 'help'], chat_id=ADMINS)
def reaction_to_commands(message: Message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    if message.text == '/start':
        try:
            my_bot.send_message(chat_id, f"Salom, {first_name} ADMINISTRATOR!",
                                reply_markup=get_admin_btns())
        except Exception as e:
            print(e.__class__)


@my_bot.message_handler(commands=['start', 'help'])
def reaction_to_commands(message: Message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    if message.text == '/start':
        try:
            user = TelegramUsers.objects.create(telegram_id=chat_id)
            user.save()
            my_bot.send_message(chat_id, f"Salom, {first_name}!")
        except Exception as e:
            print(e.__class__)



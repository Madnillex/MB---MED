from telebot.types import CallbackQuery, Message
import time

from ..loader import my_bot
from ..models import TelegramUsers
from ..keyboards.inline import get_admin_btns


@my_bot.callback_query_handler(func=lambda call: call.data == 'count_users')
def get_count_of_users(call: CallbackQuery):
    chat_id = call.message.chat.id
    users = TelegramUsers.objects.all()
    my_bot.send_message(chat_id, f'Foydalanuvchilar soni: {len(users)}',
                        reply_markup=get_admin_btns())


@my_bot.callback_query_handler(func=lambda call: call.data == 'send_users')
def send_message_to_users(call: CallbackQuery):
    chat_id = call.message.chat.id
    msg = my_bot.send_message(chat_id, 'Habarni kiriting: ')
    my_bot.register_next_step_handler(msg, send_message)

def send_message(message: Message):
    users = TelegramUsers.objects.all()
    chat_id = message.chat.id
    text = message.text
    count = 0
    for user in users:
        try:
            my_bot.send_message(chat_id=user.telegram_id, text=text)
            time.sleep(0.03)
            count += 1
        except Exception as e:
            print(e)
    my_bot.send_message(chat_id, f"Jo'natma amalga oshdi: {count}/{len(users)} qismiga jo'natildi!",
                        reply_markup=get_admin_btns())



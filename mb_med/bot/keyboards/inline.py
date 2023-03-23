from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_admin_btns():
    markup = InlineKeyboardMarkup(row_width=1)
    btn_1 = InlineKeyboardButton('Send message to users', callback_data='send_users')
    btn_2 = InlineKeyboardButton('Count of users', callback_data='count_users')
    markup.add(btn_2, btn_1)
    return markup



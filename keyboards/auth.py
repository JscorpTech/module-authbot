from telebot.types import KeyboardButton, ReplyKeyboardMarkup
from .. import messages

send_phone = ReplyKeyboardMarkup(resize_keyboard=True)
send_phone.add(KeyboardButton(text=messages.send_phone, request_contact=True))

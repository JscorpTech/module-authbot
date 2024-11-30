from telebot import TeleBot
from config.env import env


bot = TeleBot(env.str("BOT_TOKEN"))

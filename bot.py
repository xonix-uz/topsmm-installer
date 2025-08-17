import telebot
import json
from admin import handle_admin_commands
from order import handle_order
from reseller import handle_reseller

with open("config.json") as f:
    config = json.load(f)

bot = telebot.TeleBot(config["bot_token"])

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Xush kelibsiz! Buyurtma berish uchun /order, balans uchun /balance.")

@bot.message_handler(commands=["order", "balance", "admin", "reseller"])
def handle_commands(message):
    if message.text.startswith("/order"):
        handle_order(bot, message)
    elif message.text.startswith("/balance"):
        handle_reseller(bot, message)
    elif message.text.startswith("/admin"):
        handle_admin_commands(bot, message)
    elif message.text.startswith("/reseller"):
        handle_reseller(bot, message)

bot.polling()

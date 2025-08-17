def handle_admin_commands(bot, message):
    if message.from_user.id != 123456789:  # Admin ID
        bot.reply_to(message, "Siz admin emassiz.")
        return
    bot.reply_to(message, "Admin komandalar: /setprice, /addbalance")

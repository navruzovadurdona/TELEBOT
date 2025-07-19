import telebot

TOKEN = '8146046292:AAGPYmjXp5prY00yPhLQSCyLdc3dQuyBmzg'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Ассаламу алайкум ва рохматуллох 😊\n\nБот атайын канал излаш ва ссылка бериш учун ишлаб чиқилди.")

@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message, "Маълумот: Канал излаш ва ссылка бериш учун ишлатилади.")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "Буйруқлар:\n/start - бошлаш\n/info - маълумот\n/help - ёрдам\n/search_channel - канал излаш\n/question - савол бериш\n/give_channel_nik - канал ссылкаси олиш")

@bot.message_handler(commands=['search_channel'])
def search_channel(message):
    bot.reply_to(message, "Канал номини юборинг, биз топишга ёрдам берамиз...")

@bot.message_handler(commands=['question'])
def question(message):
    bot.reply_to(message, "Саволингизни ёзинг, жавоб берамиз.")

@bot.message_handler(commands=['give_channel_nik'])
def give_channel_nik(message):
    bot.reply_to(message, "Каналнинг ссылкаси: https://t.me/yourchannel")

bot.polling()

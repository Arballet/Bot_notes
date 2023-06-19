import telebot

bot = telebot.TeleBot('check_botfather_api')

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, 'Tell me something important')

@bot.message_handler(func=lambda message: True, content_types=['text'])
def msg(message):
        print("--------------------------------------------------------------")
        print(message.from_user.last_name)
        print(message.from_user.first_name)
        print("--------------------------------------------------------------")
        file_name = str(message.from_user.last_name) + str(message.from_user.first_name)  + ".txt"
        print(file_name)
        f = open(file_name, 'a')
        f.write(message.text + ' ')
        f.close()

bot.polling(none_stop=True, interval=0)

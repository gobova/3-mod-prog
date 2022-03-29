token = "5209302325:AAEdxc0hl2aN2MKa1Nb9E1tj7f9m103GAXg"

import telebot
import os

train_text_file = r"train1.txt"
# train_text_file = r"train2.txt"
# train_text_file = r"train3.txt"
# train_text_file = r"train4.txt"

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

	os.system(fr"py ./model.py -g -t {train_text_file}")
	f = open("result.txt", "r")
	response = f.read()
	f.close()
	
	bot.send_message(message.from_user.id, response)

bot.polling(none_stop=True, interval=0)
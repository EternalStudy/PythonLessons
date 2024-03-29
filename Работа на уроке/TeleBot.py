import telebot
import requests
import time

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)
"""
@bot.message_handler(content_types=['text'])
def greetings(message):
	text = message.text
	if text == 'котик':
		req = requests.get(f'https://cataas.com/cat?{time.time()}')
		bot.send_photo(message.from_user.id, req.content)
	# if 'привет' in text:
	#     bot.reply_to(message, f'Привет, {message.from_user.first_name}')
	# if text == 'погода':
	#     req = requests.get('https://wttr.in/?0T')
	#     bot.reply_to(message, req.text)
"""
bot.polling()
import telebot
import requests
import time

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
	

@bot.message_handler(content_types=['text'])
def text_message(message):
	#print(message)
	data = open('log.txt', mode='a', encoding='utf-8')
	text = f'{message.from_user.first_name} {message.from_user.last_name}: {message.text}\n'
	data.write(text)
	data.close()
	if message.text == 'регистрация':
		data = open('registred_users.txt', mode='r', encoding='utf-8')
		id_list = data.readlines()
		data.close()
		id_list = list(el[:-1] for el in id_list)
		if str(message.from_user.id) not in id_list:
			data = open('registred_users.txt', mode='a', encoding='utf-8')
			data.write(f'{message.from_user.id}\n')
			data.close()
			bot.reply_to(message, 'Регистрация прошла успешно!')
		else:
			bot.reply_to(message, 'Вы уже зарегистрированы!')
	elif message.text == 'оповещение':
		data = open('registred_users.txt', mode='r', encoding='utf-8')
		id_list = data.read().split('\n')
		data.close()
		id_list = id_list[:-1]
		for id in id_list:
			bot.send_message(id, 'совещание через 5 минут')
		
	
bot.polling()

""" Кнопки и функционал"""
markup = types.ReplyKeyboardMarkup(row_width=1)
btn_reg = types.KeyboardButton('регистрация')
btn_alarm = types.KeyboardButton('оповещение')
markup.add(btn_reg, btn_alarm)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.from_user.id, "Привет, я бот Питоша.", reply_markup=markup)
	

@bot.message_handler(content_types=['text'])
def text_message(message):
	#print(message)
	data = open('log.txt', mode='a', encoding='utf-8')
	text = f'{message.from_user.first_name} {message.from_user.last_name}: {message.text}\n'
	data.write(text)
	data.close()
	if message.text == 'регистрация':
		data = open('registred_users.txt', mode='r', encoding='utf-8')
		id_list = data.readlines()
		data.close()
		id_list = list(el[:-1] for el in id_list)
		if str(message.from_user.id) not in id_list:
			data = open('registred_users.txt', mode='a', encoding='utf-8')
			data.write(f'{message.from_user.id}\n')
			data.close()
			bot.reply_to(message, 'Регистрация прошла успешно!')
		else:
			bot.reply_to(message, 'Вы уже зарегистрированы!')
	elif message.text == 'оповещение':
		data = open('registred_users.txt', mode='r', encoding='utf-8')
		id_list = data.read().split('\n')
		data.close()
		id_list = id_list[:-1]
		for id in id_list:
			bot.send_message(id, 'совещание через 5 минут')
		
	
bot.polling()
"""Добавьте в telegram-бота игру «Угадай числа».
Бот загадывает число от 1 до 1000. Когда игрок угадывает его, бот выводит количество сделанных ходов."""

import telebot

bot = telebot.TeleBot("6197585226:AAFFC413GxsinyXZAa_PqzFOwedX5rYQK8Q")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message.chat.id, "Привет. Я хочу сыграть с тобой в игру. Я загадал число от 1 до 1000, попробуй угадать")

@bot.message_handler()
def greetings(message):
	random = random.randint(1,1000)
	count = 1
	if message.text == random:
			bot.reply_to(f"Вы угадали. Количество попытток {count}")
	else:
		print("Вы не угадали. Введите новое число")
		while message.text != random:
			if message.text == random:
				bot.reply_to(f"Вы угадали. Количество попытток {count}")
		count += 1
bot.polling()
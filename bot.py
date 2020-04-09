import os, time
import telebot
import sqlite3
import wolframalpha
from telebot import *
app_id = "LL29U8-RXX6PHLV5P" 
client = wolframalpha.Client(app_id) 
bot = telebot.TeleBot('964957577:AAHQlnTDLdyLxDsrnsSE8M0HcxRwMup6YDk')

@bot.message_handler(content_types=['text'])
def send_text(message):
	if message.text.lower() == 'уравнение':
            send = bot.send_message(message.chat.id, "Введи уравнение!:")
            bot.register_next_step_handler(send, user_equation)
            def user_equation():
                try:
                    equation = message.text
                    res = client.query(equation)
                    answer = next(res.results).text
                    bot.send_message(message.chat.id, answer)
                except:
                    print("error")

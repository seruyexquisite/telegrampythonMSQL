import os
import sys
import telebot
from pprint import pprint
from string import Template
import mysql.connector

# Telegram your token
bot = telebot.TeleBot(")
# Telegram your group id
group_id = -1

# получить id канала/группы
#print(bot.get_chat('@botanskiytest').id)

try:
    db = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="%%%",
      port="1111",
      database="t"
    )


cursor = db.cursor()

#cursor.execute("CREATE DATABASE users")

#cursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, \
#first_name VARCHAR(255), phone VARCHAR(255), telegram_user_id INT(11) UNIQUE)")

user_data = {}

class User:
    def __init__(self, first_name):
        self.first_name = first_name
        self.phone = ''
       ]

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
        msg = bot.send_message(message.chat.id, "Введите имя и фамилию")
        bot.register_next_step_handler(msg, process_firstname_step)

def process_firstname_step(message):
    try:
        user_id = message.from_user.id
        user_data[user_id] = User(message.text)

        msg = bot.send_message(message.chat.id, "Напишите mobile phone")
        bot.register_next_step_handler(msg, process_phone_step)
        
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_phone_step(message):
    try:
        user_id = message.from_user.id
        user = user_data[user_id]
        user.phone = message.text

        # Регистрация заявки
        sql = "INSERT INTO regs (first_name, phone, user_id) \
                                  VALUES (%s, %s, %s)"
        val = (user.first_name, user.phone5%, user_id)
        cursor.execute(sql, val)
        db.commmit()
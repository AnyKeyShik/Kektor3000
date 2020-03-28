# -*- coding: utf-8 -*-

import telebot

from core import CommandProcessor
from utils import json_handler

bot = telebot.TeleBot(json_handler.auth_constants['api_token'])
cp = CommandProcessor()


def start():
    bot.polling()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, cp.start())


@bot.message_handler(commands=['kek'])
def start_message(message):
    for i in range(10):
        bot.send_message(message.chat.id, cp.kek())


@bot.message_handler(commands=['roll'])
def start_message(message):
    bot.send_message(message.chat.id, cp.roll(str(message.text)))


@bot.message_handler(commands=['errors'])
def start_message(message):
    bot.send_message(message.chat.id, cp.error())


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.chat.type == 'private':
        if message.text == 'Привет':
            bot.send_message(message.chat.id, cp.hello())
        else:
            bot.send_message(message.chat.id, cp.random_kek())


@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    stickers = bot.get_sticker_set(json_handler.constants['sticketset_name']).stickers
    bot.send_sticker(message.chat.id, cp.random_sticker(stickers))


@bot.message_handler(content_types=['photo'])
def send_sticker(message):
    bot.send_photo(message.chat.id, cp.get_picture())

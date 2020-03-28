# -*- coding: utf-8 -*-

import telebot
from time import sleep
import random

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
    # TODO: REWRITE!!!!!
    for i in range(10):
        bot.send_message(message.chat.id, cp.kek())
        sleep(0.1)
    ###################


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, cp.hello())
    else:
        bot.send_message(message.chat.id, cp.random_kek())


@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    stickers = bot.get_sticker_set(json_handler.constants['sticketset_name']).stickers
    bot.send_sticker(message.chat.id, cp.random_sticker(stickers))

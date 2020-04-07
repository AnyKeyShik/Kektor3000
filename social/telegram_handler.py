# -*- coding: utf-8 -*-

#  Copyright (c) 2020.
#
#  Created by AnyKeyShik Rarity
#
#  Telegram: @AnyKeyShik
#  GitHub: https://github.com/AnyKeyShik
#  E-mail: nikitav59@gmail.com
#
#  Created by AnyKeyShik Rarity
#
#  Telegram: @AnyKeyShik
#  GitHub: https://github.com/AnyKeyShik
#  E-mail: nikitav59@gmail.com

import telebot

from core import CommandProcessor
from utils import json_handler, debug

bot = telebot.TeleBot(json_handler.auth_constants['api_token'])
cp = CommandProcessor()
TAG = 'TELEGRAM HANDLER'


def start():
    bot.polling()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, cp.start())


@bot.message_handler(commands=['kek'])
def kek_message(message):
    for i in range(10):
        bot.send_message(message.chat.id, cp.kek())


@bot.message_handler(commands=['roll'])
def roll_message(message):
    bot.send_message(message.chat.id, cp.roll(str(message.text)))


@bot.message_handler(commands=['errors'])
def errors_message(message):
    bot.send_message(message.chat.id, cp.error(), parse_mode='Markdown', disable_web_page_preview=True)


@bot.message_handler(content_types=['text'])
def send_text(message):
    debug(TAG, message)
    if message.chat.type == 'private' or message.text.lower().find('кек') != -1:
        if message.text.lower() == 'привет':
            bot.send_message(message.chat.id, cp.hello())
        else:
            bot.send_message(message.chat.id, cp.random_kek())


@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    stickers = bot.get_sticker_set(json_handler.constants['sticketset_name']).stickers
    bot.send_sticker(message.chat.id, cp.random_sticker(stickers))
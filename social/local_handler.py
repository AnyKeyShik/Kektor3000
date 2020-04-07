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

# -*- coding: utf-8 -*-

from core import CommandProcessor
from utils import debug

cp = CommandProcessor()
TAG = 'LOCAL HANDLER'


def start():
    while True:
        message = input("> ")
        process(message)


def process(message):
    debug(TAG, "Get message '" + message + "'")

    if message.find('/start') != -1:
        start_message()
    elif message.find('/kek') != -1:
        kek_message()
    elif message.find('/roll') != -1:
        roll_message(message)
    else:
        send_text(message)


def start_message():
    print(cp.start())


def kek_message():
    for i in range(10):
        print(cp.kek())


def roll_message(message):
    print(cp.roll(message))


def errors_message():
    print(cp.error())


def send_text(message):
    if message == 'Привет':
        print(cp.hello())
    else:
        print(cp.random_kek())

# -*- coding: utf-8 -*-

import random

from utils import json_handler, debug, info


class CommandProcessor(object):
    def __init__(self):
        self.TAG = "CommandProcessor"

    def start(self):
        """
        Return start answer by '/start' command

        :return: start answer
        :rtype: str
        """

        info(self.TAG, "Start answer")
        return json_handler.messages['start_answer']

    def hello(self):
        """
        Return hello answer by 'hello' message

        :return: hello answer
        :rtype: str
        """

        info(self.TAG, "Hello answer")
        return json_handler.messages['hello_answer']

    def kek(self):
        """
        Just KEK

        :return: KEK
        :rtype: str
        """

        info(self.TAG, "KEK")
        return json_handler.messages['kek']

    def random_kek(self):
        """
        Send random phrase about kek

        :return: random phrase
        :rtype: str
        """

        info(self.TAG, "Random KEK")
        choices = json_handler.messages['random_kek']
        num = random.randint(1, 100 * len(choices))
        return choices[num // 100]

    def random_sticker(self, stickers):
        """
        Send random sticker

        :return: sticker id
        :rtype: str
        """

        num = random.randint(1, 100 * len(stickers))
        return stickers[num // 100].file_id

    def roll(self, argument):
        """
        Choice of provided options

        :return: one of many
        :rtype: str
        """

        info(self.TAG, "roll")

        sentence = " ".join(argument)
        choices = sentence.split("или")

        while choices.count("или") != 0:
            choices.remove("или")

        for index, word in enumerate(choices):
            if word.find(" ") == 0:
                choices[index] = word.replace(" ", "", 1)
            if word.rfind(" ") == len(word) - 1:
                choices[index] = word[:len(word) - 1]

        choices = list(filter(None, choices))

        debug(self.TAG, "Available choices: " + str(choices))

        if len(choices) > 1:

            num = random.randint(1, 100 * len(choices))

            return choices[num // 100]
        else:
            return json_handler.messages['no_choices_answer']

    def error(self):
        """
        Errors

        :return: list of errors
        :rtype: str
        """

        info(self.TAG, "Errors")
        return json_handler.messages['errors_answer']

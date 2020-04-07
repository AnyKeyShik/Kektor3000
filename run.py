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

from argparse import ArgumentParser

from social import local_start, remote_start
from utils import patch

parser = ArgumentParser(description="Kektor bot")
parser.add_argument("-p", "--proxy", help="Run bot with proxy", action='store_true')
parser.add_argument("-l", "--local", help="Run bot locally", action='store_true')

if __name__ == "__main__":
    args = parser.parse_args()

    if args.proxy:
        patch()

    if args.local:
        local_start()
    else:
        remote_start()

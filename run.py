# -*- coding: utf-8 -*-

from argparse import ArgumentParser

from social import start
from utils import patch

parser = ArgumentParser(description="Kektor bor")
parser.add_argument("-p", "--proxy", help="Run bot with proxy", action='store_true')

if __name__ == "__main__":
    args = parser.parse_args()

    if args.proxy:
        patch()

    start()


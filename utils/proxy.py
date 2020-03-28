# -*- coding: utf-8 -*-

import socket
import socks

from utils import log_func


@log_func()
def create_connection(address):
    """
    Create connection with custom sock

    :param address: address for connection
    :return: connection sock
    :rtype: socks.socksocket
    """

    sock = socks.socksocket()
    sock.connect(address)
    return sock


@log_func()
def config(ip, port):
    """
    Config proxy

    :param ip: proxy ip
    :param port: proxy port
    :return: None
    :rtype: None
    """

    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, ip, port)


@log_func()
def patch():
    """
    Patch the socket module

    :return: None
    :rtype: None
    """

    config("127.0.0.1", 9050)

    socket.socket = socks.socksocket
    socket.create_connection = create_connection

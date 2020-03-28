# -*- coding: utf-8 -*-

import json

import pkg_resources

from utils import debug


class JsonHandler(object):
    """
    Handler for simple get messages and consts for auth
    """

    _resource_package = None
    _resource_path = None

    _tags = None
    _tags_user = None
    _commands = None
    _commands_user = None
    _ratings = None
    _ignored = None

    _consts = None
    _auth_consts = None
    _messages = None

    _TAG = "JsonHandler"

    def __init__(self):
        self._resource_package = __name__

        self._resource_path = '/'.join(('../static', 'auth_consts.json'))
        template = pkg_resources.resource_stream(self._resource_package, self._resource_path)
        line = template.read().decode('utf-8')
        self._auth_consts = json.loads(line)
        debug(self._TAG, "Get authentication data")
        template.close()

        self._resource_path = '/'.join(('../static', 'consts.json'))
        template = pkg_resources.resource_stream(self._resource_package, self._resource_path)
        line = template.read().decode('utf-8')
        self._consts = json.loads(line)
        debug(self._TAG, "Get consts")
        template.close()

        self._resource_path = '/'.join(('../static', 'messages.json'))
        template = pkg_resources.resource_stream(self._resource_package, self._resource_path)
        line = template.read().decode('utf-8')
        self._messages = json.loads(line)
        debug(self._TAG, "Get messages for answers")
        template.close()

    @property
    def auth_constants(self):
        """
        Get app constants for auth

        :return: app constants for auth
        :rtype: dict
        """

        return self._auth_consts

    @property
    def constants(self):
        """
        Get app constants

        :return: app constants for auth
        :rtype: dict
        """

        return self._consts

    @property
    def messages(self):
        """
        Get messages for send as answer

        :return: messages templates
        :rtype: dict
        """

        return self._messages


json_handler = JsonHandler()

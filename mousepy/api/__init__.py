# Copyright 2017 NEWCRAFT GROUP B.V.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import json
from copy import deepcopy
from typing import Union

import requests


class API:
    """ Base API request handling class """

    POST_METHOD_DATA = "data"
    POST_METHOD_PARAMETERS = "params"

    url = ""
    auth = ""
    debug = False

    @property
    def response(self) -> Union[dict, list]:
        if self.init is False:
            self.init = True
            return self.refresh().response

        return self._response

    @response.setter
    def response(self, response: Union[dict, list]):
        self._response = response

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        if value is not None and value not in self.command and value is not None and value is not "":
            self.command.append(value)

    def __init__(
            self,
            command: Union[list, str],
            value: str = None,
            parent: Union['API', 'Mouseflow'] = None,
            **kwargs):
        """
        Base API communication class.
        :param command:
        :param value:
        :param parent:
        :param kwargs:
        """
        self.init = False

        if isinstance(command, str):
            command = [command]

        if value is not None and value != "":
            command.append(value)

        self.command = command
        self.arguments = kwargs

        self._response = None
        self._value = None
        self.value = value

        if parent is not None:
            self.parent = deepcopy(parent)
            self.command = parent.command + self.command
        else:
            self.parent = None

    def __str__(self):
        return str(self.response)

    def refresh(self):
        """
        Forcefully trigger the get request
        :return:
        """
        self.get(*self.command, **self.arguments)
        return self

    def get(self, *args, **kwargs):
        """
        Makes a get request

        :param args:
        :param kwargs:
        :return:
        """
        request = requests.get(
            API.url + "/".join(args),
            auth=API.auth,
            params=kwargs
        )

        if API.debug:
            print("get: ", request.url, " - ", request.reason)

        response = self.response = json.loads(request.content)

        return response

    def post(self, *args, data: list = None, method: str = POST_METHOD_PARAMETERS, **kwargs):
        """
        Makes a post request using either json or data methodology

        :param args:
        :param data:
        :param method:
        :param kwargs:
        :return:
        """
        parameters = kwargs if method is API.POST_METHOD_PARAMETERS else {}

        body_type = "data" if method is API.POST_METHOD_DATA else "json" if type(data) is list else "data"
        body_value = kwargs if method is API.POST_METHOD_DATA else data if not None else {}

        request = requests.post(
            API.url + "/".join(args) + "?" + "&".join([key + "=" + value for key, value in parameters.items()]),
            **{body_type: body_value},
            auth=API.auth
        )

        if API.debug:
            print("post: ", request.url, " - ", request.reason, "\n", "      " + method + ": ", json.dumps(kwargs))

        response = self.response = json.loads(request.content) if request.content is not b'' else {}

        return response

    def put(self, *args, **kwargs):
        """
        Makes a put request

        :param args:
        :param kwargs:
        :return:
        """
        request = requests.put(
            API.url + "/".join(args),
            data=json.dumps(kwargs),
            auth=API.auth
        )

        if API.debug:
            print("put: ", request.url, " - ", request.reason, "\n", "     data:", json.dumps(kwargs))

        self.response = {}

    def delete(self, *args, **kwargs):
        """
        Makes a delete request

        :param args:
        :param kwargs:
        :return:
        """

        request = requests.delete(
            API.url + "/".join(args) + "?" + "&".join([key + "=" + value for key, value in kwargs.items()]),
            auth=API.auth
        )

        if API.debug:
            print("delete: ", request.url, " - ", request.reason, "\n", "     params: ", json.dumps(kwargs))

        self.response = {}

    def send(self, **kwargs):
        return self.put(*self.command, **kwargs)

    def list(self) -> dict:
        raise NotImplemented


class IllegalStringLengthException(BaseException):
    def __init__(self, *args, **kwargs):  # real signature unknown
        pass

    @staticmethod  # known case of __new__
    def __new__(*args, **kwargs):  # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class CannotCreateEmptyVariablesException(BaseException):
    def __init__(self, *args, **kwargs):  # real signature unknown
        pass

    @staticmethod  # known case of __new__
    def __new__(*args, **kwargs):  # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class PageNotFoundException(Exception):
    def __init__(self, *args, **kwargs):  # real signature unknown
        pass

    @staticmethod  # known case of __new__
    def __new__(*args, **kwargs):  # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

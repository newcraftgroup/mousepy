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

from typing import Union

from requests.auth import HTTPBasicAuth

from mousepy.api import API
from mousepy.api.website import Website
from mousepy.api.websites import Websites


class Mouseflow(API):
    """
    Base class for connecting to the mouseflow API
    """
    LOCATION_EUROPE = "eu"
    LOCATION_UNITED_STATES = "us"

    def __init__(self, user, token, location=LOCATION_EUROPE, debug=False, **kwargs):
        """
        :param user: The username used to connect to mouseflow
        :param token: The token used to connect to mouseflow (Generated on the Mouseflow website)
        :param location: Server location (Defaults to LOCATION_EUROPE)
        :param debug: Enable verbose output of all mouseflow calls
        :param kwargs:
        """
        super().__init__([], **kwargs)

        self.user = user
        self.password = token
        self.location = location
        self._response = None

        API.debug = debug

        API.auth = HTTPBasicAuth(self.user, self.password)
        API.url = "https://api-" + self.location + ".mouseflow.com/"

    def websites(self, site: str = None) -> Union[Websites, Website]:
        """
        Returns `mousepy.api.recordings.Websites` unless the site parameter is provided in which case it returns `mousepy.api.recordings.Website`.

        :param site: The name of the site to retrieve
        :return: [:class:`~mousepy.api.website.Website`, :class:`~mousepy.api.websites.Websites`]
        """
        websites = Websites(self)

        if site is not None:
            return websites.website(site)

        return websites

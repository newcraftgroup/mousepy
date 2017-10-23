from typing import Union

from requests.auth import HTTPBasicAuth

from mouseflow.api import API
from mouseflow.api.website import Website
from mouseflow.api.websites import Websites


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
        Returns `mouseflow.api.recordings.Websites` unless the site parameter is provided in which case it returns `mouseflow.api.recordings.Website`.

        :param site: The name of the site to retrieve
        :return: [:class:`~mouseflow.api.website.Website`, :class:`~mouseflow.api.websites.Websites`]
        """
        websites = Websites(self)

        if site is not None:
            return websites.website(site)

        return websites

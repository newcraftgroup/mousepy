from typing import Union

from requests.auth import HTTPBasicAuth

from mouseflow.api import API
from mouseflow.api.website import Website
from mouseflow.api.websites import Websites


class Mouseflow(API):
    LOCATION_EUROPE = "eu"
    LOCATION_UNITED_STATES = "us"

    def __init__(self, user, token, location=LOCATION_EUROPE, debug=False, **kwargs):
        super().__init__([], **kwargs)

        self.user = user
        self.password = token
        self.location = location
        self._response = None

        API.debug = debug

        API.auth = HTTPBasicAuth(self.user, self.password)
        API.url = "https://api-" + self.location + ".mouseflow.com/"

    def websites(self, site: str = None) -> Union[Websites, Website]:
        websites = Websites(self)

        if site is not None:
            return websites.website(site)

        return websites

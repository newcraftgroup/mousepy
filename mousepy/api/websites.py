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

from mousepy.api import API
from mousepy.api.website import Website


class Websites(API):
    def __init__(self, parent, **kwargs):
        """
        This is a test
        :param parent:
        :param kwargs:
        """
        super().__init__("websites", parent=parent, **kwargs)

    def __str__(self):
        return str(self.response)

    def list(self, id_as_key=False, list_of_objects=False) -> dict:
        return {
            site["id" if id_as_key else "name"]: {
                "id": site["id"],
                "name": site["name"],
                "readOnly": site["readOnly"],
                "status": site["status"]
            } if not list_of_objects else Website(self, site["id"]) for site in self.response
        }

    def website(self, site):
        """
        :param site: The name of the site to target
        :return: :class:`~mousepy.api.website.Website`
        """
        if len(site) == 36 and "-" in site:
            return Website(self, site)

        site = self.list()[site]["id"]

        return Website(self, site)

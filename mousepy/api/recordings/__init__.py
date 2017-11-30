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

from mousepy.api.recordings.properties.bulktag import BulkTag
from mousepy.api.recordings.properties.tags import Tags

from mousepy.api import API
from mousepy.api.recordings.properties.variables import Variables
from mousepy.api.recordings.recording import Recording


class Recordings(API):
    def __init__(self, parent, **kwargs):
        """Get the latest recordings in the specified website, with the most recent ones first.

        :param parent: API object or Mouseflow
        :param recording_id: Optional positional argument for list selection
        :return:
        """
        super().__init__("recordings", parent=parent, **kwargs)

    def count(self):
        return self.response.get("count")

    def tags(self):
        return Tags(self)

    def recording(self, value):
        return Recording(self, value)

    def ids(self):
        return [site["id"] for site in self.response["recordings"]]

    def list(self) -> dict:
        return {site["id"]: {**site} for site in self.response["recordings"]}

    def bulktag(self, tag_name: str) -> BulkTag:
        return BulkTag(self, tag_name)

    def variables(self, **kwargs):
        """
        :param kwargs:
        :return: :class:`~mousepy.api.recordings.properties.variables.Variables`
        """
        if kwargs is not None and self.value is not "":
            return Variables(self, **kwargs)

        return Variables(self)

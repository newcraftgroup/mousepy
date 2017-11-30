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


class BulkTag(API):
    """Allows for bulk listing, creation and removal of tags"""

    def __init__(self, parent: API, tag_name: str):
        super().__init__("bulktag", parent=parent, tag=tag_name)

    def __str__(self):
        return str(self.parent.tags())

    def add(self, to: list):
        """
        :param to: List of recording ids to add the tag to
        :return: :class:`~mousepy.api.recordings.bulktag.BulkTag`
        """
        self.post(*self.command, **self.arguments, data=to)

        return self

    def remove(self, ids: list):
        """
        :param ids: List of recording ids to remove the tag from
        :return: :class:`~mousepy.api.recordings.bulktag.BulkTag`
        """
        self.delete(*self.command, **self.arguments, data=ids)

        return self

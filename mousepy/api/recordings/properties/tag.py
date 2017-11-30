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


class Tag(API):
    """Allows for the listing, creation and removal of tags"""

    def __init__(self, parent, tag_name):
        super().__init__("tag", parent=parent, **{"tag": tag_name})

    def __str__(self):
        return ", ".join(self.parent.tags())

    def add(self):
        """
        :return: :class:`~mousepy.api.recordings.tag.Tag`
        """
        self.post(*self.command, method=API.POST_METHOD_PARAMETERS, **self.arguments)

        return self

    def remove(self):
        """
        :return: :class:`~mousepy.api.recordings.tag.Tag`
        """
        self.delete(*self.command, method=API.POST_METHOD_PARAMETERS, **self.arguments)

        return self

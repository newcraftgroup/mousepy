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


class Star(API):
    def __init__(self, parent):
        super().__init__("star", parent=parent)

        self.arguments = None

    def __str__(self):
        if self.parent.command[-1] is "recordings":
            return "\n".join(self.response)

        return "\n".join(self.parent.response["variables"])

    def run(self):
        """
        :return: :class:`~mousepy.api.recordings.star.Star`
        """
        self.post(*self.command, **self.arguments)

        return self

    def remove(self):
        """
        :return: :class:`~mousepy.api.recordings.star.Star`
        """
        self.delete(*self.command, **self.arguments)

        return self

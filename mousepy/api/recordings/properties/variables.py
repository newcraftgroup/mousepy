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


class Variables(API):
    """
    Listing and creation of recording variables
    """

    def __init__(self, parent, **kwargs):
        super().__init__("variables", parent=parent)

        if "search" in self.arguments.keys():
            del self.arguments["search"]

        if len(kwargs.keys()) > 0:
            self.variables = kwargs
        else:
            self.variables = None

    def __str__(self):
        if self.parent.command[-1] is "recordings":
            return "\n".join(self.response)

        variables = self.parent.response.get("variables")

        if len(variables) == 0:
            return "[]"

        return "\n".join(variables)

    def create(self):
        """
        :return: :class:`~mousepy.api.recordings.variables.Variables`
        """
        if self.variables is None:
            return self

        self.send(**self.variables)

        return self

    def delete(self):
        """
        :return: :class:`~mousepy.api.recordings.variables.Variables`
        """
        if self.variables is None:
            return self

        self.send(**{key: None for key in self.variables.keys()})

        return self

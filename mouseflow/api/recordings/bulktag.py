import json

from mouseflow.api import API


class BulkTag(API):
    """List all available tags or"""

    def __init__(self, parent: API, tag_name: str):
        super().__init__("bulktag", parent=parent, tag=tag_name)

    def __str__(self):
        return str(self.parent.tags())

    def add(self, to: list):
        """
        :param to: List of recording ids to add the tag to
        :return:
        """
        self.post(*self.command, **self.arguments, data=to)

        return self

    def remove(self, ids: list):
        """
        :param ids: List of recording ids to remove the tag from
        :return: 
        """
        self.delete(*self.command, **self.arguments, data=ids)

        return self

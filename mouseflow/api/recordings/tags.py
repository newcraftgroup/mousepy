import json

from mouseflow.api import API


class Tags(API):
    """List all available tags or"""
    def __init__(self, parent):
        super().__init__("tags", parent=parent)

    def list(self) -> list:
        return self.response

    def __str__(self):
        return json.dumps(self.response)

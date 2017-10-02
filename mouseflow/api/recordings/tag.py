from mouseflow.api import API


class Tag(API):
    """List all available tags or"""

    def __init__(self, parent, tag_name):
        super().__init__("tag", parent=parent, **{"tag": tag_name})

    def __str__(self):
        return ", ".join(self.parent.tags())

    def add(self):
        self.post(*self.command, method=API.POST_METHOD_PARAMETERS, **self.arguments)

        return self

    def remove(self):
        self.delete(*self.command, method=API.POST_METHOD_PARAMETERS, **self.arguments)

        return self

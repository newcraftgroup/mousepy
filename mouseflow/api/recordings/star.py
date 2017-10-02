from mouseflow.api import API


class Star(API):
    def __init__(self, parent):
        super().__init__("star", parent=parent)

        self.arguments = None

    def __str__(self):
        if self.parent.command[-1] is "recordings":
            return "\n".join(self.response)

        return "\n".join(self.parent.response["variables"])

    def run(self):
        self.post(*self.command, **self.arguments)

        return self

    def remove(self):
        self.delete(*self.command, **self.arguments)

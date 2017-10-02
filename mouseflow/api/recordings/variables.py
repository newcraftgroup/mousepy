from mouseflow.api import API


class Variables(API):
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
        if self.variables is None:
            return self

        self.send(**self.variables)

        return self

    def delete(self):
        if self.variables is None:
            return self

        self.send(**{key: None for key in self.variables.keys()})

        return self

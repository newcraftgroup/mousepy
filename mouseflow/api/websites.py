from mouseflow.api import API
from mouseflow.api.website import Website


class Websites(API):
    def __init__(self, parent, **kwargs):
        """
        This is a test
        :param parent:
        :param kwargs:
        """
        super().__init__("websites", parent=parent, **kwargs)

    def __str__(self):
        return str(self.response)

    def list(self, id_as_key=False, list_of_objects=False) -> dict:
        return {
            site["id" if id_as_key else "name"]: {
                "id": site["id"],
                "name": site["name"],
                "readOnly": site["readOnly"],
                "status": site["status"]
            } if not list_of_objects else Website(self, site["id"]) for site in self.response
        }

    def website(self, site):
        if len(site) == 36 and "-" in site:
            return Website(self, site)

        site = self.list()[site]["id"]

        return Website(self, site)

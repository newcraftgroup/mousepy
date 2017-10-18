from mouseflow.api import API


class Heatmaps(API):
    def __init__(self, parent, uri: str = "", **kwargs):
        if uri is None:
            uri = ""

        super().__init__(["pagelist"], value=uri, parent=parent, **kwargs)

    def list(self, detailed=False):
        """
        Lists all available pages along with their specs
        :return:
        """

        if detailed:
            return {page["uri"]: {
                "title": page["title"],
                "displayUrl": page["displayUrl"],
                "token": page["token"] if "token" in page.keys() else "",
                "views": page["views"],
                "visitTime": page["visitTime"],
                "engagementTime": page["engagementTime"],
                "clicks": page["clicks"],
                "renderTime": page["renderTime"],
                "scroll": page["scroll"],
                "fold": page["fold"],
                "height": page["height"],
                "size": page["size"]
            } for page in self.response["pages"]}

        return {page["uri"]: {
            "title": page["title"],
            "displayUrl": page["displayUrl"]
        } for page in self.response["pages"]}

    def page_list(self) -> list:
        return Heatmaps(self.parent, "urls").response["urls"]

    def details(self, uri):
        return Heatmaps(self.parent, url=uri)

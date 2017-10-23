from mouseflow.api.recordings.properties.bulktag import BulkTag
from mouseflow.api.recordings.properties.tags import Tags

from mouseflow.api import API
from mouseflow.api.recordings.properties.variables import Variables
from mouseflow.api.recordings.recording import Recording


class Recordings(API):
    def __init__(self, parent, **kwargs):
        """Get the latest recordings in the specified website, with the most recent ones first.

        :param parent: API object or Mouseflow
        :param recording_id: Optional positional argument for list selection
        :return:
        """
        super().__init__("recordings", parent=parent, **kwargs)

    def count(self):
        return self.response.get("count")

    def tags(self):
        return Tags(self)

    def recording(self, value):
        return Recording(self, value)

    def ids(self):
        return [site["id"] for site in self.response["recordings"]]

    def list(self) -> dict:
        return {site["id"]: {**site} for site in self.response["recordings"]}

    def variables(self, **kwargs):
        """
        :param kwargs:
        :return: :class:`~mouseflow.api.recordings.properties.variables.Variables`
        """
        if kwargs is not None and self.value is not "":
            return Variables(self, **kwargs)

        return Variables(self)

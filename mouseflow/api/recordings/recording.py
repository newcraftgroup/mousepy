from mouseflow.api import API
from mouseflow.api.recordings.star import Star
from mouseflow.api.recordings.tag import Tag
from mouseflow.api.recordings.variables import Variables


class Recording(API):
    def __init__(self, parent, recording_id: str, **kwargs):
        r"""Get the latest recordings in the specified website, with the most recent ones first.

            GET /websites/{website-id}/recordings

            :param parent: API object or Mouseflow
            :param recording_id: Optional positional argument for list selection
            :return:
        """
        super().__init__(recording_id, parent=parent, **kwargs)

    def id(self):
        return self.response.get("id")

    def token(self):
        return self.response.get("token")

    def created(self):
        return self.response.get("created")

    def last_activity(self):
        return self.response.get("lastActivity")

    def page_views(self):
        return self.response.get("pageViews")

    def duration(self):
        return self.response.get("duration")

    def pages(self):
        return self.response.get("pages")

    def country(self):
        return self.response.get("country")

    @property
    def city(self):
        return self.response.get("city")

    def isp(self):
        return self.response.get("isp")

    def ip(self):
        return self.response.get("ip")

    def language(self):
        return self.response.get("language")

    def user_agent(self):
        return self.response.get("userAgent")

    def browser(self):
        return self.response.get("browser")

    def browser_version(self):
        return self.response.get("browserVersion")

    def screen_resolution(self):
        return self.response.get("screenRes")

    def os(self):
        return self.response.get("os")

    def os_version(self):
        return self.response.get("osVersion")

    def device(self):
        return self.response.get("device")

    def referrer(self):
        return self.response.get("referrer")

    def tags(self):
        return self.response.get("tags")

    def starred(self):
        return self.response.get("starred")

    @property
    def lng(self):
        return self.response.get("lng")

    @property
    def lat(self):
        return self.response.get("lat")

    def visitor_id(self):
        return self.response.get("visitorId")

    def visitor_name(self):
        return self.response.get("visitorName")

    def recording(self, recording_id):
        return Recording(self, recording_id)

    def tag(self, tag_name: str = None):
        return Tag(self, tag_name)

    def star(self):
        return Star(self)

    def variables(self, **kwargs):
        if kwargs is not None and self.value is not "":
            return Variables(self, **kwargs)

        return Variables(self)

from typing import Union

import mouseflow
from mouseflow.api import API, IllegalStringLengthException
from mouseflow.api.heatmaps import Heatmaps
from mouseflow.api.recordings.recording import Recording
from mouseflow.api.recordings.recordings import Recordings


class Website(API):
    ALIGNMENT_CENTER = "Center"
    ALIGNMENT_LEFT = "Left"
    ALIGNMENT_RIGHT = "RIGHT"
    ALIGNMENT_FLEXIBLE = "RIGHT"

    STATUS_NOT_INSTALLED = "NotInstalled"
    STATUS_RECORDING = "Recording"
    STATUS_STOPPED = "Stopped"
    STATUS_PAUSED = "Paused"

    def __init__(self, parent, site_name: str, **kwargs):
        super().__init__(site_name, parent=parent, **kwargs)

        if mouseflow.Mouseflow.debug and self.read_only:
            print("!!! WARNING: ACCESSING READ ONLY WEBSITE !!!")

    def __str__(self):
        return str(self.response)

    @property
    def id(self):
        return self.response.get("id")

    @property
    def name(self) -> str:
        return self.response.get("name")

    @name.setter
    def name(self, value: str):
        if not value:
            raise ValueError

        self.put(**self.command, **{"name": value})

    @property
    def created(self):
        return self.response.get("created")

    @property
    def status(self):
        return self.response.get("status")

    @status.setter
    def status(self, value):
        if value not in [Website.STATUS_NOT_INSTALLED,
                         Website.STATUS_PAUSED,
                         Website.STATUS_RECORDING,
                         Website.STATUS_STOPPED]:
            raise ValueError

        self.put(**self.command, **{"status": value})

    @property
    def read_only(self) -> bool:
        # Avoid having to make a new API call if not necessary
        if isinstance(self.parent, mouseflow.Websites) and self.parent.init is True:
            return self.parent.list(True)[self.command[-1]]["readOnly"]

        return self.response.get("readOnly")

    @property
    def domains(self):
        return self.response.get("domains")

    @property
    def recording_rate(self):
        return self.response.get("recordingRate")

    @recording_rate.setter
    def recording_rate(self, value: int):
        if value < 1:
            raise ValueError

        self.put(**self.command, **{"recordingRate": value})

    @property
    def alignment(self):
        return self.response.get("alignment")

    @alignment.setter
    def alignment(self, value: str):
        if value not in [Website.ALIGNMENT_LEFT,
                         Website.ALIGNMENT_CENTER,
                         Website.ALIGNMENT_RIGHT,
                         Website.ALIGNMENT_FLEXIBLE]:
            raise ValueError

        self.put(**self.command, **{"alignment": value})

    @property
    def width(self):
        return self.response.get("width")

    @width.setter
    def width(self, value: str):
        if not value:
            raise ValueError

        self.put(**self.command, **{"width": value})

    @property
    def page_identifiers(self):
        return self.response.get("pageIdentifiers")

    @property
    def encoding(self):
        return self.response.get("encoding")

    @property
    def anonymize_ips(self):
        return self.response.get("anonymizeIps")

    @property
    def excluded_ips(self):
        return self.response.get("excludedIps")

    @property
    def merge_urls(self):
        return self.response.get("mergeUrls")

    def recordings(self,
                   id: str = None,
                   search: str = None,
                   from_date=None,
                   to_date=None,
                   country: str = None,
                   tags: list = None,
                   vars: dict = None,
                   star: bool = None,
                   limit: int = None,
                   meta: bool = False,
                   **kwargs) -> Union[Recordings, Recording]:
        """
        :param id:
        :param search:
        :param from_date:
        :param to_date:
        :param country:
        :param tags:
        :param vars:
        :param star:
        :param limit:
        :param meta: Alias for limit = 0
        :param kwargs: Other potential filters as documented in https://api-docs.mouseflow.com/#filters
        :return:
        """

        if limit is not None:
            kwargs["limit"] = limit
        if limit is None and meta is True:
            kwargs["limit"] = 0
        if from_date is not None:
            kwargs["fromDate"] = from_date
        if to_date is not None:
            kwargs["toDate"] = to_date
        if search is not None:
            kwargs["search"] = search
        if country is not None:
            if len(country) > 2:
                raise IllegalStringLengthException
            kwargs["country"] = str.lower(country)
        if star is not None:
            kwargs["star"] = 1 if star is True else 0
        if tags is not None:
            kwargs["tags"] = ",".join(tags)
        if vars is not None:
            kwargs["vars"] = ",".join(["%s=%s" % (key, value) for (key, value) in vars.items()])

        if id is not None:
            return Recordings(self, **kwargs).recording(id)

        return Recordings(self, **kwargs)

    def heatmaps(self) -> Heatmaps:
        return Heatmaps(self)

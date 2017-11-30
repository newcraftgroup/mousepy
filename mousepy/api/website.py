# Copyright 2017 NEWCRAFT GROUP B.V.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from typing import Union

import mousepy
from mousepy.api import API, IllegalStringLengthException
from mousepy.api.heatmaps import Heatmaps
from mousepy.api.recordings import Recordings
from mousepy.api.recordings.recording import Recording


class Website(API):
    ALIGNMENT_CENTER = "Center"
    ALIGNMENT_LEFT = "Left"
    ALIGNMENT_RIGHT = "Right"
    ALIGNMENT_FLEXIBLE = "Flexible"

    STATUS_NOT_INSTALLED = "NotInstalled"
    STATUS_RECORDING = "Recording"
    STATUS_STOPPED = "Stopped"
    STATUS_PAUSED = "Paused"

    def __init__(self, parent, site_name: str, **kwargs):
        super().__init__(site_name, parent=parent, **kwargs)

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
        if isinstance(self.parent, mousepy.Websites) and self.parent.init is True:
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
                   recording_id: str = None,
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
        Returns :class:`~mousepy.api.recordings.recording.Recording` if an id is provided otherwise returns :class:`~mousepy.api.recordings.Recordings`

        :param recording_id: Recording ID filter
        :param search: Text search filter
        :param from_date: Start date filter
        :param to_date: End date filter
        :param country: country filter
        :param tags: tag filter
        :param vars: variable filter
        :param star: star filter
        :param limit: Maximum amount of values returned
        :param meta: Alias for limit = 0
        :param kwargs: Other potential filters as documented in https://api-docs.mouseflow.com/#filters
        :return: :class:`~mousepy.api.recordings.Recordings` or :class:`~mousepy.api.recordings.recording.Recording`
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

        if recording_id is not None:
            return Recordings(self, **kwargs).recording(recording_id)

        return Recordings(self, **kwargs)

    def heatmaps(self, uri=None) -> Heatmaps:
        """
        :param uri: Uri of the page to load the heatmaps from.
        :return: :class:`~mousepy.api.heatmaps.Heatmaps`
        """
        return Heatmaps(self, uri)

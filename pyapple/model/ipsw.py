from datetime import datetime
from typing import Optional
from dateutil import tz
from hurry.filesize import size, alternative


class IPSW:
    def __init__(
        self,
        identifier: str,
        buildid: str,
        version: str,
        url: str,
        filesize: int,
        sha1: str,
        md5: str,
        releasedate: str,
        uploaddate: str,
        signed: bool,
    ) -> None:
        self.identifier = identifier
        self.buildid = buildid
        self.version = version
        self.uri = url
        self.filesize = (filesize, self._tofilesize(filesize))
        self.sha1 = sha1
        self.md5 = md5
        self.signed = signed
        self.releasedate = self._todatetime(releasedate)
        self.uploaddate = self._todatetime(uploaddate)

    def _todatetime(self, time: str):
        dest = tz.tzutc()
        obj = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
        obj = obj.replace(tzinfo=dest)
        return obj

    def _tofilesize(self, value: int):
        return size(value, system=alternative)


class IPSWKeys:
    def __init__(
        self,
        identifier: str,
        buildid: str,
        codename: str,
        baseband: str,
        updateramdisk: bool,
        restoreramdisk: bool,
        keys: Optional[list],
    ) -> None:
        self.identifier = identifier
        self.buildid = buildid
        self.codename = codename
        self.baseband = baseband
        self.updateramdisk = updateramdisk
        self.restoreramdisk = restoreramdisk
        self.keys = keys


class OTAIPSW:
    def __init__(
        self,
        identifier: str,
        buildid: str,
        version: str,
        url: str,
        filesize: int,
        prereq_buildid: str,
        prereq_version: str,
        release_type: str,
        uploaddate: str,
        releasedate: str,
        signed: bool,
    ) -> None:
        self.identifier = identifier
        self.buildid = buildid
        self.version = version
        self.uri = url
        self.filesize = (filesize, self._tofilesize(filesize))
        self.prereq_buildid = prereq_buildid
        self.prereq_version = prereq_version
        self.release_type = release_type
        self.upload_date = self._todatetime(uploaddate)
        self.release_date = self._todatetime(releasedate)
        self.signed = signed

    def _todatetime(self, time: str):
        dest = tz.tzutc()
        obj = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
        obj = obj.replace(tzinfo=dest)
        return obj

    def _tofilesize(self, value: int):
        return size(value, system=alternative)
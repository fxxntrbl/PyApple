from typing import List

from ..interface import IPSW, OTA, DeviceKeys, FirmwareKeys, iDevice
from ..utils import AsyncRequest


class IPSWME:
    def __init__(self) -> None:
        self.__HTTP = AsyncRequest()
        super().__init__()

    async def fetch_device(self, identifier: str) -> iDevice:
        data = await self.__HTTP.ipsw(
            endpoint=f"/device/{identifier}", return_type="json"
        )
        data["firmwares"] = [IPSW(**firmware) for firmware in data["firmwares"]]

        await self.__HTTP.session.close()
        return iDevice(**data)

    async def search_ipsw(self, identifier: str, buildid: str) -> IPSW:
        data = await self.__HTTP.ipsw(
            endpoint=f"/ipsw/{identifier}/{buildid}", return_type="json"
        )

        await self.__HTTP.session.close()
        return IPSW(**data)

    async def fetch_ipsw_version(self, version: str) -> List[IPSW]:
        data = await self.__HTTP.ipsw(endpoint=f"/ipsw/{version}", return_type="json")

        return [IPSW(**firmware) for firmware in data]

    async def device_keys(self, identifier: str) -> List[DeviceKeys]:
        data = await self.__HTTP.ipsw(
            endpoint=f"/keys/device/{identifier}", return_type="json"
        )

        await self.__HTTP.session.close()
        return [DeviceKeys(**keys) for keys in data]

    async def firmware_keys(self, identifier: str, buildid: str) -> DeviceKeys:
        data = await self.__HTTP.ipsw(
            endpoint=f"/keys/ipsw/{identifier}/{buildid}", return_type="json"
        )
        data["keys"] = [FirmwareKeys(**keys) for keys in data["keys"]]

        await self.__HTTP.session.close()
        return DeviceKeys(**data)

    async def search_ota(self, identifier: str, buildid: str) -> OTA:
        data = await self.__HTTP.ipsw(
            endpoint=f"/ota/{identifier}/{buildid}", return_type="json"
        )

        await self.__HTTP.session.close()
        return OTA(**data)

    async def fetch_ota_version(self, version: str) -> List[OTA]:
        data = await self.__HTTP.ipsw(endpoint=f"/ota/{version}", return_type="json")

        await self.__HTTP.session.close()
        return [OTA(**ota) for ota in data]

    async def fetch_ota_docs(self, identifier: str, version: str) -> str:
        data = await self.__HTTP.ipsw(
            endpoint=f"/ota/documentation/{identifier}/{version}", return_type="text"
        )

        await self.__HTTP.session.close()
        return data

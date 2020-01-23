
from platform_sdk.utils.http import HttpClient


class DomainReaderApi:
    def __init__(self, uri):
        self.base_uri = uri
        self.client = HttpClient()

    def get_map_entities(self, _map, _type, _params):
        uri = self._mount_uri(_map, _type, _params)
        return self.client.get(uri)

    def _mount_uri(self, _map, _type, _params):
        return '{}{}/{}?{}'.format(self.base_uri, _map, _type, _params)
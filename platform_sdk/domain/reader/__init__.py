
from platform_sdk.utils.http import HttpClient


class ReaderApi:
    def __init__(self, reader_settings):
        self.base_uri = reader_settings['uri']
        self.client = HttpClient()

    def get_entities(self, _map, _type, _params):
        uri = self.get_uri(_map, _type, _params)
        result = self.client.get(uri)
        if not result.has_error and result.content:
            return result.content[0]

    def get_uri(self, _map, _type, _params):
        return '{}{}/{}?{}'.format(self.base_uri, _map, _type, _params)

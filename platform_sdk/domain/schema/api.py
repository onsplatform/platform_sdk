import os

from platform_sdk.utils.http import HttpClient


class SchemaApi:
    def __init__(self, schema_settings):
        self.base_uri = schema_settings['uri']
        self.client = HttpClient()

    def get_schema(self, _map, _type):
        uri = self.get_uri(_map, _type)
        result = self.client.get(uri)
        if not result.has_error:
            return result.content

    def get_uri(self, _map, _type):
        return  '{}{}/{}'.format(self.base_uri, _map, _type)

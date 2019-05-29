from platform_sdk.utils.http import HttpClient


class SchemaApi:
    def __init__(self, schema_settings):
        self.base_uri = schema_settings['api_url']
        self.client = HttpClient()

    def get_schema(self, solution, app, _map):
        uri = self.get_uri(solution, app, _map)
        result = self.client.get(uri)
        if not result.has_error:
            return result.content

    def get_uri(self, solution, app, _map):
        return  f'{self.base_uri}{solution}/{app}/{_map}'

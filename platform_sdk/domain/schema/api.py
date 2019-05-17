import requests


class SchemaApi:
    def __init__(self, schema_settings):
        self.url_schema_api = schema_settings['api_url']

    def get_schema(self, solution, app, _map):
        api_response = self._get_schema_response(solution, app, _map)
        if api_response:
            return api_response.json()

    def _get_schema_response(self, solution, app, _map):
        response = requests.get(self._get_schema_api_url(solution, app, _map))
        if response.ok:
            return response

        raise Exception('http error')

    def _get_schema_api_url(self, solution, app, _map):
        return self.url_schema_api + '{0}/{1}/{2}'.format(solution, app, _map)

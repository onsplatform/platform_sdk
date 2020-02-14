from platform_sdk.utils.http import HttpClient


class SchemaApi:
    def __init__(self, schema_settings):
        self.base_uri = schema_settings['uri']
        self.client = HttpClient()

    def get_schema(self, _map, _type):
        uri = self._get_uri(_map, _type)
        result = self.client.get(uri)
        if not result.has_error and result.content:
            return result.content[0]

    def set_reprocessing(self, solution):
        uri = self._get_solution_byname_uri(solution)
        result = self.client.get(uri)
        if not result.has_error and result.content:
            solution = result.content[0]
            solution['is_reprocessing'] = True
            uri = self._get_solution_byid_uri(solution['id'])
            self.client.put(uri, solution)

    def is_reprocessing(self, solution):
        uri = self._get_solution_byname_uri(solution)
        result = self.client.get(uri)
        if not result.has_error and result.content:
            return result.content[0]['is_reprocessing']

    def get_reprocessable_solutions(self):
        uri = self._get_solutions_uri()
        result = self.client.get(uri)
        if not result.has_error and result.content:
            solutions = result.content
            return [solution for solution in solutions if solution['is_reprocessable']]

    def _get_solutions_uri(self):
        return '{}solution'.format(self.base_uri)

    def _get_solution_byid_uri(self, id):
        return '{}solution/{}/'.format(self.base_uri, id)

    def _get_solution_byname_uri(self, solution):
        return '{}solution/byname/{}'.format(self.base_uri, solution)

    def _get_uri(self, _map, _type):
        return '{}{}/{}'.format(self.base_uri, _map, _type)

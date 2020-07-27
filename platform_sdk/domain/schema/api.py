from platform_sdk.utils.http import HttpClient


class SchemaApi:
    def __init__(self, schema_settings):
        self.base_uri = schema_settings['uri']
        self.client = HttpClient()

    def get_reprocessable_tables_grouped_by_tags(self, tag_and_entities):
        uri = self._get_reprocessable_tables_grouped_by_tags_uri()
        result = self.client.post(uri, tag_and_entities)
        if not result.has_error and result.content:
            return result.content

    def get_schema(self, _map, _version, _type):
        uri = self._get_uri(_map, _version, _type)
        result = self.client.get(uri)
        if not result.has_error and result.content:
            schema = result.content[0]
            if schema:
                by_id_filter = [filter for filter in schema['filters'] if filter['name'].lower() == 'byid']
                if not by_id_filter:
                    schema['filters'].append(
                        {
                            'name': 'byId',
                            'expression': 'id = :id',
                            'parameters': [
                                {
                                    'name': 'id',
                                    'is_array': False
                                }
                            ]
                        }
                    )
                return schema

    def set_reprocessing(self, solution):
        uri = self._get_solution_byname_uri(solution)
        result = self.client.get(uri)
        if not result.has_error and result.content:
            solution = result.content[0]
            solution['is_reprocessing'] = True
            uri = self._get_solution_byid_uri(solution['id'])
            self.client.put(uri, solution)

    def get_solution_by_name(self, solution):
        uri = self._get_solution_byname_uri(solution)
        result = self.client.get(uri)
        if not result.has_error and result.content:
            return result.content[0]

    def is_reprocessing(self, solution):
        uri = self._get_active_reprocess_bysolutionid_uri(solution)
        result = self.client.get(uri)
        if not result.has_error and result.content:
            return True
        return False

    def is_reproducing(self, solution):
        uri = self._get_active_reproduction_bysolutionid_uri(solution)
        result = self.client.get(uri)
        if not result.has_error and result.content:
            return True
        return False

    def get_reproduction_status(self, reproductionId):
        uri = self._get_reproduction_status_byreproductionid_uri(reproductionId)
        result = self.client.get(uri)
        
        if not result.has_error and result.content:
            if [item for item in result.content if item['is_reproducing'] is True]:
                return {status: 'active'}
            else:
                return {status: 'finished'}
        else:
            return {status: 'not_found'}

    def get_reprocessable_solutions(self):
        uri = self._get_solutions_uri()
        result = self.client.get(uri)
        if not result.has_error and result.content:
            solutions = result.content
            return [solution for solution in solutions if solution['is_reprocessable']]

    def get_solution(self, solution_id):
        uri = self._get_solution_byid_uri(solution_id)
        result = self.client.get(uri)
        if not result.has_error and result.content:
            return result.content

    def get_solutions(self):
        uri = self._get_solutions_uri()
        result = self.client.get(uri)
        if not result.has_error and result.content:
            return result.content

    def get_branch(self, name, solution_name):
        uri = self._get_branch_uri(name, solution_name)
        result = self.client.get(uri)
        if not result.has_error and result.content:
            return result.content[0]

    def _get_branch_uri(self, name, solution_name):
        return f'{self.base_uri}branch/{solution_name}/{name}'

    def _get_solutions_uri(self):
        return '{}solution/'.format(self.base_uri)

    def _get_solution_byid_uri(self, solution_id):
        return '{}solution/{}/'.format(self.base_uri, solution_id)

    def _get_solution_byname_uri(self, solution):
        return '{}solution/byname/{}'.format(self.base_uri, solution)

    def _get_active_reprocess_bysolutionid_uri(self, solution):
        return '{}reprocess/actives/bysolutionid/{}'.format(self.base_uri, solution)

    def _get_active_reproduction_bysolutionid_uri(self, solution):
        return '{}reproduction/actives/bysolutionid/{}'.format(self.base_uri, solution)
    
    def _get_reproduction_status_byreproductionid_uri(self, reproductionId):
        return '{}reproduction/status/byreproductionid/{}'.format(self.base_uri, reproductionId)

    def _get_uri(self, _map, _version, _type):
        return '{}entitymap/{}/{}/{}'.format(self.base_uri, _map, _version, _type)

    def _get_reprocessable_tables_grouped_by_tags_uri(self):
        return f'{self.base_uri}appversion/byreprocessableentities'

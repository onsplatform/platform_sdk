from platform_sdk.utils.http import HttpClient


class DomainReaderApi:
    def __init__(self, settings):
        self.base_uri = settings['api_url']
        self.client = HttpClient()

    def get_map_entities(self, _map, _version, _type, _filter, _params):
        uri = self._mount_uri(_map, _version, _type, _filter)
        response = self.client.post(uri, _params)

        if not response.has_error:
            return response.content
    
    def instances_which_queries_would_find_any_touched_entity(self, entities, filters):
        uri = self._get_instances_which_queries_would_find_any_touched_entity_uri()
        request = {'entities': entities, 'filters': filters}
        response = self.client.post(uri, request)

    def _mount_uri(self, _map, _version, _type, _filter):
        return '{}{}/{}/{}/{}'.format(self.base_uri, _map, _version, _type, _filter)
        
    def _get_instances_which_queries_would_find_any_touched_entity_uri(self):
        return '{}{}'.format(self.base_uri, 'instanceswhichquerieswouldreturnentity')

    

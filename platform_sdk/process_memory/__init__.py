from platform_sdk.utils.http import *


class GetWithEntitiesType():
    def __init__(self):
        self.entities = []

    def add(self, id=None, type=None, timestamp=None):
        self.entities.append(
            {
                'id': id,
                'type': type,
                'timestamp': timestamp
            }
        )

    def get_body(self):
        return {
            'entities': self.entities
        }


class ProcessMemoryApi():
    def __init__(self, process_memory_settings):
        self.url_process_memory_api = process_memory_settings['api_url']
        self.client = HttpClient()

    def get_process_memory_data(self, process_memory_id):
        response = self.client.get(self._get_head_url(process_memory_id))

        if not response.has_error:
            return response.content

    def get_payload(self, process_memory_id):
        response = self.client.get(self._get_payload_url(process_memory_id))

        if not response.has_error:
            return response.content

    def get_maps(self, process_memory_id):
        response = self.client.get(self._get_maps_url(process_memory_id))

        if not response.has_error:
            return response.content

    def get_entities(self, process_memory_id):
        response = self.client.get(self._get_entities_url(process_memory_id))

        if not response.has_error:
            return response.content

    def get_using_entities(self, entities: GetWithEntitiesType):
        response = self.client.post(self._get_using_entities_url(), entities.get_body())

        if not response.has_error:
            return response.content

    def get_with_entities_type(self, entities: GetWithEntitiesType):
        response = self.client.post(self._get_with_entities_type_url(), entities.get_body())

        if not response.has_error:
            return response.content

    def _get_head_url(self, process_memory_id):
        return self.url_process_memory_api + '%s/head' % process_memory_id

    def _get_payload_url(self, process_memory_id):
        return self.url_process_memory_api + 'payload/%s' % process_memory_id

    def _get_maps_url(self, process_memory_id):
        return self.url_process_memory_api + 'maps/%s' % process_memory_id

    def _get_entities_url(self, process_memory_id):
        return self.url_process_memory_api + 'entities/%s' % process_memory_id

    def _get_with_entities_type_url(self):
        return self.url_process_memory_api + 'entities/with/type'

    def _get_using_entities_url(self):
        return self.url_process_memory_api + 'entities/with/ids'

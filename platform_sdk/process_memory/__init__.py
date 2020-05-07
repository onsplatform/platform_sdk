from platform_sdk.utils.http import *


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

    def get_event(self, process_memory_id):
        response = self.client.get(self._get_event_url(process_memory_id))

        if not response.has_error:
            return response.content

    def get_instance_filter(self, process_memory_id):
        response = self.client.get(
            self._get_instance_filter_url(process_memory_id))
        if not response.has_error:
            return response.content

    def get_instance_filters_by_instance_ids(self, instace_ids):
        response = self.client.post(self._get_instance_filter_by_instance_ids_url(),
                                    {'instance_ids': instace_ids})
        if not response.has_error:
            return response.content

    def get_entities(self, process_memory_id):
        response = self.client.get(self._get_entities_url(process_memory_id))

        if not response.has_error:
            return response.content
      
    def get_instance_filters_by_instance_ids_and_types(self, instances_and_types):
        response = self.client.post(self._get_instance_filters_by_instance_ids_and_types_url(),
                                    {'instances_and_types': instances_and_types})
        if not response.has_error:
            return response.content

    def get_using_entities(self, entities):
        response = self.client.post(self._get_using_entities_url(), entities)

        if not response.has_error:
            return response.content

    def get_by_tags(self, tags):
        request = {
            'tables_grouped_by_tags': tags
        }

        response = self.client.post(self._get_by_tags_url(), request)

        if not response.has_error:
            return response.content

    def get_events_between_dates(self, process_id, date_begin_validity, date_end_validity):
        request = {
            'process_id': process_id,
            'date_begin_validity': date_begin_validity,
            'date_end_validity': date_end_validity
        }
        response = self.client.post(self._get_between_dates_url(), request)

        if not response.has_error:
            return response.content

    def _get_between_dates_url(self):
        return self.url_process_memory_api + 'events/between/dates'

    def _get_head_url(self, process_memory_id):
        return self.url_process_memory_api + '%s/head' % process_memory_id

    def _get_payload_url(self, process_memory_id):
        return self.url_process_memory_api + 'payload/%s' % process_memory_id

    def _get_maps_url(self, process_memory_id):
        return self.url_process_memory_api + 'maps/%s' % process_memory_id

    def _get_entities_url(self, process_memory_id):
        return self.url_process_memory_api + 'entities/%s' % process_memory_id

    def _get_event_url(self, process_memory_id):
        return self.url_process_memory_api + 'event/%s' % process_memory_id

    def _get_instance_filter_url(self, process_memory_id):
        return self.url_process_memory_api + 'instance_filter/%s' % process_memory_id

    def _get_instance_filter_by_instance_ids_url(self):
        return self.url_process_memory_api + 'instance_filters/byinstanceids'

    def _get_by_tags_url(self):
        return self.url_process_memory_api + 'instances/bytags'

    def _get_using_entities_url(self):
        return self.url_process_memory_api + 'instances/reprocessable/byentities'
            
    def _get_instance_filters_by_instance_ids_and_types_url(self):
        return self.url_process_memory_api + 'instance_filters/byinstanceidsandtypes' 
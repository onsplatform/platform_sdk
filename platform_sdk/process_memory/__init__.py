import requests


class ProcessMemoryApi():
    def __init__(self, process_memory_settings):
        self.url_process_memory_api = process_memory_settings['api_url']

    def get_process_memory_data(self, process_memory_id):
        api_response = self._get_process_memory_response(process_memory_id)
        if api_response:
            return api_response.json()

    def _get_process_memory_response(self, process_memory_id):
        response = requests.get(
            self._get_process_memory_api_url(process_memory_id))

        if response.ok:
            return response

        raise Exception('http error')

    def _get_process_memory_api_url(self, process_memory_id):
        return self.url_process_memory_api + '%s/head' % process_memory_id

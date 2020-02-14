from platform_sdk.utils.http import HttpClient


class EventManager:
    def __init__(self, settings):
        self.base_uri = settings['api_url']
        self.client = HttpClient()

    def send_event(self, event):
        uri = '{}{}'.format(self.base_uri, 'sendevent')
        response = self.client.put(uri, event)

        if not response.has_error:
            return response.content

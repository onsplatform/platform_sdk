import json
import requests
import datetime


class HttpRequestResult:
    def __init__(self, has_error=False, content=None, error_message=None):
        self.has_error = has_error
        self.error_message = error_message
        self.content = content

    @classmethod
    def error(cls, message, content=None):
        return cls(has_error=True, error_message=message, content=content)

    @classmethod
    def success(cls, content):
        return cls(content=content)


class HttpClient:
    @classmethod
    def execute(cls, func, *args, **kwargs):
        try:
            response = func(*args, timeout=100, **kwargs)
            response.raise_for_status()
            return HttpRequestResult.success(content=response.json())

        except requests.exceptions.HTTPError as err:
            return HttpRequestResult.error(content=err, message='Http Error')

        except requests.exceptions.ConnectionError as err:
            return HttpRequestResult.error(content=err, message='Connection Error')

        except requests.exceptions.Timeout as err:
            return HttpRequestResult.error(content=err, message='Connection timed out.')

        except requests.exceptions.RequestException as err:
            return HttpRequestResult.error(content=err, message='Generic Error')

    @classmethod
    def get(self, uri, params=None):
        if params is not None:
            return self.execute(requests)
        return self.execute(requests.get, uri)

    @classmethod
    def post(self, url, body):
        return self.execute(func=requests.post, url=url, data=json.dumps(body, default=self.converter))

    @classmethod
    def put(self, url, body):
        headers = {'content-type': 'application/json'}
        return self.execute(func=requests.put, url=url, data=json.dumps(body, default=self.converter), headers=headers)

    def converter(o):
        if isinstance(o, datetime.datetime):
            return o.__str__()

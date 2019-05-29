import requests


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
            response = func(*args, timeout=3, **kwargs)
            return HttpRequestResult.success(content=response.json())

        except requests.exceptions.HTTPError as err:
            return HttpRequestResult.error(content=err, message='Http Error')

        except requests.exceptions.ConnectionError as err:
            return HttpRequestResult.error(content=err, message='Connection Error')

        except requests.exceptions.Timeout as err:
            return HttpRequestResult.error(content=err, message='Connection timed out.')

        except requests.exceptions.RequestException as err:
            return HttpRequestResult.error(content=err, message='Generic Error')

    def get(self, uri):
        return self.execute(requests.get, uri)

    # TODO: implement post and put.

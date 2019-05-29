from platform_sdk.utils.http import HttpClient, HttpRequestResult


class TestHttpRequestResult:
    def test_create_success_result(self):
        # act
        ret = HttpRequestResult.success(content='Foo bar')

        # assert
        assert not ret.has_error
        assert ret.content == 'Foo bar'

    def test_create_error_result(self):
        # act
        ret = HttpRequestResult.error(message='Error', content='Foo bar')

        # assert
        assert ret.has_error
        assert ret.error_message == 'Error'
        assert ret.content == 'Foo bar'


class TestHttpClient:
    def test_get_json_response(self):
        # act
        client = HttpClient()
        result = client.get('http://ip.jsontest.com/')

        # assert
        assert not result.has_error
        assert 'ip' in result.content









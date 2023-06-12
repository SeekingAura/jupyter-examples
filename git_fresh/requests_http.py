import requests
import requests_mock


class RequestHttp:
    def __init__(
        self,
        http_adapter: requests_mock.Adapter = None,
    ):
        self.http_session = requests.Session()
        if http_adapter:
            self.http_session.mount("https://", http_adapter)

    def set_http_adapter(self, http_adapter: requests_mock.Adapter):
        self.http_session.mount("https://", http_adapter)

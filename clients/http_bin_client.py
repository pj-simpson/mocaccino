import typing

import httpx


class HttpBinClient:
    def __init__(self):
        self.base_url = f"https://httpbin.org"

    def _do_http_bin_request(
        self, path: str, method: str, body: typing.Any = None
    ) -> typing.Dict:
        url = httpx.URL(path=path)

        with httpx.Client(
            base_url=self.base_url
        ) as http_client:
            
            response = http_client.request(
                url=url, method=method, json=body
            )
            print(type(response))
            response.raise_for_status()
        return response.json()

    def get_uuid_from_httpbin(
        self,
    ) -> str:
        path = f"/uuid"
        response = self._do_http_bin_request(path, "GET")
        print(type(response))
        return response["uuid"]

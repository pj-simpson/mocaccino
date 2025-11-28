from clients.http_bin_client import HttpBinClient
from unittest.mock import patch,Mock

import pytest

UUID_CONST = "05246485-d2a9-4eeb-ab00-6329d1b6f2d7"

class StubUUIDResponse:

    counter ={
        "raise_for_status": 0,
        "json":0
    }
    
    def __call__(self,*args,**kwargs):
        return self
    
    def raise_for_status(self):
        self.counter["raise_for_status"] += 1
        pass

    def json(self):
        self.counter["json"] += 1
        return {'uuid': UUID_CONST}

@patch("clients.http_bin_client.httpx.Client.request",new_callable=StubUUIDResponse)
def test_httpbin_uuid_with_patch_and_new_callable(stub_client_response):
    httpbin_client = HttpBinClient()
    api_response = httpbin_client._do_http_bin_request("/uuid", "GET")
    assert api_response['uuid'] == UUID_CONST
    assert stub_client_response.counter["raise_for_status"] == 1
    assert stub_client_response.counter["json"] == 1
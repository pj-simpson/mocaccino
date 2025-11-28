from clients.http_bin_client import HttpBinClient

import pytest

UUID_CONST = "05246485-d2a9-4eeb-ab00-6329d1b6f2d7"

class StubUUIDResponse:
    def raise_for_status(self):
        pass

    def json(self):
        return {'uuid': UUID_CONST}

@pytest.fixture
def get_stub_uuid():
    def return_stub_uuid(*args,**kwargs):
        return StubUUIDResponse()
    return return_stub_uuid


def test_httpbin_uuid_with_monkeypatch_and_stub(monkeypatch,get_stub_uuid):
        
    monkeypatch.setattr("httpx.Client.request", get_stub_uuid)
    httpbin_client = HttpBinClient()
    random_uuid = httpbin_client.get_uuid_from_httpbin()
    assert random_uuid == UUID_CONST
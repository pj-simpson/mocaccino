from clients.http_bin_client import HttpBinClient

import pytest

UUID_CONST = "05246485-d2a9-4eeb-ab00-6329d1b6f2d7"

@pytest.fixture
def uuid_return_value():
    return {"uuid": UUID_CONST}

def test_httpbin_uuid_with_mock(mocker,uuid_return_value):
    httpbin_client = HttpBinClient()
    httpbin_client._do_http_bin_request = mocker.Mock(return_value=uuid_return_value)
    random_uuid = httpbin_client.get_uuid_from_httpbin()
    assert random_uuid == UUID_CONST
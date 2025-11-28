from clients.http_bin_client import HttpBinClient
from unittest.mock import Mock

import pytest
import uuid

# test the client's public get_uuid api, by Mocking the private method'

UUID_CONST = "05246485-d2a9-4eeb-ab00-6329d1b6f2d7"

def test_httpbin_uuid_with_mock():
    httpbin_client = HttpBinClient()
    httpbin_client._do_http_bin_request = Mock(return_value={
        "uuid": UUID_CONST
        })
    uuid = httpbin_client.get_uuid_from_httpbin()
    assert uuid == UUID_CONST
    httpbin_client._do_http_bin_request.assert_called_once_with("/uuid","GET")
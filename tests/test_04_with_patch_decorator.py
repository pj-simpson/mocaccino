from clients.http_bin_client import HttpBinClient
from unittest.mock import patch,Mock

import pytest

UUID_CONST = "05246485-d2a9-4eeb-ab00-6329d1b6f2d7"

# patch the httpx library's client with a magic mock
# access the magic mock returned by the context managed class
# use a dict and arbitrary kwargs to define the Response's Mock return values

@patch("clients.http_bin_client.httpx.Client")
def test_httpbin_uuid_with_patch_decorator(mock_client_class):
    mocked_context_managed_client = mock_client_class.return_value.__enter__.return_value
    http_response_methods = {'raise_for_status.return_value': None, 'json.return_value': {'uuid': UUID_CONST}}
    mocked_context_managed_client.request.return_value = Mock(**http_response_methods)
    
    httpbin_client = HttpBinClient()
    api_response = httpbin_client._do_http_bin_request("/uuid", "GET")
    assert api_response['uuid'] == UUID_CONST
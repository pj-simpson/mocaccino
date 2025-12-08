from clients.http_bin_client import HttpBinClient
from unittest.mock import MagicMock, patch

import pytest
import uuid

# test the client's public get_uuid api, Mock at the most stable external boundary.

UUID_CONST = "05246485-d2a9-4eeb-ab00-6329d1b6f2d7"

@patch("clients.http_bin_client.httpx.Client.request")
def test_httpbin_uuid_with_mock_at_most_stable_external_boundary(mocked_request):
    
    #arrange
    # Create a mock response object
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {'uuid': UUID_CONST}
    
    # Make the request method return the mock response
    mocked_request.return_value = mock_response
    
    httpbin_client = HttpBinClient()

    #act
    uuid = httpbin_client.get_uuid_from_httpbin()

    #assert
    assert uuid == UUID_CONST
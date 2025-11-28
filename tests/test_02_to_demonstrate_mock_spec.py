from clients.http_bin_client import HttpBinClient
from unittest.mock import Mock

import pytest

# use the Mock's spec to ensure it can pass type-based assertions

def test_to_demonstrate_mock_spec():
    httpbin_client_mock = Mock(spec=HttpBinClient)
    assert isinstance(httpbin_client_mock,HttpBinClient)
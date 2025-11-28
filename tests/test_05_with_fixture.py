# from clients.http_bin_client import HttpBinClient

# import pytest
# import uuid

# @pytest.fixture
# def bin_client_for_test():
#     return HttpBinClient()

# def test_httpbin_uuid_with_real_network_call_fixture_demo(bin_client_for_test):
#     random_uuid = bin_client_for_test.get_uuid_from_httpbin()
#     parsed_uuid = uuid.UUID(random_uuid)
#     assert type(parsed_uuid) is uuid.UUID
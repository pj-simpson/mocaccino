# from clients.http_bin_client import HttpBinClient

# import pytest
# import uuid

# # test the client by actually making the network call

# def test_httpbin_uuid_with_real_network_call():
#     httpbin_client = HttpBinClient()
#     random_uuid = httpbin_client.get_uuid_from_httpbin()
#     parsed_uuid = uuid.UUID(random_uuid)
#     assert type(parsed_uuid) is uuid.UUID
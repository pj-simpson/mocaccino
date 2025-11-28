from clients.http_bin_client import HttpBinClient

if __name__ == "__main__":
    httpbin_client = HttpBinClient()
    random_uuid = httpbin_client.get_uuid_from_httpbin()
    print(f"The httpbin utility generated the following GUID {random_uuid}")

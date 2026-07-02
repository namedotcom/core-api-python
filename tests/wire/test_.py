from .conftest import get_client, verify_request_count


def test__hello() -> None:
    """Test Hello endpoint with WireMock"""
    test_id = "hello.0"
    client = get_client(test_id)
    client.hello()
    verify_request_count(test_id, "GET", "/core/v1/hello", None, 1)

from .conftest import get_client, verify_request_count


def test_urlForwardings_list_url_forwardings() -> None:
    """Test ListURLForwardings endpoint with WireMock"""
    test_id = "url_forwardings.list_url_forwardings.0"
    client = get_client(test_id)
    client.url_forwardings.list_url_forwardings(
        domain_name="example.com",
        per_page=100,
        page=1,
    )
    verify_request_count(
        test_id, "GET", "/core/v1/domains/example.com/url/forwarding", {"perPage": "100", "page": "1"}, 1
    )


def test_urlForwardings_create_url_forwarding() -> None:
    """Test CreateURLForwarding endpoint with WireMock"""
    test_id = "url_forwardings.create_url_forwarding.0"
    client = get_client(test_id)
    client.url_forwardings.create_url_forwarding(
        domain_name="example.com",
        forwards_to="https://destination-site.com",
        host="www",
        type="masked",
    )
    verify_request_count(test_id, "POST", "/core/v1/domains/example.com/url/forwarding", None, 1)


def test_urlForwardings_get_url_forwarding() -> None:
    """Test GetURLForwarding endpoint with WireMock"""
    test_id = "url_forwardings.get_url_forwarding.0"
    client = get_client(test_id)
    client.url_forwardings.get_url_forwarding(
        domain_name="example.com",
        host="www.example.org",
    )
    verify_request_count(test_id, "GET", "/core/v1/domains/example.com/url/forwarding/www.example.org", None, 1)


def test_urlForwardings_update_url_forwarding() -> None:
    """Test UpdateURLForwarding endpoint with WireMock"""
    test_id = "url_forwardings.update_url_forwarding.0"
    client = get_client(test_id)
    client.url_forwardings.update_url_forwarding(
        domain_name="example.com",
        host_="www.example.org",
    )
    verify_request_count(test_id, "PUT", "/core/v1/domains/example.com/url/forwarding/www.example.org", None, 1)


def test_urlForwardings_delete_url_forwarding() -> None:
    """Test DeleteURLForwarding endpoint with WireMock"""
    test_id = "url_forwardings.delete_url_forwarding.0"
    client = get_client(test_id)
    client.url_forwardings.delete_url_forwarding(
        domain_name="example.com",
        host="www.example.org",
    )
    verify_request_count(test_id, "DELETE", "/core/v1/domains/example.com/url/forwarding/www.example.org", None, 1)


def test_urlForwardings_list_url_forwardings_by_domain() -> None:
    """Test ListURLForwardingsByDomain endpoint with WireMock"""
    test_id = "url_forwardings.list_url_forwardings_by_domain.0"
    client = get_client(test_id)
    client.url_forwardings.list_url_forwardings_by_domain(
        domain_name="example.com",
        per_page=100,
        page=1,
    )
    verify_request_count(test_id, "GET", "/core/v1/urlforwarding/example.com", {"perPage": "100", "page": "1"}, 1)


def test_urlForwardings_get_url_forwarding_by_id() -> None:
    """Test GetURLForwardingById endpoint with WireMock"""
    test_id = "url_forwardings.get_url_forwarding_by_id.0"
    client = get_client(test_id)
    client.url_forwardings.get_url_forwarding_by_id(
        domain_name="example.com",
        id=12345,
    )
    verify_request_count(test_id, "GET", "/core/v1/urlforwarding/example.com/12345", None, 1)


def test_urlForwardings_delete_url_forwarding_by_id() -> None:
    """Test DeleteURLForwardingById endpoint with WireMock"""
    test_id = "url_forwardings.delete_url_forwarding_by_id.0"
    client = get_client(test_id)
    client.url_forwardings.delete_url_forwarding_by_id(
        domain_name="example.com",
        id=12345,
    )
    verify_request_count(test_id, "DELETE", "/core/v1/urlforwarding/example.com/12345", None, 1)


def test_urlForwardings_update_url_forwarding_by_id() -> None:
    """Test UpdateURLForwardingById endpoint with WireMock"""
    test_id = "url_forwardings.update_url_forwarding_by_id.0"
    client = get_client(test_id)
    client.url_forwardings.update_url_forwarding_by_id(
        domain_name="example.com",
        id=12345,
    )
    verify_request_count(test_id, "PATCH", "/core/v1/urlforwarding/example.com/12345", None, 1)

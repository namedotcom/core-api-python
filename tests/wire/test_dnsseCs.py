from .conftest import get_client, verify_request_count


def test_dnsseCs_list_dnsse_cs() -> None:
    """Test ListDNSSECs endpoint with WireMock"""
    test_id = "dnsse_cs.list_dnsse_cs.0"
    client = get_client(test_id)
    client.dnsse_cs.list_dnsse_cs(
        domain_name="domainName",
    )
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/dnssec", None, 1)


def test_dnsseCs_create_dnssec() -> None:
    """Test CreateDNSSEC endpoint with WireMock"""
    test_id = "dnsse_cs.create_dnssec.0"
    client = get_client(test_id)
    client.dnsse_cs.create_dnssec(
        domain_name="domainName",
        algorithm=1,
        digest="digest",
        digest_type=1,
        key_tag=1,
    )
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/dnssec", None, 1)


def test_dnsseCs_get_dnssec() -> None:
    """Test GetDNSSEC endpoint with WireMock"""
    test_id = "dnsse_cs.get_dnssec.0"
    client = get_client(test_id)
    client.dnsse_cs.get_dnssec(
        domain_name="domainName",
        digest="digest",
    )
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/dnssec/digest", None, 1)


def test_dnsseCs_delete_dnssec() -> None:
    """Test DeleteDNSSEC endpoint with WireMock"""
    test_id = "dnsse_cs.delete_dnssec.0"
    client = get_client(test_id)
    client.dnsse_cs.delete_dnssec(
        domain_name="domainName",
        digest="digest",
    )
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/dnssec/digest", None, 1)

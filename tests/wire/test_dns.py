from .conftest import get_client, verify_request_count


def test_dns_list_records() -> None:
    """Test ListRecords endpoint with WireMock"""
    test_id = "dns.list_records.0"
    client = get_client(test_id)
    client.dns.list_records(
        domain_name="domainName",
    )
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/records", None, 1)


def test_dns_create_record() -> None:
    """Test CreateRecord endpoint with WireMock"""
    test_id = "dns.create_record.0"
    client = get_client(test_id)
    client.dns.create_record(
        domain_name="domainName",
        answer="answer",
        host="host",
        type="A",
    )
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/records", None, 1)


def test_dns_get_record() -> None:
    """Test GetRecord endpoint with WireMock"""
    test_id = "dns.get_record.0"
    client = get_client(test_id)
    client.dns.get_record(
        domain_name="domainName",
        id=1,
    )
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_update_record() -> None:
    """Test UpdateRecord endpoint with WireMock"""
    test_id = "dns.update_record.0"
    client = get_client(test_id)
    client.dns.update_record(
        domain_name="domainName",
        id=1,
        answer="answer",
        type="A",
    )
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_delete_record() -> None:
    """Test DeleteRecord endpoint with WireMock"""
    test_id = "dns.delete_record.0"
    client = get_client(test_id)
    client.dns.delete_record(
        domain_name="domainName",
        id=1,
    )
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/records/1", None, 1)

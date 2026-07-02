from .conftest import get_client, verify_request_count


def test_vanityNameservers_list_vanity_nameservers() -> None:
    """Test ListVanityNameservers endpoint with WireMock"""
    test_id = "vanity_nameservers.list_vanity_nameservers.0"
    client = get_client(test_id)
    client.vanity_nameservers.list_vanity_nameservers(
        domain_name="example.com",
        per_page=50,
        page=2,
    )
    verify_request_count(
        test_id, "GET", "/core/v1/domains/example.com/vanity_nameservers", {"perPage": "50", "page": "2"}, 1
    )


def test_vanityNameservers_create_vanity_nameserver() -> None:
    """Test CreateVanityNameserver endpoint with WireMock"""
    test_id = "vanity_nameservers.create_vanity_nameserver.0"
    client = get_client(test_id)
    client.vanity_nameservers.create_vanity_nameserver(
        domain_name="example.com",
        hostname="ns1",
        ips=["192.168.1.10", "2001:0db8:85a3:0000:0000:8a2e:0370:7334"],
    )
    verify_request_count(test_id, "POST", "/core/v1/domains/example.com/vanity_nameservers", None, 1)


def test_vanityNameservers_get_vanity_nameserver() -> None:
    """Test GetVanityNameserver endpoint with WireMock"""
    test_id = "vanity_nameservers.get_vanity_nameserver.0"
    client = get_client(test_id)
    client.vanity_nameservers.get_vanity_nameserver(
        domain_name="example.com",
        hostname="ns1.example.com",
    )
    verify_request_count(test_id, "GET", "/core/v1/domains/example.com/vanity_nameservers/ns1.example.com", None, 1)


def test_vanityNameservers_update_vanity_nameserver() -> None:
    """Test UpdateVanityNameserver endpoint with WireMock"""
    test_id = "vanity_nameservers.update_vanity_nameserver.0"
    client = get_client(test_id)
    client.vanity_nameservers.update_vanity_nameserver(
        domain_name="example.com",
        hostname="ns1.example.com",
    )
    verify_request_count(test_id, "PUT", "/core/v1/domains/example.com/vanity_nameservers/ns1.example.com", None, 1)


def test_vanityNameservers_delete_vanity_nameserver() -> None:
    """Test DeleteVanityNameserver endpoint with WireMock"""
    test_id = "vanity_nameservers.delete_vanity_nameserver.0"
    client = get_client(test_id)
    client.vanity_nameservers.delete_vanity_nameserver(
        domain_name="example.com",
        hostname="ns1.example.com",
    )
    verify_request_count(test_id, "DELETE", "/core/v1/domains/example.com/vanity_nameservers/ns1.example.com", None, 1)

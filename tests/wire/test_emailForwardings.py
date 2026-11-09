from .conftest import get_client, verify_request_count


def test_emailForwardings_list_email_forwardings() -> None:
    """Test ListEmailForwardings endpoint with WireMock"""
    test_id = "email_forwardings.list_email_forwardings.0"
    client = get_client(test_id)
    client.email_forwardings.list_email_forwardings(
        domain_name="domainName",
        per_page=100,
        page=1,
    )
    verify_request_count(
        test_id, "GET", "/core/v1/domains/domainName/email/forwarding", {"perPage": "100", "page": "1"}, 1
    )


def test_emailForwardings_create_email_forwarding() -> None:
    """Test CreateEmailForwarding endpoint with WireMock"""
    test_id = "email_forwardings.create_email_forwarding.0"
    client = get_client(test_id)
    client.email_forwardings.create_email_forwarding(
        domain_name="example.com",
        email_box="admin",
        email_to="webmaster@example.com",
    )
    verify_request_count(test_id, "POST", "/core/v1/domains/example.com/email/forwarding", None, 1)


def test_emailForwardings_get_email_forwarding() -> None:
    """Test GetEmailForwarding endpoint with WireMock"""
    test_id = "email_forwardings.get_email_forwarding.0"
    client = get_client(test_id)
    client.email_forwardings.get_email_forwarding(
        domain_name="domainName",
        email_box="emailBox",
    )
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_update_email_forwarding() -> None:
    """Test UpdateEmailForwarding endpoint with WireMock"""
    test_id = "email_forwardings.update_email_forwarding.0"
    client = get_client(test_id)
    client.email_forwardings.update_email_forwarding(
        domain_name="domainName",
        email_box="emailBox",
        email_to="emailTo",
    )
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_delete_email_forwarding() -> None:
    """Test DeleteEmailForwarding endpoint with WireMock"""
    test_id = "email_forwardings.delete_email_forwarding.0"
    client = get_client(test_id)
    client.email_forwardings.delete_email_forwarding(
        domain_name="domainName",
        email_box="emailBox",
    )
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)

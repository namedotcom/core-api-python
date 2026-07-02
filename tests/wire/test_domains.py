from .conftest import get_client, verify_request_count

from namecom_core_api import DomainCreatePayload
from namecom_core_api.domains import UpdateDomainRequestBodyAutorenewEnabled


def test_domains_list_domains() -> None:
    """Test ListDomains endpoint with WireMock"""
    test_id = "domains.list_domains.0"
    client = get_client(test_id)
    client.domains.list_domains()
    verify_request_count(test_id, "GET", "/core/v1/domains", None, 1)


def test_domains_create_domain() -> None:
    """Test CreateDomain endpoint with WireMock"""
    test_id = "domains.create_domain.0"
    client = get_client(test_id)
    client.domains.create_domain(
        idempotency_key="083910ef-04e4-4bd1-a0bf-3737fe005ca8",
        domain=DomainCreatePayload(
            domain_name="example.com",
        ),
    )
    verify_request_count(test_id, "POST", "/core/v1/domains", None, 1)


def test_domains_get_domain() -> None:
    """Test GetDomain endpoint with WireMock"""
    test_id = "domains.get_domain.0"
    client = get_client(test_id)
    client.domains.get_domain(
        domain_name="example.com",
    )
    verify_request_count(test_id, "GET", "/core/v1/domains/example.com", None, 1)


def test_domains_update_domain() -> None:
    """Test UpdateDomain endpoint with WireMock"""
    test_id = "domains.update_domain.0"
    client = get_client(test_id)
    client.domains.update_domain(
        domain_name="domainName",
        request=UpdateDomainRequestBodyAutorenewEnabled(
            autorenew_enabled=True,
        ),
    )
    verify_request_count(test_id, "PATCH", "/core/v1/domains/domainName", None, 1)


def test_domains_disable_autorenew() -> None:
    """Test DisableAutorenew endpoint with WireMock"""
    test_id = "domains.disable_autorenew.0"
    client = get_client(test_id)
    client.domains.disable_autorenew(
        domain_name="example.com",
    )
    verify_request_count(test_id, "POST", "/core/v1/domains/example.com:disableAutorenew", None, 1)


def test_domains_disable_whois_privacy() -> None:
    """Test DisableWhoisPrivacy endpoint with WireMock"""
    test_id = "domains.disable_whois_privacy.0"
    client = get_client(test_id)
    client.domains.disable_whois_privacy(
        domain_name="example.com",
    )
    verify_request_count(test_id, "POST", "/core/v1/domains/example.com:disableWhoisPrivacy", None, 1)


def test_domains_enable_autorenew() -> None:
    """Test EnableAutorenew endpoint with WireMock"""
    test_id = "domains.enable_autorenew.0"
    client = get_client(test_id)
    client.domains.enable_autorenew(
        domain_name="example.com",
    )
    verify_request_count(test_id, "POST", "/core/v1/domains/example.com:enableAutorenew", None, 1)


def test_domains_enable_whois_privacy() -> None:
    """Test EnableWhoisPrivacy endpoint with WireMock"""
    test_id = "domains.enable_whois_privacy.0"
    client = get_client(test_id)
    client.domains.enable_whois_privacy(
        domain_name="domainName",
    )
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:enableWhoisPrivacy", None, 1)


def test_domains_get_auth_code_for_domain() -> None:
    """Test GetAuthCodeForDomain endpoint with WireMock"""
    test_id = "domains.get_auth_code_for_domain.0"
    client = get_client(test_id)
    client.domains.get_auth_code_for_domain(
        domain_name="domainName",
    )
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName:getAuthCode", None, 1)


def test_domains_get_pricing_for_domain() -> None:
    """Test GetPricingForDomain endpoint with WireMock"""
    test_id = "domains.get_pricing_for_domain.0"
    client = get_client(test_id)
    client.domains.get_pricing_for_domain(
        domain_name="domainName",
        years=2,
    )
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName:getPricing", {"years": "2"}, 1)


def test_domains_lock_domain() -> None:
    """Test LockDomain endpoint with WireMock"""
    test_id = "domains.lock_domain.0"
    client = get_client(test_id)
    client.domains.lock_domain(
        domain_name="example.com",
    )
    verify_request_count(test_id, "POST", "/core/v1/domains/example.com:lock", None, 1)


def test_domains_purchase_privacy() -> None:
    """Test PurchasePrivacy endpoint with WireMock"""
    test_id = "domains.purchase_privacy.0"
    client = get_client(test_id)
    client.domains.purchase_privacy(
        domain_name="domainName",
        idempotency_key="083910ef-04e4-4bd1-a0bf-3737fe005ca8",
    )
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:purchasePrivacy", None, 1)


def test_domains_renew_domain() -> None:
    """Test RenewDomain endpoint with WireMock"""
    test_id = "domains.renew_domain.0"
    client = get_client(test_id)
    client.domains.renew_domain(
        domain_name="domainName",
    )
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:renew", None, 1)


def test_domains_set_contacts() -> None:
    """Test SetContacts endpoint with WireMock"""
    test_id = "domains.set_contacts.0"
    client = get_client(test_id)
    client.domains.set_contacts(
        domain_name="example.com",
    )
    verify_request_count(test_id, "POST", "/core/v1/domains/example.com:setContacts", None, 1)


def test_domains_set_nameservers() -> None:
    """Test SetNameservers endpoint with WireMock"""
    test_id = "domains.set_nameservers.0"
    client = get_client(test_id)
    client.domains.set_nameservers(
        domain_name="example.com",
        nameservers=["ns1.name.com", "ns2.name.com"],
    )
    verify_request_count(test_id, "POST", "/core/v1/domains/example.com:setNameservers", None, 1)


def test_domains_unlock_domain() -> None:
    """Test UnlockDomain endpoint with WireMock"""
    test_id = "domains.unlock_domain.0"
    client = get_client(test_id)
    client.domains.unlock_domain(
        domain_name="domainName",
    )
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:unlock", None, 1)


def test_domains_check_availability() -> None:
    """Test CheckAvailability endpoint with WireMock"""
    test_id = "domains.check_availability.0"
    client = get_client(test_id)
    client.domains.check_availability(
        domain_names=["domainNames"],
    )
    verify_request_count(test_id, "POST", "/core/v1/domains:checkAvailability", None, 1)


def test_domains_search() -> None:
    """Test Search endpoint with WireMock"""
    test_id = "domains.search.0"
    client = get_client(test_id)
    client.domains.search(
        keyword="mydomain",
    )
    verify_request_count(test_id, "POST", "/core/v1/domains:search", None, 1)


def test_domains_zone_check() -> None:
    """Test ZoneCheck endpoint with WireMock"""
    test_id = "domains.zone_check.0"
    client = get_client(test_id)
    client.domains.zone_check(
        domain_names=["example.com", "example.net", "example.org"],
    )
    verify_request_count(test_id, "POST", "/core/v1/zonecheck", None, 1)

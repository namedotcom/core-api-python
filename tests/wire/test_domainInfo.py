from .conftest import get_client, verify_request_count


def test_domainInfo_get_requirement() -> None:
    """Test GetRequirement endpoint with WireMock"""
    test_id = "domain_info.get_requirement.0"
    client = get_client(test_id)
    client.domain_info.get_requirement(
        tld="fr",
    )
    verify_request_count(test_id, "GET", "/core/v1/domaininfo/requirements/fr", None, 1)


def test_domainInfo_check_domain_claims() -> None:
    """Test CheckDomainClaims endpoint with WireMock"""
    test_id = "domain_info.check_domain_claims.0"
    client = get_client(test_id)
    client.domain_info.check_domain_claims(
        domain="tiktok.page",
    )
    verify_request_count(test_id, "POST", "/core/v1/domaininfo/claims/tiktok.page", None, 1)


def test_domainInfo_get_tld_requirements_v2() -> None:
    """Test GetTldRequirementsV2 endpoint with WireMock"""
    test_id = "domain_info.get_tld_requirements_v2.0"
    client = get_client(test_id)
    client.domain_info.get_tld_requirements_v2(
        tld="fr",
    )
    verify_request_count(test_id, "GET", "/core/v1/domaininfo/requirementsV2/fr", None, 1)

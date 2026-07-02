from .conftest import get_client, verify_request_count


def test_premiumDomains_premium_domain_lists() -> None:
    """Test PremiumDomainLists endpoint with WireMock"""
    test_id = "premium_domains.premium_domain_lists.0"
    client = get_client(test_id)
    client.premium_domains.premium_domain_lists()
    verify_request_count(test_id, "GET", "/core/v1/premiumdomainslist", None, 1)

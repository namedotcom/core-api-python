from .conftest import get_client, verify_request_count


def test_tldPricing_tld_price_list() -> None:
    """Test TldPriceList endpoint with WireMock"""
    test_id = "tld_pricing.tld_price_list.0"
    client = get_client(test_id)
    client.tld_pricing.tld_price_list(
        duration=1,
    )
    verify_request_count(test_id, "GET", "/core/v1/tldpricing", {"duration": "1"}, 1)

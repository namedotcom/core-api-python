import pytest
from .conftest import get_client, verify_request_count

from namecom_core_api import (
    BadGatewayError,
    ForbiddenError,
    GatewayTimeoutError,
    InternalServerError,
    MethodNotAllowedError,
    NotFoundError,
    ServiceUnavailableError,
    TooManyRequestsError,
    UnauthorizedError,
)
from namecom_core_api.core.jsonable_encoder import jsonable_encoder


def test_premiumDomains_premium_domain_lists() -> None:
    """Test PremiumDomainLists endpoint with WireMock"""
    test_id = "premium_domains.premium_domain_lists.0"
    client = get_client(test_id)
    client.premium_domains.premium_domain_lists()
    verify_request_count(test_id, "GET", "/core/v1/premiumdomainslist", None, 1)


def test_premiumDomains_premium_domain_lists_throws_unauthorized_error() -> None:
    """Test PremiumDomainLists endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "premium_domains.premium_domain_lists.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.premium_domains.premium_domain_lists()
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/premiumdomainslist", None, 1)


def test_premiumDomains_premium_domain_lists_throws_forbidden_error() -> None:
    """Test PremiumDomainLists endpoint error response (ForbiddenError) with WireMock"""
    test_id = "premium_domains.premium_domain_lists.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.premium_domains.premium_domain_lists()
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/premiumdomainslist", None, 1)


def test_premiumDomains_premium_domain_lists_throws_not_found_error() -> None:
    """Test PremiumDomainLists endpoint error response (NotFoundError) with WireMock"""
    test_id = "premium_domains.premium_domain_lists.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.premium_domains.premium_domain_lists()
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "GET", "/core/v1/premiumdomainslist", None, 1)


def test_premiumDomains_premium_domain_lists_throws_method_not_allowed_error() -> None:
    """Test PremiumDomainLists endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "premium_domains.premium_domain_lists.4"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.premium_domains.premium_domain_lists()
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/premiumdomainslist", None, 1)


def test_premiumDomains_premium_domain_lists_throws_too_many_requests_error() -> None:
    """Test PremiumDomainLists endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "premium_domains.premium_domain_lists.5"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.premium_domains.premium_domain_lists()
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/premiumdomainslist", None, 1)


def test_premiumDomains_premium_domain_lists_throws_internal_server_error() -> None:
    """Test PremiumDomainLists endpoint error response (InternalServerError) with WireMock"""
    test_id = "premium_domains.premium_domain_lists.6"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.premium_domains.premium_domain_lists()
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/premiumdomainslist", None, 1)


def test_premiumDomains_premium_domain_lists_throws_bad_gateway_error() -> None:
    """Test PremiumDomainLists endpoint error response (BadGatewayError) with WireMock"""
    test_id = "premium_domains.premium_domain_lists.7"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.premium_domains.premium_domain_lists()
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/premiumdomainslist", None, 1)


def test_premiumDomains_premium_domain_lists_throws_service_unavailable_error() -> None:
    """Test PremiumDomainLists endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "premium_domains.premium_domain_lists.8"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.premium_domains.premium_domain_lists()
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/premiumdomainslist", None, 1)


def test_premiumDomains_premium_domain_lists_throws_gateway_timeout_error() -> None:
    """Test PremiumDomainLists endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "premium_domains.premium_domain_lists.9"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.premium_domains.premium_domain_lists()
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/premiumdomainslist", None, 1)

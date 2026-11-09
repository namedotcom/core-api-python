import pytest
from .conftest import get_client, verify_request_count

from namecom_core_api import (
    BadGatewayError,
    BadRequestError,
    ForbiddenError,
    GatewayTimeoutError,
    InternalServerError,
    MethodNotAllowedError,
    ServiceUnavailableError,
    TooManyRequestsError,
    UnauthorizedError,
)
from namecom_core_api.core.jsonable_encoder import jsonable_encoder


def test_tldPricing_tld_price_list() -> None:
    """Test TldPriceList endpoint with WireMock"""
    test_id = "tld_pricing.tld_price_list.0"
    client = get_client(test_id)
    client.tld_pricing.tld_price_list(
        duration=1,
    )
    verify_request_count(test_id, "GET", "/core/v1/tldpricing", {"duration": "1"}, 1)


def test_tldPricing_tld_price_list_throws_bad_request_error() -> None:
    """Test TldPriceList endpoint error response (BadRequestError) with WireMock"""
    test_id = "tld_pricing.tld_price_list.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.tld_pricing.tld_price_list()
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/tldpricing", None, 1)


def test_tldPricing_tld_price_list_throws_unauthorized_error() -> None:
    """Test TldPriceList endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "tld_pricing.tld_price_list.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.tld_pricing.tld_price_list()
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/tldpricing", None, 1)


def test_tldPricing_tld_price_list_throws_forbidden_error() -> None:
    """Test TldPriceList endpoint error response (ForbiddenError) with WireMock"""
    test_id = "tld_pricing.tld_price_list.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.tld_pricing.tld_price_list()
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/tldpricing", None, 1)


def test_tldPricing_tld_price_list_throws_method_not_allowed_error() -> None:
    """Test TldPriceList endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "tld_pricing.tld_price_list.4"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.tld_pricing.tld_price_list()
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/tldpricing", None, 1)


def test_tldPricing_tld_price_list_throws_too_many_requests_error() -> None:
    """Test TldPriceList endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "tld_pricing.tld_price_list.5"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.tld_pricing.tld_price_list()
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/tldpricing", None, 1)


def test_tldPricing_tld_price_list_throws_internal_server_error() -> None:
    """Test TldPriceList endpoint error response (InternalServerError) with WireMock"""
    test_id = "tld_pricing.tld_price_list.6"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.tld_pricing.tld_price_list()
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/tldpricing", None, 1)


def test_tldPricing_tld_price_list_throws_bad_gateway_error() -> None:
    """Test TldPriceList endpoint error response (BadGatewayError) with WireMock"""
    test_id = "tld_pricing.tld_price_list.7"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.tld_pricing.tld_price_list()
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/tldpricing", None, 1)


def test_tldPricing_tld_price_list_throws_service_unavailable_error() -> None:
    """Test TldPriceList endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "tld_pricing.tld_price_list.8"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.tld_pricing.tld_price_list()
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/tldpricing", None, 1)


def test_tldPricing_tld_price_list_throws_gateway_timeout_error() -> None:
    """Test TldPriceList endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "tld_pricing.tld_price_list.9"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.tld_pricing.tld_price_list()
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/tldpricing", None, 1)

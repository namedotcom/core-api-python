import pytest
from .conftest import get_client, verify_request_count

from namecom_core_api import (
    BadGatewayError,
    ForbiddenError,
    GatewayTimeoutError,
    InternalServerError,
    MethodNotAllowedError,
    ServiceUnavailableError,
    TooManyRequestsError,
    UnauthorizedError,
)
from namecom_core_api.core.jsonable_encoder import jsonable_encoder


def test__hello() -> None:
    """Test Hello endpoint with WireMock"""
    test_id = "hello.0"
    client = get_client(test_id)
    client.hello()
    verify_request_count(test_id, "GET", "/core/v1/hello", None, 1)


def test__hello_throws_unauthorized_error() -> None:
    """Test Hello endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "hello.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.hello()
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/hello", None, 1)


def test__hello_throws_forbidden_error() -> None:
    """Test Hello endpoint error response (ForbiddenError) with WireMock"""
    test_id = "hello.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.hello()
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/hello", None, 1)


def test__hello_throws_method_not_allowed_error() -> None:
    """Test Hello endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "hello.3"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.hello()
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/hello", None, 1)


def test__hello_throws_too_many_requests_error() -> None:
    """Test Hello endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "hello.4"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.hello()
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/hello", None, 1)


def test__hello_throws_internal_server_error() -> None:
    """Test Hello endpoint error response (InternalServerError) with WireMock"""
    test_id = "hello.5"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.hello()
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/hello", None, 1)


def test__hello_throws_bad_gateway_error() -> None:
    """Test Hello endpoint error response (BadGatewayError) with WireMock"""
    test_id = "hello.6"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.hello()
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/hello", None, 1)


def test__hello_throws_service_unavailable_error() -> None:
    """Test Hello endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "hello.7"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.hello()
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/hello", None, 1)


def test__hello_throws_gateway_timeout_error() -> None:
    """Test Hello endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "hello.8"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.hello()
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/hello", None, 1)

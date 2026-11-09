import pytest
from .conftest import get_client, verify_request_count

from namecom_core_api import (
    BadGatewayError,
    BadRequestError,
    ConflictError,
    ForbiddenError,
    GatewayTimeoutError,
    InternalServerError,
    MethodNotAllowedError,
    NotFoundError,
    ServiceUnavailableError,
    TooManyRequestsError,
    UnauthorizedError,
    UnsupportedMediaTypeError,
)
from namecom_core_api.core.jsonable_encoder import jsonable_encoder


def test_urlForwardings_list_url_forwardings() -> None:
    """Test ListURLForwardings endpoint with WireMock"""
    test_id = "url_forwardings.list_url_forwardings.0"
    client = get_client(test_id)
    client.url_forwardings.list_url_forwardings(
        domain_name="example.com",
        per_page=100,
        page=1,
    )
    verify_request_count(
        test_id, "GET", "/core/v1/domains/example.com/url/forwarding", {"perPage": "100", "page": "1"}, 1
    )


def test_urlForwardings_list_url_forwardings_throws_bad_request_error() -> None:
    """Test ListURLForwardings endpoint error response (BadRequestError) with WireMock"""
    test_id = "url_forwardings.list_url_forwardings.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.url_forwardings.list_url_forwardings(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/url/forwarding", None, 1)


def test_urlForwardings_list_url_forwardings_throws_unauthorized_error() -> None:
    """Test ListURLForwardings endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "url_forwardings.list_url_forwardings.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.url_forwardings.list_url_forwardings(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/url/forwarding", None, 1)


def test_urlForwardings_list_url_forwardings_throws_forbidden_error() -> None:
    """Test ListURLForwardings endpoint error response (ForbiddenError) with WireMock"""
    test_id = "url_forwardings.list_url_forwardings.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.url_forwardings.list_url_forwardings(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/url/forwarding", None, 1)


def test_urlForwardings_list_url_forwardings_throws_not_found_error() -> None:
    """Test ListURLForwardings endpoint error response (NotFoundError) with WireMock"""
    test_id = "url_forwardings.list_url_forwardings.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.url_forwardings.list_url_forwardings(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/url/forwarding", None, 1)


def test_urlForwardings_list_url_forwardings_throws_method_not_allowed_error() -> None:
    """Test ListURLForwardings endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "url_forwardings.list_url_forwardings.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.url_forwardings.list_url_forwardings(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/url/forwarding", None, 1)


def test_urlForwardings_list_url_forwardings_throws_too_many_requests_error() -> None:
    """Test ListURLForwardings endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "url_forwardings.list_url_forwardings.6"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.url_forwardings.list_url_forwardings(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/url/forwarding", None, 1)


def test_urlForwardings_list_url_forwardings_throws_internal_server_error() -> None:
    """Test ListURLForwardings endpoint error response (InternalServerError) with WireMock"""
    test_id = "url_forwardings.list_url_forwardings.7"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.url_forwardings.list_url_forwardings(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/url/forwarding", None, 1)


def test_urlForwardings_list_url_forwardings_throws_bad_gateway_error() -> None:
    """Test ListURLForwardings endpoint error response (BadGatewayError) with WireMock"""
    test_id = "url_forwardings.list_url_forwardings.8"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.url_forwardings.list_url_forwardings(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/url/forwarding", None, 1)


def test_urlForwardings_list_url_forwardings_throws_service_unavailable_error() -> None:
    """Test ListURLForwardings endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "url_forwardings.list_url_forwardings.9"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.url_forwardings.list_url_forwardings(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/url/forwarding", None, 1)


def test_urlForwardings_list_url_forwardings_throws_gateway_timeout_error() -> None:
    """Test ListURLForwardings endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "url_forwardings.list_url_forwardings.10"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.url_forwardings.list_url_forwardings(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/url/forwarding", None, 1)


def test_urlForwardings_create_url_forwarding() -> None:
    """Test CreateURLForwarding endpoint with WireMock"""
    test_id = "url_forwardings.create_url_forwarding.0"
    client = get_client(test_id)
    client.url_forwardings.create_url_forwarding(
        domain_name="example.com",
        forwards_to="https://destination-site.com",
        host="www",
        type="masked",
    )
    verify_request_count(test_id, "POST", "/core/v1/domains/example.com/url/forwarding", None, 1)


def test_urlForwardings_create_url_forwarding_throws_bad_request_error() -> None:
    """Test CreateURLForwarding endpoint error response (BadRequestError) with WireMock"""
    test_id = "url_forwardings.create_url_forwarding.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.url_forwardings.create_url_forwarding(
            domain_name="domainName",
            forwards_to="forwardsTo",
            host="host",
            type="masked",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/url/forwarding", None, 1)


def test_urlForwardings_create_url_forwarding_throws_unauthorized_error() -> None:
    """Test CreateURLForwarding endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "url_forwardings.create_url_forwarding.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.url_forwardings.create_url_forwarding(
            domain_name="domainName",
            forwards_to="forwardsTo",
            host="host",
            type="masked",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/url/forwarding", None, 1)


def test_urlForwardings_create_url_forwarding_throws_forbidden_error() -> None:
    """Test CreateURLForwarding endpoint error response (ForbiddenError) with WireMock"""
    test_id = "url_forwardings.create_url_forwarding.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.url_forwardings.create_url_forwarding(
            domain_name="domainName",
            forwards_to="forwardsTo",
            host="host",
            type="masked",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/url/forwarding", None, 1)


def test_urlForwardings_create_url_forwarding_throws_not_found_error() -> None:
    """Test CreateURLForwarding endpoint error response (NotFoundError) with WireMock"""
    test_id = "url_forwardings.create_url_forwarding.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.url_forwardings.create_url_forwarding(
            domain_name="domainName",
            forwards_to="forwardsTo",
            host="host",
            type="masked",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/url/forwarding", None, 1)


def test_urlForwardings_create_url_forwarding_throws_method_not_allowed_error() -> None:
    """Test CreateURLForwarding endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "url_forwardings.create_url_forwarding.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.url_forwardings.create_url_forwarding(
            domain_name="domainName",
            forwards_to="forwardsTo",
            host="host",
            type="masked",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/url/forwarding", None, 1)


def test_urlForwardings_create_url_forwarding_throws_conflict_error() -> None:
    """Test CreateURLForwarding endpoint error response (ConflictError) with WireMock"""
    test_id = "url_forwardings.create_url_forwarding.6"
    client = get_client(test_id)
    with pytest.raises(ConflictError) as exc_info:
        client.url_forwardings.create_url_forwarding(
            domain_name="domainName",
            forwards_to="forwardsTo",
            host="host",
            type="masked",
        )
    assert exc_info.value.status_code == 409
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/url/forwarding", None, 1)


def test_urlForwardings_create_url_forwarding_throws_unsupported_media_type_error() -> None:
    """Test CreateURLForwarding endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "url_forwardings.create_url_forwarding.7"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.url_forwardings.create_url_forwarding(
            domain_name="domainName",
            forwards_to="forwardsTo",
            host="host",
            type="masked",
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/url/forwarding", None, 1)


def test_urlForwardings_create_url_forwarding_throws_too_many_requests_error() -> None:
    """Test CreateURLForwarding endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "url_forwardings.create_url_forwarding.8"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.url_forwardings.create_url_forwarding(
            domain_name="domainName",
            forwards_to="forwardsTo",
            host="host",
            type="masked",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/url/forwarding", None, 1)


def test_urlForwardings_create_url_forwarding_throws_internal_server_error() -> None:
    """Test CreateURLForwarding endpoint error response (InternalServerError) with WireMock"""
    test_id = "url_forwardings.create_url_forwarding.9"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.url_forwardings.create_url_forwarding(
            domain_name="domainName",
            forwards_to="forwardsTo",
            host="host",
            type="masked",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/url/forwarding", None, 1)


def test_urlForwardings_create_url_forwarding_throws_bad_gateway_error() -> None:
    """Test CreateURLForwarding endpoint error response (BadGatewayError) with WireMock"""
    test_id = "url_forwardings.create_url_forwarding.10"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.url_forwardings.create_url_forwarding(
            domain_name="domainName",
            forwards_to="forwardsTo",
            host="host",
            type="masked",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/url/forwarding", None, 1)


def test_urlForwardings_create_url_forwarding_throws_service_unavailable_error() -> None:
    """Test CreateURLForwarding endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "url_forwardings.create_url_forwarding.11"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.url_forwardings.create_url_forwarding(
            domain_name="domainName",
            forwards_to="forwardsTo",
            host="host",
            type="masked",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/url/forwarding", None, 1)


def test_urlForwardings_create_url_forwarding_throws_gateway_timeout_error() -> None:
    """Test CreateURLForwarding endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "url_forwardings.create_url_forwarding.12"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.url_forwardings.create_url_forwarding(
            domain_name="domainName",
            forwards_to="forwardsTo",
            host="host",
            type="masked",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/url/forwarding", None, 1)


def test_urlForwardings_get_url_forwarding() -> None:
    """Test GetURLForwarding endpoint with WireMock"""
    test_id = "url_forwardings.get_url_forwarding.0"
    client = get_client(test_id)
    client.url_forwardings.get_url_forwarding(
        domain_name="example.com",
        host="www.example.org",
    )
    verify_request_count(test_id, "GET", "/core/v1/domains/example.com/url/forwarding/www.example.org", None, 1)


def test_urlForwardings_get_url_forwarding_throws_bad_request_error() -> None:
    """Test GetURLForwarding endpoint error response (BadRequestError) with WireMock"""
    test_id = "url_forwardings.get_url_forwarding.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.url_forwardings.get_url_forwarding(
            domain_name="domainName",
            host="host",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/url/forwarding/host", None, 1)


def test_urlForwardings_get_url_forwarding_throws_unauthorized_error() -> None:
    """Test GetURLForwarding endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "url_forwardings.get_url_forwarding.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.url_forwardings.get_url_forwarding(
            domain_name="domainName",
            host="host",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/url/forwarding/host", None, 1)


def test_urlForwardings_get_url_forwarding_throws_forbidden_error() -> None:
    """Test GetURLForwarding endpoint error response (ForbiddenError) with WireMock"""
    test_id = "url_forwardings.get_url_forwarding.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.url_forwardings.get_url_forwarding(
            domain_name="domainName",
            host="host",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/url/forwarding/host", None, 1)


def test_urlForwardings_get_url_forwarding_throws_not_found_error() -> None:
    """Test GetURLForwarding endpoint error response (NotFoundError) with WireMock"""
    test_id = "url_forwardings.get_url_forwarding.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.url_forwardings.get_url_forwarding(
            domain_name="domainName",
            host="host",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/url/forwarding/host", None, 1)


def test_urlForwardings_get_url_forwarding_throws_method_not_allowed_error() -> None:
    """Test GetURLForwarding endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "url_forwardings.get_url_forwarding.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.url_forwardings.get_url_forwarding(
            domain_name="domainName",
            host="host",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/url/forwarding/host", None, 1)


def test_urlForwardings_get_url_forwarding_throws_too_many_requests_error() -> None:
    """Test GetURLForwarding endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "url_forwardings.get_url_forwarding.6"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.url_forwardings.get_url_forwarding(
            domain_name="domainName",
            host="host",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/url/forwarding/host", None, 1)


def test_urlForwardings_get_url_forwarding_throws_internal_server_error() -> None:
    """Test GetURLForwarding endpoint error response (InternalServerError) with WireMock"""
    test_id = "url_forwardings.get_url_forwarding.7"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.url_forwardings.get_url_forwarding(
            domain_name="domainName",
            host="host",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/url/forwarding/host", None, 1)


def test_urlForwardings_get_url_forwarding_throws_bad_gateway_error() -> None:
    """Test GetURLForwarding endpoint error response (BadGatewayError) with WireMock"""
    test_id = "url_forwardings.get_url_forwarding.8"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.url_forwardings.get_url_forwarding(
            domain_name="domainName",
            host="host",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/url/forwarding/host", None, 1)


def test_urlForwardings_get_url_forwarding_throws_service_unavailable_error() -> None:
    """Test GetURLForwarding endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "url_forwardings.get_url_forwarding.9"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.url_forwardings.get_url_forwarding(
            domain_name="domainName",
            host="host",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/url/forwarding/host", None, 1)


def test_urlForwardings_get_url_forwarding_throws_gateway_timeout_error() -> None:
    """Test GetURLForwarding endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "url_forwardings.get_url_forwarding.10"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.url_forwardings.get_url_forwarding(
            domain_name="domainName",
            host="host",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/url/forwarding/host", None, 1)


def test_urlForwardings_update_url_forwarding() -> None:
    """Test UpdateURLForwarding endpoint with WireMock"""
    test_id = "url_forwardings.update_url_forwarding.0"
    client = get_client(test_id)
    client.url_forwardings.update_url_forwarding(
        domain_name="example.com",
        host_="www.example.org",
    )
    verify_request_count(test_id, "PUT", "/core/v1/domains/example.com/url/forwarding/www.example.org", None, 1)


def test_urlForwardings_update_url_forwarding_throws_bad_request_error() -> None:
    """Test UpdateURLForwarding endpoint error response (BadRequestError) with WireMock"""
    test_id = "url_forwardings.update_url_forwarding.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.url_forwardings.update_url_forwarding(
            domain_name="domainName",
            host_="host",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/url/forwarding/host", None, 1)


def test_urlForwardings_update_url_forwarding_throws_unauthorized_error() -> None:
    """Test UpdateURLForwarding endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "url_forwardings.update_url_forwarding.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.url_forwardings.update_url_forwarding(
            domain_name="domainName",
            host_="host",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/url/forwarding/host", None, 1)


def test_urlForwardings_update_url_forwarding_throws_forbidden_error() -> None:
    """Test UpdateURLForwarding endpoint error response (ForbiddenError) with WireMock"""
    test_id = "url_forwardings.update_url_forwarding.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.url_forwardings.update_url_forwarding(
            domain_name="domainName",
            host_="host",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/url/forwarding/host", None, 1)


def test_urlForwardings_update_url_forwarding_throws_not_found_error() -> None:
    """Test UpdateURLForwarding endpoint error response (NotFoundError) with WireMock"""
    test_id = "url_forwardings.update_url_forwarding.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.url_forwardings.update_url_forwarding(
            domain_name="domainName",
            host_="host",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/url/forwarding/host", None, 1)


def test_urlForwardings_update_url_forwarding_throws_method_not_allowed_error() -> None:
    """Test UpdateURLForwarding endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "url_forwardings.update_url_forwarding.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.url_forwardings.update_url_forwarding(
            domain_name="domainName",
            host_="host",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/url/forwarding/host", None, 1)


def test_urlForwardings_update_url_forwarding_throws_unsupported_media_type_error() -> None:
    """Test UpdateURLForwarding endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "url_forwardings.update_url_forwarding.6"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.url_forwardings.update_url_forwarding(
            domain_name="domainName",
            host_="host",
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/url/forwarding/host", None, 1)


def test_urlForwardings_update_url_forwarding_throws_too_many_requests_error() -> None:
    """Test UpdateURLForwarding endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "url_forwardings.update_url_forwarding.7"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.url_forwardings.update_url_forwarding(
            domain_name="domainName",
            host_="host",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/url/forwarding/host", None, 1)


def test_urlForwardings_update_url_forwarding_throws_internal_server_error() -> None:
    """Test UpdateURLForwarding endpoint error response (InternalServerError) with WireMock"""
    test_id = "url_forwardings.update_url_forwarding.8"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.url_forwardings.update_url_forwarding(
            domain_name="domainName",
            host_="host",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/url/forwarding/host", None, 1)


def test_urlForwardings_update_url_forwarding_throws_bad_gateway_error() -> None:
    """Test UpdateURLForwarding endpoint error response (BadGatewayError) with WireMock"""
    test_id = "url_forwardings.update_url_forwarding.9"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.url_forwardings.update_url_forwarding(
            domain_name="domainName",
            host_="host",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/url/forwarding/host", None, 1)


def test_urlForwardings_update_url_forwarding_throws_service_unavailable_error() -> None:
    """Test UpdateURLForwarding endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "url_forwardings.update_url_forwarding.10"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.url_forwardings.update_url_forwarding(
            domain_name="domainName",
            host_="host",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/url/forwarding/host", None, 1)


def test_urlForwardings_update_url_forwarding_throws_gateway_timeout_error() -> None:
    """Test UpdateURLForwarding endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "url_forwardings.update_url_forwarding.11"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.url_forwardings.update_url_forwarding(
            domain_name="domainName",
            host_="host",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/url/forwarding/host", None, 1)


def test_urlForwardings_delete_url_forwarding() -> None:
    """Test DeleteURLForwarding endpoint with WireMock"""
    test_id = "url_forwardings.delete_url_forwarding.0"
    client = get_client(test_id)
    client.url_forwardings.delete_url_forwarding(
        domain_name="example.com",
        host="www.example.org",
    )
    verify_request_count(test_id, "DELETE", "/core/v1/domains/example.com/url/forwarding/www.example.org", None, 1)


def test_urlForwardings_delete_url_forwarding_throws_unauthorized_error() -> None:
    """Test DeleteURLForwarding endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "url_forwardings.delete_url_forwarding.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.url_forwardings.delete_url_forwarding(
            domain_name="domainName",
            host="host",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/url/forwarding/host", None, 1)


def test_urlForwardings_delete_url_forwarding_throws_forbidden_error() -> None:
    """Test DeleteURLForwarding endpoint error response (ForbiddenError) with WireMock"""
    test_id = "url_forwardings.delete_url_forwarding.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.url_forwardings.delete_url_forwarding(
            domain_name="domainName",
            host="host",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/url/forwarding/host", None, 1)


def test_urlForwardings_delete_url_forwarding_throws_not_found_error() -> None:
    """Test DeleteURLForwarding endpoint error response (NotFoundError) with WireMock"""
    test_id = "url_forwardings.delete_url_forwarding.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.url_forwardings.delete_url_forwarding(
            domain_name="domainName",
            host="host",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/url/forwarding/host", None, 1)


def test_urlForwardings_delete_url_forwarding_throws_method_not_allowed_error() -> None:
    """Test DeleteURLForwarding endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "url_forwardings.delete_url_forwarding.4"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.url_forwardings.delete_url_forwarding(
            domain_name="domainName",
            host="host",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/url/forwarding/host", None, 1)


def test_urlForwardings_delete_url_forwarding_throws_too_many_requests_error() -> None:
    """Test DeleteURLForwarding endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "url_forwardings.delete_url_forwarding.5"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.url_forwardings.delete_url_forwarding(
            domain_name="domainName",
            host="host",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/url/forwarding/host", None, 1)


def test_urlForwardings_delete_url_forwarding_throws_internal_server_error() -> None:
    """Test DeleteURLForwarding endpoint error response (InternalServerError) with WireMock"""
    test_id = "url_forwardings.delete_url_forwarding.6"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.url_forwardings.delete_url_forwarding(
            domain_name="domainName",
            host="host",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/url/forwarding/host", None, 1)


def test_urlForwardings_delete_url_forwarding_throws_bad_gateway_error() -> None:
    """Test DeleteURLForwarding endpoint error response (BadGatewayError) with WireMock"""
    test_id = "url_forwardings.delete_url_forwarding.7"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.url_forwardings.delete_url_forwarding(
            domain_name="domainName",
            host="host",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/url/forwarding/host", None, 1)


def test_urlForwardings_delete_url_forwarding_throws_service_unavailable_error() -> None:
    """Test DeleteURLForwarding endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "url_forwardings.delete_url_forwarding.8"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.url_forwardings.delete_url_forwarding(
            domain_name="domainName",
            host="host",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/url/forwarding/host", None, 1)


def test_urlForwardings_delete_url_forwarding_throws_gateway_timeout_error() -> None:
    """Test DeleteURLForwarding endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "url_forwardings.delete_url_forwarding.9"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.url_forwardings.delete_url_forwarding(
            domain_name="domainName",
            host="host",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/url/forwarding/host", None, 1)


def test_urlForwardings_list_url_forwardings_by_domain() -> None:
    """Test ListURLForwardingsByDomain endpoint with WireMock"""
    test_id = "url_forwardings.list_url_forwardings_by_domain.0"
    client = get_client(test_id)
    client.url_forwardings.list_url_forwardings_by_domain(
        domain_name="example.com",
        per_page=100,
        page=1,
    )
    verify_request_count(test_id, "GET", "/core/v1/urlforwarding/example.com", {"perPage": "100", "page": "1"}, 1)


def test_urlForwardings_list_url_forwardings_by_domain_throws_bad_request_error() -> None:
    """Test ListURLForwardingsByDomain endpoint error response (BadRequestError) with WireMock"""
    test_id = "url_forwardings.list_url_forwardings_by_domain.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.url_forwardings.list_url_forwardings_by_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/urlforwarding/domainName", None, 1)


def test_urlForwardings_list_url_forwardings_by_domain_throws_unauthorized_error() -> None:
    """Test ListURLForwardingsByDomain endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "url_forwardings.list_url_forwardings_by_domain.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.url_forwardings.list_url_forwardings_by_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/urlforwarding/domainName", None, 1)


def test_urlForwardings_list_url_forwardings_by_domain_throws_forbidden_error() -> None:
    """Test ListURLForwardingsByDomain endpoint error response (ForbiddenError) with WireMock"""
    test_id = "url_forwardings.list_url_forwardings_by_domain.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.url_forwardings.list_url_forwardings_by_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/urlforwarding/domainName", None, 1)


def test_urlForwardings_list_url_forwardings_by_domain_throws_not_found_error() -> None:
    """Test ListURLForwardingsByDomain endpoint error response (NotFoundError) with WireMock"""
    test_id = "url_forwardings.list_url_forwardings_by_domain.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.url_forwardings.list_url_forwardings_by_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "GET", "/core/v1/urlforwarding/domainName", None, 1)


def test_urlForwardings_list_url_forwardings_by_domain_throws_method_not_allowed_error() -> None:
    """Test ListURLForwardingsByDomain endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "url_forwardings.list_url_forwardings_by_domain.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.url_forwardings.list_url_forwardings_by_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/urlforwarding/domainName", None, 1)


def test_urlForwardings_list_url_forwardings_by_domain_throws_too_many_requests_error() -> None:
    """Test ListURLForwardingsByDomain endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "url_forwardings.list_url_forwardings_by_domain.6"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.url_forwardings.list_url_forwardings_by_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/urlforwarding/domainName", None, 1)


def test_urlForwardings_list_url_forwardings_by_domain_throws_internal_server_error() -> None:
    """Test ListURLForwardingsByDomain endpoint error response (InternalServerError) with WireMock"""
    test_id = "url_forwardings.list_url_forwardings_by_domain.7"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.url_forwardings.list_url_forwardings_by_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/urlforwarding/domainName", None, 1)


def test_urlForwardings_list_url_forwardings_by_domain_throws_bad_gateway_error() -> None:
    """Test ListURLForwardingsByDomain endpoint error response (BadGatewayError) with WireMock"""
    test_id = "url_forwardings.list_url_forwardings_by_domain.8"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.url_forwardings.list_url_forwardings_by_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/urlforwarding/domainName", None, 1)


def test_urlForwardings_list_url_forwardings_by_domain_throws_service_unavailable_error() -> None:
    """Test ListURLForwardingsByDomain endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "url_forwardings.list_url_forwardings_by_domain.9"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.url_forwardings.list_url_forwardings_by_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/urlforwarding/domainName", None, 1)


def test_urlForwardings_list_url_forwardings_by_domain_throws_gateway_timeout_error() -> None:
    """Test ListURLForwardingsByDomain endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "url_forwardings.list_url_forwardings_by_domain.10"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.url_forwardings.list_url_forwardings_by_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/urlforwarding/domainName", None, 1)


def test_urlForwardings_get_url_forwarding_by_id() -> None:
    """Test GetURLForwardingById endpoint with WireMock"""
    test_id = "url_forwardings.get_url_forwarding_by_id.0"
    client = get_client(test_id)
    client.url_forwardings.get_url_forwarding_by_id(
        domain_name="example.com",
        id=12345,
    )
    verify_request_count(test_id, "GET", "/core/v1/urlforwarding/example.com/12345", None, 1)


def test_urlForwardings_get_url_forwarding_by_id_throws_bad_request_error() -> None:
    """Test GetURLForwardingById endpoint error response (BadRequestError) with WireMock"""
    test_id = "url_forwardings.get_url_forwarding_by_id.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.url_forwardings.get_url_forwarding_by_id(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/urlforwarding/domainName/1", None, 1)


def test_urlForwardings_get_url_forwarding_by_id_throws_unauthorized_error() -> None:
    """Test GetURLForwardingById endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "url_forwardings.get_url_forwarding_by_id.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.url_forwardings.get_url_forwarding_by_id(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/urlforwarding/domainName/1", None, 1)


def test_urlForwardings_get_url_forwarding_by_id_throws_forbidden_error() -> None:
    """Test GetURLForwardingById endpoint error response (ForbiddenError) with WireMock"""
    test_id = "url_forwardings.get_url_forwarding_by_id.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.url_forwardings.get_url_forwarding_by_id(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/urlforwarding/domainName/1", None, 1)


def test_urlForwardings_get_url_forwarding_by_id_throws_not_found_error() -> None:
    """Test GetURLForwardingById endpoint error response (NotFoundError) with WireMock"""
    test_id = "url_forwardings.get_url_forwarding_by_id.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.url_forwardings.get_url_forwarding_by_id(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "GET", "/core/v1/urlforwarding/domainName/1", None, 1)


def test_urlForwardings_get_url_forwarding_by_id_throws_method_not_allowed_error() -> None:
    """Test GetURLForwardingById endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "url_forwardings.get_url_forwarding_by_id.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.url_forwardings.get_url_forwarding_by_id(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/urlforwarding/domainName/1", None, 1)


def test_urlForwardings_get_url_forwarding_by_id_throws_too_many_requests_error() -> None:
    """Test GetURLForwardingById endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "url_forwardings.get_url_forwarding_by_id.6"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.url_forwardings.get_url_forwarding_by_id(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/urlforwarding/domainName/1", None, 1)


def test_urlForwardings_get_url_forwarding_by_id_throws_internal_server_error() -> None:
    """Test GetURLForwardingById endpoint error response (InternalServerError) with WireMock"""
    test_id = "url_forwardings.get_url_forwarding_by_id.7"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.url_forwardings.get_url_forwarding_by_id(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/urlforwarding/domainName/1", None, 1)


def test_urlForwardings_get_url_forwarding_by_id_throws_bad_gateway_error() -> None:
    """Test GetURLForwardingById endpoint error response (BadGatewayError) with WireMock"""
    test_id = "url_forwardings.get_url_forwarding_by_id.8"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.url_forwardings.get_url_forwarding_by_id(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/urlforwarding/domainName/1", None, 1)


def test_urlForwardings_get_url_forwarding_by_id_throws_service_unavailable_error() -> None:
    """Test GetURLForwardingById endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "url_forwardings.get_url_forwarding_by_id.9"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.url_forwardings.get_url_forwarding_by_id(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/urlforwarding/domainName/1", None, 1)


def test_urlForwardings_get_url_forwarding_by_id_throws_gateway_timeout_error() -> None:
    """Test GetURLForwardingById endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "url_forwardings.get_url_forwarding_by_id.10"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.url_forwardings.get_url_forwarding_by_id(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/urlforwarding/domainName/1", None, 1)


def test_urlForwardings_delete_url_forwarding_by_id() -> None:
    """Test DeleteURLForwardingById endpoint with WireMock"""
    test_id = "url_forwardings.delete_url_forwarding_by_id.0"
    client = get_client(test_id)
    client.url_forwardings.delete_url_forwarding_by_id(
        domain_name="example.com",
        id=12345,
    )
    verify_request_count(test_id, "DELETE", "/core/v1/urlforwarding/example.com/12345", None, 1)


def test_urlForwardings_delete_url_forwarding_by_id_throws_unauthorized_error() -> None:
    """Test DeleteURLForwardingById endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "url_forwardings.delete_url_forwarding_by_id.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.url_forwardings.delete_url_forwarding_by_id(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/urlforwarding/domainName/1", None, 1)


def test_urlForwardings_delete_url_forwarding_by_id_throws_forbidden_error() -> None:
    """Test DeleteURLForwardingById endpoint error response (ForbiddenError) with WireMock"""
    test_id = "url_forwardings.delete_url_forwarding_by_id.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.url_forwardings.delete_url_forwarding_by_id(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/urlforwarding/domainName/1", None, 1)


def test_urlForwardings_delete_url_forwarding_by_id_throws_not_found_error() -> None:
    """Test DeleteURLForwardingById endpoint error response (NotFoundError) with WireMock"""
    test_id = "url_forwardings.delete_url_forwarding_by_id.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.url_forwardings.delete_url_forwarding_by_id(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "DELETE", "/core/v1/urlforwarding/domainName/1", None, 1)


def test_urlForwardings_delete_url_forwarding_by_id_throws_method_not_allowed_error() -> None:
    """Test DeleteURLForwardingById endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "url_forwardings.delete_url_forwarding_by_id.4"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.url_forwardings.delete_url_forwarding_by_id(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/urlforwarding/domainName/1", None, 1)


def test_urlForwardings_delete_url_forwarding_by_id_throws_too_many_requests_error() -> None:
    """Test DeleteURLForwardingById endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "url_forwardings.delete_url_forwarding_by_id.5"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.url_forwardings.delete_url_forwarding_by_id(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/urlforwarding/domainName/1", None, 1)


def test_urlForwardings_delete_url_forwarding_by_id_throws_internal_server_error() -> None:
    """Test DeleteURLForwardingById endpoint error response (InternalServerError) with WireMock"""
    test_id = "url_forwardings.delete_url_forwarding_by_id.6"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.url_forwardings.delete_url_forwarding_by_id(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/urlforwarding/domainName/1", None, 1)


def test_urlForwardings_delete_url_forwarding_by_id_throws_bad_gateway_error() -> None:
    """Test DeleteURLForwardingById endpoint error response (BadGatewayError) with WireMock"""
    test_id = "url_forwardings.delete_url_forwarding_by_id.7"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.url_forwardings.delete_url_forwarding_by_id(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/urlforwarding/domainName/1", None, 1)


def test_urlForwardings_delete_url_forwarding_by_id_throws_service_unavailable_error() -> None:
    """Test DeleteURLForwardingById endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "url_forwardings.delete_url_forwarding_by_id.8"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.url_forwardings.delete_url_forwarding_by_id(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/urlforwarding/domainName/1", None, 1)


def test_urlForwardings_delete_url_forwarding_by_id_throws_gateway_timeout_error() -> None:
    """Test DeleteURLForwardingById endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "url_forwardings.delete_url_forwarding_by_id.9"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.url_forwardings.delete_url_forwarding_by_id(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/urlforwarding/domainName/1", None, 1)


def test_urlForwardings_update_url_forwarding_by_id() -> None:
    """Test UpdateURLForwardingById endpoint with WireMock"""
    test_id = "url_forwardings.update_url_forwarding_by_id.0"
    client = get_client(test_id)
    client.url_forwardings.update_url_forwarding_by_id(
        domain_name="example.com",
        id=12345,
    )
    verify_request_count(test_id, "PATCH", "/core/v1/urlforwarding/example.com/12345", None, 1)


def test_urlForwardings_update_url_forwarding_by_id_throws_bad_request_error() -> None:
    """Test UpdateURLForwardingById endpoint error response (BadRequestError) with WireMock"""
    test_id = "url_forwardings.update_url_forwarding_by_id.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.url_forwardings.update_url_forwarding_by_id(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/core/v1/urlforwarding/domainName/1", None, 1)


def test_urlForwardings_update_url_forwarding_by_id_throws_unauthorized_error() -> None:
    """Test UpdateURLForwardingById endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "url_forwardings.update_url_forwarding_by_id.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.url_forwardings.update_url_forwarding_by_id(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/core/v1/urlforwarding/domainName/1", None, 1)


def test_urlForwardings_update_url_forwarding_by_id_throws_forbidden_error() -> None:
    """Test UpdateURLForwardingById endpoint error response (ForbiddenError) with WireMock"""
    test_id = "url_forwardings.update_url_forwarding_by_id.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.url_forwardings.update_url_forwarding_by_id(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/core/v1/urlforwarding/domainName/1", None, 1)


def test_urlForwardings_update_url_forwarding_by_id_throws_not_found_error() -> None:
    """Test UpdateURLForwardingById endpoint error response (NotFoundError) with WireMock"""
    test_id = "url_forwardings.update_url_forwarding_by_id.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.url_forwardings.update_url_forwarding_by_id(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "PATCH", "/core/v1/urlforwarding/domainName/1", None, 1)


def test_urlForwardings_update_url_forwarding_by_id_throws_method_not_allowed_error() -> None:
    """Test UpdateURLForwardingById endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "url_forwardings.update_url_forwarding_by_id.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.url_forwardings.update_url_forwarding_by_id(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/core/v1/urlforwarding/domainName/1", None, 1)


def test_urlForwardings_update_url_forwarding_by_id_throws_unsupported_media_type_error() -> None:
    """Test UpdateURLForwardingById endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "url_forwardings.update_url_forwarding_by_id.6"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.url_forwardings.update_url_forwarding_by_id(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "PATCH", "/core/v1/urlforwarding/domainName/1", None, 1)


def test_urlForwardings_update_url_forwarding_by_id_throws_too_many_requests_error() -> None:
    """Test UpdateURLForwardingById endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "url_forwardings.update_url_forwarding_by_id.7"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.url_forwardings.update_url_forwarding_by_id(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/core/v1/urlforwarding/domainName/1", None, 1)


def test_urlForwardings_update_url_forwarding_by_id_throws_internal_server_error() -> None:
    """Test UpdateURLForwardingById endpoint error response (InternalServerError) with WireMock"""
    test_id = "url_forwardings.update_url_forwarding_by_id.8"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.url_forwardings.update_url_forwarding_by_id(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/core/v1/urlforwarding/domainName/1", None, 1)


def test_urlForwardings_update_url_forwarding_by_id_throws_bad_gateway_error() -> None:
    """Test UpdateURLForwardingById endpoint error response (BadGatewayError) with WireMock"""
    test_id = "url_forwardings.update_url_forwarding_by_id.9"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.url_forwardings.update_url_forwarding_by_id(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/core/v1/urlforwarding/domainName/1", None, 1)


def test_urlForwardings_update_url_forwarding_by_id_throws_service_unavailable_error() -> None:
    """Test UpdateURLForwardingById endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "url_forwardings.update_url_forwarding_by_id.10"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.url_forwardings.update_url_forwarding_by_id(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/core/v1/urlforwarding/domainName/1", None, 1)


def test_urlForwardings_update_url_forwarding_by_id_throws_gateway_timeout_error() -> None:
    """Test UpdateURLForwardingById endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "url_forwardings.update_url_forwarding_by_id.11"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.url_forwardings.update_url_forwarding_by_id(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/core/v1/urlforwarding/domainName/1", None, 1)

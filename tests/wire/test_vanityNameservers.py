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


def test_vanityNameservers_list_vanity_nameservers_throws_bad_request_error() -> None:
    """Test ListVanityNameservers endpoint error response (BadRequestError) with WireMock"""
    test_id = "vanity_nameservers.list_vanity_nameservers.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.vanity_nameservers.list_vanity_nameservers(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/vanity_nameservers", None, 1)


def test_vanityNameservers_list_vanity_nameservers_throws_unauthorized_error() -> None:
    """Test ListVanityNameservers endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "vanity_nameservers.list_vanity_nameservers.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.vanity_nameservers.list_vanity_nameservers(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/vanity_nameservers", None, 1)


def test_vanityNameservers_list_vanity_nameservers_throws_forbidden_error() -> None:
    """Test ListVanityNameservers endpoint error response (ForbiddenError) with WireMock"""
    test_id = "vanity_nameservers.list_vanity_nameservers.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.vanity_nameservers.list_vanity_nameservers(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/vanity_nameservers", None, 1)


def test_vanityNameservers_list_vanity_nameservers_throws_not_found_error() -> None:
    """Test ListVanityNameservers endpoint error response (NotFoundError) with WireMock"""
    test_id = "vanity_nameservers.list_vanity_nameservers.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.vanity_nameservers.list_vanity_nameservers(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/vanity_nameservers", None, 1)


def test_vanityNameservers_list_vanity_nameservers_throws_method_not_allowed_error() -> None:
    """Test ListVanityNameservers endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "vanity_nameservers.list_vanity_nameservers.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.vanity_nameservers.list_vanity_nameservers(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/vanity_nameservers", None, 1)


def test_vanityNameservers_list_vanity_nameservers_throws_too_many_requests_error() -> None:
    """Test ListVanityNameservers endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "vanity_nameservers.list_vanity_nameservers.6"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.vanity_nameservers.list_vanity_nameservers(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/vanity_nameservers", None, 1)


def test_vanityNameservers_list_vanity_nameservers_throws_internal_server_error() -> None:
    """Test ListVanityNameservers endpoint error response (InternalServerError) with WireMock"""
    test_id = "vanity_nameservers.list_vanity_nameservers.7"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.vanity_nameservers.list_vanity_nameservers(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/vanity_nameservers", None, 1)


def test_vanityNameservers_list_vanity_nameservers_throws_bad_gateway_error() -> None:
    """Test ListVanityNameservers endpoint error response (BadGatewayError) with WireMock"""
    test_id = "vanity_nameservers.list_vanity_nameservers.8"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.vanity_nameservers.list_vanity_nameservers(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/vanity_nameservers", None, 1)


def test_vanityNameservers_list_vanity_nameservers_throws_service_unavailable_error() -> None:
    """Test ListVanityNameservers endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "vanity_nameservers.list_vanity_nameservers.9"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.vanity_nameservers.list_vanity_nameservers(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/vanity_nameservers", None, 1)


def test_vanityNameservers_list_vanity_nameservers_throws_gateway_timeout_error() -> None:
    """Test ListVanityNameservers endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "vanity_nameservers.list_vanity_nameservers.10"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.vanity_nameservers.list_vanity_nameservers(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/vanity_nameservers", None, 1)


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


def test_vanityNameservers_create_vanity_nameserver_throws_bad_request_error() -> None:
    """Test CreateVanityNameserver endpoint error response (BadRequestError) with WireMock"""
    test_id = "vanity_nameservers.create_vanity_nameserver.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.vanity_nameservers.create_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
            ips=["ips", "ips"],
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/vanity_nameservers", None, 1)


def test_vanityNameservers_create_vanity_nameserver_throws_unauthorized_error() -> None:
    """Test CreateVanityNameserver endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "vanity_nameservers.create_vanity_nameserver.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.vanity_nameservers.create_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
            ips=["ips", "ips"],
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/vanity_nameservers", None, 1)


def test_vanityNameservers_create_vanity_nameserver_throws_forbidden_error() -> None:
    """Test CreateVanityNameserver endpoint error response (ForbiddenError) with WireMock"""
    test_id = "vanity_nameservers.create_vanity_nameserver.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.vanity_nameservers.create_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
            ips=["ips", "ips"],
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/vanity_nameservers", None, 1)


def test_vanityNameservers_create_vanity_nameserver_throws_not_found_error() -> None:
    """Test CreateVanityNameserver endpoint error response (NotFoundError) with WireMock"""
    test_id = "vanity_nameservers.create_vanity_nameserver.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.vanity_nameservers.create_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
            ips=["ips", "ips"],
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/vanity_nameservers", None, 1)


def test_vanityNameservers_create_vanity_nameserver_throws_method_not_allowed_error() -> None:
    """Test CreateVanityNameserver endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "vanity_nameservers.create_vanity_nameserver.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.vanity_nameservers.create_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
            ips=["ips", "ips"],
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/vanity_nameservers", None, 1)


def test_vanityNameservers_create_vanity_nameserver_throws_conflict_error() -> None:
    """Test CreateVanityNameserver endpoint error response (ConflictError) with WireMock"""
    test_id = "vanity_nameservers.create_vanity_nameserver.6"
    client = get_client(test_id)
    with pytest.raises(ConflictError) as exc_info:
        client.vanity_nameservers.create_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
            ips=["ips", "ips"],
        )
    assert exc_info.value.status_code == 409
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/vanity_nameservers", None, 1)


def test_vanityNameservers_create_vanity_nameserver_throws_unsupported_media_type_error() -> None:
    """Test CreateVanityNameserver endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "vanity_nameservers.create_vanity_nameserver.7"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.vanity_nameservers.create_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
            ips=["ips", "ips"],
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/vanity_nameservers", None, 1)


def test_vanityNameservers_create_vanity_nameserver_throws_too_many_requests_error() -> None:
    """Test CreateVanityNameserver endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "vanity_nameservers.create_vanity_nameserver.8"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.vanity_nameservers.create_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
            ips=["ips", "ips"],
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/vanity_nameservers", None, 1)


def test_vanityNameservers_create_vanity_nameserver_throws_internal_server_error() -> None:
    """Test CreateVanityNameserver endpoint error response (InternalServerError) with WireMock"""
    test_id = "vanity_nameservers.create_vanity_nameserver.9"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.vanity_nameservers.create_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
            ips=["ips", "ips"],
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/vanity_nameservers", None, 1)


def test_vanityNameservers_create_vanity_nameserver_throws_bad_gateway_error() -> None:
    """Test CreateVanityNameserver endpoint error response (BadGatewayError) with WireMock"""
    test_id = "vanity_nameservers.create_vanity_nameserver.10"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.vanity_nameservers.create_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
            ips=["ips", "ips"],
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/vanity_nameservers", None, 1)


def test_vanityNameservers_create_vanity_nameserver_throws_service_unavailable_error() -> None:
    """Test CreateVanityNameserver endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "vanity_nameservers.create_vanity_nameserver.11"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.vanity_nameservers.create_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
            ips=["ips", "ips"],
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/vanity_nameservers", None, 1)


def test_vanityNameservers_create_vanity_nameserver_throws_gateway_timeout_error() -> None:
    """Test CreateVanityNameserver endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "vanity_nameservers.create_vanity_nameserver.12"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.vanity_nameservers.create_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
            ips=["ips", "ips"],
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/vanity_nameservers", None, 1)


def test_vanityNameservers_get_vanity_nameserver() -> None:
    """Test GetVanityNameserver endpoint with WireMock"""
    test_id = "vanity_nameservers.get_vanity_nameserver.0"
    client = get_client(test_id)
    client.vanity_nameservers.get_vanity_nameserver(
        domain_name="example.com",
        hostname="ns1.example.com",
    )
    verify_request_count(test_id, "GET", "/core/v1/domains/example.com/vanity_nameservers/ns1.example.com", None, 1)


def test_vanityNameservers_get_vanity_nameserver_throws_bad_request_error() -> None:
    """Test GetVanityNameserver endpoint error response (BadRequestError) with WireMock"""
    test_id = "vanity_nameservers.get_vanity_nameserver.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.vanity_nameservers.get_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)


def test_vanityNameservers_get_vanity_nameserver_throws_unauthorized_error() -> None:
    """Test GetVanityNameserver endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "vanity_nameservers.get_vanity_nameserver.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.vanity_nameservers.get_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)


def test_vanityNameservers_get_vanity_nameserver_throws_forbidden_error() -> None:
    """Test GetVanityNameserver endpoint error response (ForbiddenError) with WireMock"""
    test_id = "vanity_nameservers.get_vanity_nameserver.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.vanity_nameservers.get_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)


def test_vanityNameservers_get_vanity_nameserver_throws_not_found_error() -> None:
    """Test GetVanityNameserver endpoint error response (NotFoundError) with WireMock"""
    test_id = "vanity_nameservers.get_vanity_nameserver.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.vanity_nameservers.get_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)


def test_vanityNameservers_get_vanity_nameserver_throws_method_not_allowed_error() -> None:
    """Test GetVanityNameserver endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "vanity_nameservers.get_vanity_nameserver.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.vanity_nameservers.get_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)


def test_vanityNameservers_get_vanity_nameserver_throws_too_many_requests_error() -> None:
    """Test GetVanityNameserver endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "vanity_nameservers.get_vanity_nameserver.6"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.vanity_nameservers.get_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)


def test_vanityNameservers_get_vanity_nameserver_throws_internal_server_error() -> None:
    """Test GetVanityNameserver endpoint error response (InternalServerError) with WireMock"""
    test_id = "vanity_nameservers.get_vanity_nameserver.7"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.vanity_nameservers.get_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)


def test_vanityNameservers_get_vanity_nameserver_throws_bad_gateway_error() -> None:
    """Test GetVanityNameserver endpoint error response (BadGatewayError) with WireMock"""
    test_id = "vanity_nameservers.get_vanity_nameserver.8"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.vanity_nameservers.get_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)


def test_vanityNameservers_get_vanity_nameserver_throws_service_unavailable_error() -> None:
    """Test GetVanityNameserver endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "vanity_nameservers.get_vanity_nameserver.9"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.vanity_nameservers.get_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)


def test_vanityNameservers_get_vanity_nameserver_throws_gateway_timeout_error() -> None:
    """Test GetVanityNameserver endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "vanity_nameservers.get_vanity_nameserver.10"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.vanity_nameservers.get_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)


def test_vanityNameservers_update_vanity_nameserver() -> None:
    """Test UpdateVanityNameserver endpoint with WireMock"""
    test_id = "vanity_nameservers.update_vanity_nameserver.0"
    client = get_client(test_id)
    client.vanity_nameservers.update_vanity_nameserver(
        domain_name="example.com",
        hostname="ns1.example.com",
        ips=["192.168.1.10", "2001:0db8:85a3:0000:0000:8a2e:0370:7334"],
    )
    verify_request_count(test_id, "PUT", "/core/v1/domains/example.com/vanity_nameservers/ns1.example.com", None, 1)


def test_vanityNameservers_update_vanity_nameserver_throws_bad_request_error() -> None:
    """Test UpdateVanityNameserver endpoint error response (BadRequestError) with WireMock"""
    test_id = "vanity_nameservers.update_vanity_nameserver.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.vanity_nameservers.update_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
            ips=["ips", "ips"],
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)


def test_vanityNameservers_update_vanity_nameserver_throws_unauthorized_error() -> None:
    """Test UpdateVanityNameserver endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "vanity_nameservers.update_vanity_nameserver.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.vanity_nameservers.update_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
            ips=["ips", "ips"],
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)


def test_vanityNameservers_update_vanity_nameserver_throws_forbidden_error() -> None:
    """Test UpdateVanityNameserver endpoint error response (ForbiddenError) with WireMock"""
    test_id = "vanity_nameservers.update_vanity_nameserver.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.vanity_nameservers.update_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
            ips=["ips", "ips"],
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)


def test_vanityNameservers_update_vanity_nameserver_throws_not_found_error() -> None:
    """Test UpdateVanityNameserver endpoint error response (NotFoundError) with WireMock"""
    test_id = "vanity_nameservers.update_vanity_nameserver.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.vanity_nameservers.update_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
            ips=["ips", "ips"],
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)


def test_vanityNameservers_update_vanity_nameserver_throws_method_not_allowed_error() -> None:
    """Test UpdateVanityNameserver endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "vanity_nameservers.update_vanity_nameserver.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.vanity_nameservers.update_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
            ips=["ips", "ips"],
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)


def test_vanityNameservers_update_vanity_nameserver_throws_unsupported_media_type_error() -> None:
    """Test UpdateVanityNameserver endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "vanity_nameservers.update_vanity_nameserver.6"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.vanity_nameservers.update_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
            ips=["ips", "ips"],
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)


def test_vanityNameservers_update_vanity_nameserver_throws_too_many_requests_error() -> None:
    """Test UpdateVanityNameserver endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "vanity_nameservers.update_vanity_nameserver.7"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.vanity_nameservers.update_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
            ips=["ips", "ips"],
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)


def test_vanityNameservers_update_vanity_nameserver_throws_internal_server_error() -> None:
    """Test UpdateVanityNameserver endpoint error response (InternalServerError) with WireMock"""
    test_id = "vanity_nameservers.update_vanity_nameserver.8"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.vanity_nameservers.update_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
            ips=["ips", "ips"],
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)


def test_vanityNameservers_update_vanity_nameserver_throws_bad_gateway_error() -> None:
    """Test UpdateVanityNameserver endpoint error response (BadGatewayError) with WireMock"""
    test_id = "vanity_nameservers.update_vanity_nameserver.9"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.vanity_nameservers.update_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
            ips=["ips", "ips"],
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)


def test_vanityNameservers_update_vanity_nameserver_throws_service_unavailable_error() -> None:
    """Test UpdateVanityNameserver endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "vanity_nameservers.update_vanity_nameserver.10"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.vanity_nameservers.update_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
            ips=["ips", "ips"],
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)


def test_vanityNameservers_update_vanity_nameserver_throws_gateway_timeout_error() -> None:
    """Test UpdateVanityNameserver endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "vanity_nameservers.update_vanity_nameserver.11"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.vanity_nameservers.update_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
            ips=["ips", "ips"],
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)


def test_vanityNameservers_delete_vanity_nameserver() -> None:
    """Test DeleteVanityNameserver endpoint with WireMock"""
    test_id = "vanity_nameservers.delete_vanity_nameserver.0"
    client = get_client(test_id)
    client.vanity_nameservers.delete_vanity_nameserver(
        domain_name="example.com",
        hostname="ns1.example.com",
    )
    verify_request_count(test_id, "DELETE", "/core/v1/domains/example.com/vanity_nameservers/ns1.example.com", None, 1)


def test_vanityNameservers_delete_vanity_nameserver_throws_bad_request_error() -> None:
    """Test DeleteVanityNameserver endpoint error response (BadRequestError) with WireMock"""
    test_id = "vanity_nameservers.delete_vanity_nameserver.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.vanity_nameservers.delete_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)


def test_vanityNameservers_delete_vanity_nameserver_throws_unauthorized_error() -> None:
    """Test DeleteVanityNameserver endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "vanity_nameservers.delete_vanity_nameserver.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.vanity_nameservers.delete_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)


def test_vanityNameservers_delete_vanity_nameserver_throws_forbidden_error() -> None:
    """Test DeleteVanityNameserver endpoint error response (ForbiddenError) with WireMock"""
    test_id = "vanity_nameservers.delete_vanity_nameserver.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.vanity_nameservers.delete_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)


def test_vanityNameservers_delete_vanity_nameserver_throws_not_found_error() -> None:
    """Test DeleteVanityNameserver endpoint error response (NotFoundError) with WireMock"""
    test_id = "vanity_nameservers.delete_vanity_nameserver.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.vanity_nameservers.delete_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)


def test_vanityNameservers_delete_vanity_nameserver_throws_method_not_allowed_error() -> None:
    """Test DeleteVanityNameserver endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "vanity_nameservers.delete_vanity_nameserver.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.vanity_nameservers.delete_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)


def test_vanityNameservers_delete_vanity_nameserver_throws_too_many_requests_error() -> None:
    """Test DeleteVanityNameserver endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "vanity_nameservers.delete_vanity_nameserver.6"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.vanity_nameservers.delete_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)


def test_vanityNameservers_delete_vanity_nameserver_throws_internal_server_error() -> None:
    """Test DeleteVanityNameserver endpoint error response (InternalServerError) with WireMock"""
    test_id = "vanity_nameservers.delete_vanity_nameserver.7"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.vanity_nameservers.delete_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)


def test_vanityNameservers_delete_vanity_nameserver_throws_bad_gateway_error() -> None:
    """Test DeleteVanityNameserver endpoint error response (BadGatewayError) with WireMock"""
    test_id = "vanity_nameservers.delete_vanity_nameserver.8"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.vanity_nameservers.delete_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)


def test_vanityNameservers_delete_vanity_nameserver_throws_service_unavailable_error() -> None:
    """Test DeleteVanityNameserver endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "vanity_nameservers.delete_vanity_nameserver.9"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.vanity_nameservers.delete_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)


def test_vanityNameservers_delete_vanity_nameserver_throws_gateway_timeout_error() -> None:
    """Test DeleteVanityNameserver endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "vanity_nameservers.delete_vanity_nameserver.10"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.vanity_nameservers.delete_vanity_nameserver(
            domain_name="domainName",
            hostname="hostname",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/vanity_nameservers/hostname", None, 1)

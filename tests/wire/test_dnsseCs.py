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


def test_dnsseCs_list_dnsse_cs() -> None:
    """Test ListDNSSECs endpoint with WireMock"""
    test_id = "dnsse_cs.list_dnsse_cs.0"
    client = get_client(test_id)
    client.dnsse_cs.list_dnsse_cs(
        domain_name="domainName",
    )
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/dnssec", None, 1)


def test_dnsseCs_list_dnsse_cs_throws_unauthorized_error() -> None:
    """Test ListDNSSECs endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "dnsse_cs.list_dnsse_cs.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.dnsse_cs.list_dnsse_cs(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/dnssec", None, 1)


def test_dnsseCs_list_dnsse_cs_throws_forbidden_error() -> None:
    """Test ListDNSSECs endpoint error response (ForbiddenError) with WireMock"""
    test_id = "dnsse_cs.list_dnsse_cs.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.dnsse_cs.list_dnsse_cs(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/dnssec", None, 1)


def test_dnsseCs_list_dnsse_cs_throws_not_found_error() -> None:
    """Test ListDNSSECs endpoint error response (NotFoundError) with WireMock"""
    test_id = "dnsse_cs.list_dnsse_cs.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.dnsse_cs.list_dnsse_cs(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/dnssec", None, 1)


def test_dnsseCs_list_dnsse_cs_throws_method_not_allowed_error() -> None:
    """Test ListDNSSECs endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "dnsse_cs.list_dnsse_cs.4"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.dnsse_cs.list_dnsse_cs(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/dnssec", None, 1)


def test_dnsseCs_list_dnsse_cs_throws_too_many_requests_error() -> None:
    """Test ListDNSSECs endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "dnsse_cs.list_dnsse_cs.5"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.dnsse_cs.list_dnsse_cs(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/dnssec", None, 1)


def test_dnsseCs_list_dnsse_cs_throws_internal_server_error() -> None:
    """Test ListDNSSECs endpoint error response (InternalServerError) with WireMock"""
    test_id = "dnsse_cs.list_dnsse_cs.6"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.dnsse_cs.list_dnsse_cs(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/dnssec", None, 1)


def test_dnsseCs_list_dnsse_cs_throws_bad_gateway_error() -> None:
    """Test ListDNSSECs endpoint error response (BadGatewayError) with WireMock"""
    test_id = "dnsse_cs.list_dnsse_cs.7"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.dnsse_cs.list_dnsse_cs(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/dnssec", None, 1)


def test_dnsseCs_list_dnsse_cs_throws_service_unavailable_error() -> None:
    """Test ListDNSSECs endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "dnsse_cs.list_dnsse_cs.8"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.dnsse_cs.list_dnsse_cs(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/dnssec", None, 1)


def test_dnsseCs_list_dnsse_cs_throws_gateway_timeout_error() -> None:
    """Test ListDNSSECs endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "dnsse_cs.list_dnsse_cs.9"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.dnsse_cs.list_dnsse_cs(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/dnssec", None, 1)


def test_dnsseCs_create_dnssec() -> None:
    """Test CreateDNSSEC endpoint with WireMock"""
    test_id = "dnsse_cs.create_dnssec.0"
    client = get_client(test_id)
    client.dnsse_cs.create_dnssec(
        domain_name="domainName",
        algorithm=1,
        digest="digest",
        digest_type=1,
        key_tag=1,
    )
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/dnssec", None, 1)


def test_dnsseCs_create_dnssec_throws_bad_request_error() -> None:
    """Test CreateDNSSEC endpoint error response (BadRequestError) with WireMock"""
    test_id = "dnsse_cs.create_dnssec.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.dnsse_cs.create_dnssec(
            domain_name="domainName",
            algorithm=1,
            digest="x",
            digest_type=1,
            key_tag=1,
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/dnssec", None, 1)


def test_dnsseCs_create_dnssec_throws_unauthorized_error() -> None:
    """Test CreateDNSSEC endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "dnsse_cs.create_dnssec.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.dnsse_cs.create_dnssec(
            domain_name="domainName",
            algorithm=1,
            digest="x",
            digest_type=1,
            key_tag=1,
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/dnssec", None, 1)


def test_dnsseCs_create_dnssec_throws_forbidden_error() -> None:
    """Test CreateDNSSEC endpoint error response (ForbiddenError) with WireMock"""
    test_id = "dnsse_cs.create_dnssec.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.dnsse_cs.create_dnssec(
            domain_name="domainName",
            algorithm=1,
            digest="x",
            digest_type=1,
            key_tag=1,
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/dnssec", None, 1)


def test_dnsseCs_create_dnssec_throws_not_found_error() -> None:
    """Test CreateDNSSEC endpoint error response (NotFoundError) with WireMock"""
    test_id = "dnsse_cs.create_dnssec.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.dnsse_cs.create_dnssec(
            domain_name="domainName",
            algorithm=1,
            digest="x",
            digest_type=1,
            key_tag=1,
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/dnssec", None, 1)


def test_dnsseCs_create_dnssec_throws_method_not_allowed_error() -> None:
    """Test CreateDNSSEC endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "dnsse_cs.create_dnssec.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.dnsse_cs.create_dnssec(
            domain_name="domainName",
            algorithm=1,
            digest="x",
            digest_type=1,
            key_tag=1,
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/dnssec", None, 1)


def test_dnsseCs_create_dnssec_throws_conflict_error() -> None:
    """Test CreateDNSSEC endpoint error response (ConflictError) with WireMock"""
    test_id = "dnsse_cs.create_dnssec.6"
    client = get_client(test_id)
    with pytest.raises(ConflictError) as exc_info:
        client.dnsse_cs.create_dnssec(
            domain_name="domainName",
            algorithm=1,
            digest="x",
            digest_type=1,
            key_tag=1,
        )
    assert exc_info.value.status_code == 409
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/dnssec", None, 1)


def test_dnsseCs_create_dnssec_throws_unsupported_media_type_error() -> None:
    """Test CreateDNSSEC endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "dnsse_cs.create_dnssec.7"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.dnsse_cs.create_dnssec(
            domain_name="domainName",
            algorithm=1,
            digest="x",
            digest_type=1,
            key_tag=1,
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/dnssec", None, 1)


def test_dnsseCs_create_dnssec_throws_too_many_requests_error() -> None:
    """Test CreateDNSSEC endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "dnsse_cs.create_dnssec.8"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.dnsse_cs.create_dnssec(
            domain_name="domainName",
            algorithm=1,
            digest="x",
            digest_type=1,
            key_tag=1,
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/dnssec", None, 1)


def test_dnsseCs_create_dnssec_throws_internal_server_error() -> None:
    """Test CreateDNSSEC endpoint error response (InternalServerError) with WireMock"""
    test_id = "dnsse_cs.create_dnssec.9"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.dnsse_cs.create_dnssec(
            domain_name="domainName",
            algorithm=1,
            digest="x",
            digest_type=1,
            key_tag=1,
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/dnssec", None, 1)


def test_dnsseCs_create_dnssec_throws_bad_gateway_error() -> None:
    """Test CreateDNSSEC endpoint error response (BadGatewayError) with WireMock"""
    test_id = "dnsse_cs.create_dnssec.10"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.dnsse_cs.create_dnssec(
            domain_name="domainName",
            algorithm=1,
            digest="x",
            digest_type=1,
            key_tag=1,
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/dnssec", None, 1)


def test_dnsseCs_create_dnssec_throws_service_unavailable_error() -> None:
    """Test CreateDNSSEC endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "dnsse_cs.create_dnssec.11"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.dnsse_cs.create_dnssec(
            domain_name="domainName",
            algorithm=1,
            digest="x",
            digest_type=1,
            key_tag=1,
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/dnssec", None, 1)


def test_dnsseCs_create_dnssec_throws_gateway_timeout_error() -> None:
    """Test CreateDNSSEC endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "dnsse_cs.create_dnssec.12"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.dnsse_cs.create_dnssec(
            domain_name="domainName",
            algorithm=1,
            digest="x",
            digest_type=1,
            key_tag=1,
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/dnssec", None, 1)


def test_dnsseCs_get_dnssec() -> None:
    """Test GetDNSSEC endpoint with WireMock"""
    test_id = "dnsse_cs.get_dnssec.0"
    client = get_client(test_id)
    client.dnsse_cs.get_dnssec(
        domain_name="domainName",
        digest="digest",
    )
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/dnssec/digest", None, 1)


def test_dnsseCs_get_dnssec_throws_unauthorized_error() -> None:
    """Test GetDNSSEC endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "dnsse_cs.get_dnssec.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.dnsse_cs.get_dnssec(
            domain_name="domainName",
            digest="digest",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/dnssec/digest", None, 1)


def test_dnsseCs_get_dnssec_throws_forbidden_error() -> None:
    """Test GetDNSSEC endpoint error response (ForbiddenError) with WireMock"""
    test_id = "dnsse_cs.get_dnssec.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.dnsse_cs.get_dnssec(
            domain_name="domainName",
            digest="digest",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/dnssec/digest", None, 1)


def test_dnsseCs_get_dnssec_throws_not_found_error() -> None:
    """Test GetDNSSEC endpoint error response (NotFoundError) with WireMock"""
    test_id = "dnsse_cs.get_dnssec.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.dnsse_cs.get_dnssec(
            domain_name="domainName",
            digest="digest",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/dnssec/digest", None, 1)


def test_dnsseCs_get_dnssec_throws_method_not_allowed_error() -> None:
    """Test GetDNSSEC endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "dnsse_cs.get_dnssec.4"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.dnsse_cs.get_dnssec(
            domain_name="domainName",
            digest="digest",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/dnssec/digest", None, 1)


def test_dnsseCs_get_dnssec_throws_too_many_requests_error() -> None:
    """Test GetDNSSEC endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "dnsse_cs.get_dnssec.5"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.dnsse_cs.get_dnssec(
            domain_name="domainName",
            digest="digest",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/dnssec/digest", None, 1)


def test_dnsseCs_get_dnssec_throws_internal_server_error() -> None:
    """Test GetDNSSEC endpoint error response (InternalServerError) with WireMock"""
    test_id = "dnsse_cs.get_dnssec.6"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.dnsse_cs.get_dnssec(
            domain_name="domainName",
            digest="digest",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/dnssec/digest", None, 1)


def test_dnsseCs_get_dnssec_throws_bad_gateway_error() -> None:
    """Test GetDNSSEC endpoint error response (BadGatewayError) with WireMock"""
    test_id = "dnsse_cs.get_dnssec.7"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.dnsse_cs.get_dnssec(
            domain_name="domainName",
            digest="digest",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/dnssec/digest", None, 1)


def test_dnsseCs_get_dnssec_throws_service_unavailable_error() -> None:
    """Test GetDNSSEC endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "dnsse_cs.get_dnssec.8"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.dnsse_cs.get_dnssec(
            domain_name="domainName",
            digest="digest",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/dnssec/digest", None, 1)


def test_dnsseCs_get_dnssec_throws_gateway_timeout_error() -> None:
    """Test GetDNSSEC endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "dnsse_cs.get_dnssec.9"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.dnsse_cs.get_dnssec(
            domain_name="domainName",
            digest="digest",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/dnssec/digest", None, 1)


def test_dnsseCs_delete_dnssec() -> None:
    """Test DeleteDNSSEC endpoint with WireMock"""
    test_id = "dnsse_cs.delete_dnssec.0"
    client = get_client(test_id)
    client.dnsse_cs.delete_dnssec(
        domain_name="domainName",
        digest="digest",
    )
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/dnssec/digest", None, 1)


def test_dnsseCs_delete_dnssec_throws_unauthorized_error() -> None:
    """Test DeleteDNSSEC endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "dnsse_cs.delete_dnssec.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.dnsse_cs.delete_dnssec(
            domain_name="domainName",
            digest="digest",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/dnssec/digest", None, 1)


def test_dnsseCs_delete_dnssec_throws_forbidden_error() -> None:
    """Test DeleteDNSSEC endpoint error response (ForbiddenError) with WireMock"""
    test_id = "dnsse_cs.delete_dnssec.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.dnsse_cs.delete_dnssec(
            domain_name="domainName",
            digest="digest",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/dnssec/digest", None, 1)


def test_dnsseCs_delete_dnssec_throws_not_found_error() -> None:
    """Test DeleteDNSSEC endpoint error response (NotFoundError) with WireMock"""
    test_id = "dnsse_cs.delete_dnssec.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.dnsse_cs.delete_dnssec(
            domain_name="domainName",
            digest="digest",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/dnssec/digest", None, 1)


def test_dnsseCs_delete_dnssec_throws_method_not_allowed_error() -> None:
    """Test DeleteDNSSEC endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "dnsse_cs.delete_dnssec.4"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.dnsse_cs.delete_dnssec(
            domain_name="domainName",
            digest="digest",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/dnssec/digest", None, 1)


def test_dnsseCs_delete_dnssec_throws_too_many_requests_error() -> None:
    """Test DeleteDNSSEC endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "dnsse_cs.delete_dnssec.5"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.dnsse_cs.delete_dnssec(
            domain_name="domainName",
            digest="digest",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/dnssec/digest", None, 1)


def test_dnsseCs_delete_dnssec_throws_internal_server_error() -> None:
    """Test DeleteDNSSEC endpoint error response (InternalServerError) with WireMock"""
    test_id = "dnsse_cs.delete_dnssec.6"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.dnsse_cs.delete_dnssec(
            domain_name="domainName",
            digest="digest",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/dnssec/digest", None, 1)


def test_dnsseCs_delete_dnssec_throws_bad_gateway_error() -> None:
    """Test DeleteDNSSEC endpoint error response (BadGatewayError) with WireMock"""
    test_id = "dnsse_cs.delete_dnssec.7"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.dnsse_cs.delete_dnssec(
            domain_name="domainName",
            digest="digest",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/dnssec/digest", None, 1)


def test_dnsseCs_delete_dnssec_throws_service_unavailable_error() -> None:
    """Test DeleteDNSSEC endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "dnsse_cs.delete_dnssec.8"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.dnsse_cs.delete_dnssec(
            domain_name="domainName",
            digest="digest",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/dnssec/digest", None, 1)


def test_dnsseCs_delete_dnssec_throws_gateway_timeout_error() -> None:
    """Test DeleteDNSSEC endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "dnsse_cs.delete_dnssec.9"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.dnsse_cs.delete_dnssec(
            domain_name="domainName",
            digest="digest",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/dnssec/digest", None, 1)

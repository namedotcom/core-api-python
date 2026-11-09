import pytest
from .conftest import get_client, verify_request_count

from namecom_core_api import (
    BadGatewayError,
    BadRequestError,
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


def test_dns_list_records() -> None:
    """Test ListRecords endpoint with WireMock"""
    test_id = "dns.list_records.0"
    client = get_client(test_id)
    client.dns.list_records(
        domain_name="domainName",
    )
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/records", None, 1)


def test_dns_list_records_throws_bad_request_error() -> None:
    """Test ListRecords endpoint error response (BadRequestError) with WireMock"""
    test_id = "dns.list_records.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.dns.list_records(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/records", None, 1)


def test_dns_list_records_throws_unauthorized_error() -> None:
    """Test ListRecords endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "dns.list_records.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.dns.list_records(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/records", None, 1)


def test_dns_list_records_throws_forbidden_error() -> None:
    """Test ListRecords endpoint error response (ForbiddenError) with WireMock"""
    test_id = "dns.list_records.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.dns.list_records(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/records", None, 1)


def test_dns_list_records_throws_not_found_error() -> None:
    """Test ListRecords endpoint error response (NotFoundError) with WireMock"""
    test_id = "dns.list_records.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.dns.list_records(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/records", None, 1)


def test_dns_list_records_throws_method_not_allowed_error() -> None:
    """Test ListRecords endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "dns.list_records.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.dns.list_records(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/records", None, 1)


def test_dns_list_records_throws_too_many_requests_error() -> None:
    """Test ListRecords endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "dns.list_records.6"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.dns.list_records(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/records", None, 1)


def test_dns_list_records_throws_internal_server_error() -> None:
    """Test ListRecords endpoint error response (InternalServerError) with WireMock"""
    test_id = "dns.list_records.7"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.dns.list_records(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/records", None, 1)


def test_dns_list_records_throws_bad_gateway_error() -> None:
    """Test ListRecords endpoint error response (BadGatewayError) with WireMock"""
    test_id = "dns.list_records.8"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.dns.list_records(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/records", None, 1)


def test_dns_list_records_throws_service_unavailable_error() -> None:
    """Test ListRecords endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "dns.list_records.9"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.dns.list_records(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/records", None, 1)


def test_dns_list_records_throws_gateway_timeout_error() -> None:
    """Test ListRecords endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "dns.list_records.10"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.dns.list_records(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/records", None, 1)


def test_dns_create_record() -> None:
    """Test CreateRecord endpoint with WireMock"""
    test_id = "dns.create_record.0"
    client = get_client(test_id)
    client.dns.create_record(
        domain_name="domainName",
        answer="answer",
        host="host",
        type="A",
    )
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/records", None, 1)


def test_dns_create_record_throws_bad_request_error() -> None:
    """Test CreateRecord endpoint error response (BadRequestError) with WireMock"""
    test_id = "dns.create_record.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.dns.create_record(
            domain_name="domainName",
            answer="x",
            host="host",
            type="A",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/records", None, 1)


def test_dns_create_record_throws_unauthorized_error() -> None:
    """Test CreateRecord endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "dns.create_record.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.dns.create_record(
            domain_name="domainName",
            answer="x",
            host="host",
            type="A",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/records", None, 1)


def test_dns_create_record_throws_forbidden_error() -> None:
    """Test CreateRecord endpoint error response (ForbiddenError) with WireMock"""
    test_id = "dns.create_record.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.dns.create_record(
            domain_name="domainName",
            answer="x",
            host="host",
            type="A",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/records", None, 1)


def test_dns_create_record_throws_not_found_error() -> None:
    """Test CreateRecord endpoint error response (NotFoundError) with WireMock"""
    test_id = "dns.create_record.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.dns.create_record(
            domain_name="domainName",
            answer="x",
            host="host",
            type="A",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/records", None, 1)


def test_dns_create_record_throws_method_not_allowed_error() -> None:
    """Test CreateRecord endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "dns.create_record.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.dns.create_record(
            domain_name="domainName",
            answer="x",
            host="host",
            type="A",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/records", None, 1)


def test_dns_create_record_throws_unsupported_media_type_error() -> None:
    """Test CreateRecord endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "dns.create_record.6"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.dns.create_record(
            domain_name="domainName",
            answer="x",
            host="host",
            type="A",
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/records", None, 1)


def test_dns_create_record_throws_too_many_requests_error() -> None:
    """Test CreateRecord endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "dns.create_record.7"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.dns.create_record(
            domain_name="domainName",
            answer="x",
            host="host",
            type="A",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/records", None, 1)


def test_dns_create_record_throws_internal_server_error() -> None:
    """Test CreateRecord endpoint error response (InternalServerError) with WireMock"""
    test_id = "dns.create_record.8"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.dns.create_record(
            domain_name="domainName",
            answer="x",
            host="host",
            type="A",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/records", None, 1)


def test_dns_create_record_throws_bad_gateway_error() -> None:
    """Test CreateRecord endpoint error response (BadGatewayError) with WireMock"""
    test_id = "dns.create_record.9"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.dns.create_record(
            domain_name="domainName",
            answer="x",
            host="host",
            type="A",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/records", None, 1)


def test_dns_create_record_throws_service_unavailable_error() -> None:
    """Test CreateRecord endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "dns.create_record.10"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.dns.create_record(
            domain_name="domainName",
            answer="x",
            host="host",
            type="A",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/records", None, 1)


def test_dns_create_record_throws_gateway_timeout_error() -> None:
    """Test CreateRecord endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "dns.create_record.11"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.dns.create_record(
            domain_name="domainName",
            answer="x",
            host="host",
            type="A",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/records", None, 1)


def test_dns_get_record() -> None:
    """Test GetRecord endpoint with WireMock"""
    test_id = "dns.get_record.0"
    client = get_client(test_id)
    client.dns.get_record(
        domain_name="domainName",
        id=1,
    )
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_get_record_throws_unauthorized_error() -> None:
    """Test GetRecord endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "dns.get_record.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.dns.get_record(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_get_record_throws_forbidden_error() -> None:
    """Test GetRecord endpoint error response (ForbiddenError) with WireMock"""
    test_id = "dns.get_record.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.dns.get_record(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_get_record_throws_not_found_error() -> None:
    """Test GetRecord endpoint error response (NotFoundError) with WireMock"""
    test_id = "dns.get_record.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.dns.get_record(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_get_record_throws_method_not_allowed_error() -> None:
    """Test GetRecord endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "dns.get_record.4"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.dns.get_record(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_get_record_throws_too_many_requests_error() -> None:
    """Test GetRecord endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "dns.get_record.5"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.dns.get_record(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_get_record_throws_internal_server_error() -> None:
    """Test GetRecord endpoint error response (InternalServerError) with WireMock"""
    test_id = "dns.get_record.6"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.dns.get_record(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_get_record_throws_bad_gateway_error() -> None:
    """Test GetRecord endpoint error response (BadGatewayError) with WireMock"""
    test_id = "dns.get_record.7"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.dns.get_record(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_get_record_throws_service_unavailable_error() -> None:
    """Test GetRecord endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "dns.get_record.8"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.dns.get_record(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_get_record_throws_gateway_timeout_error() -> None:
    """Test GetRecord endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "dns.get_record.9"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.dns.get_record(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_update_record() -> None:
    """Test UpdateRecord endpoint with WireMock"""
    test_id = "dns.update_record.0"
    client = get_client(test_id)
    client.dns.update_record(
        domain_name="domainName",
        id=1,
        answer="answer",
        type="A",
    )
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_update_record_throws_bad_request_error() -> None:
    """Test UpdateRecord endpoint error response (BadRequestError) with WireMock"""
    test_id = "dns.update_record.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.dns.update_record(
            domain_name="domainName",
            id=1,
            answer="x",
            type="A",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_update_record_throws_unauthorized_error() -> None:
    """Test UpdateRecord endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "dns.update_record.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.dns.update_record(
            domain_name="domainName",
            id=1,
            answer="x",
            type="A",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_update_record_throws_forbidden_error() -> None:
    """Test UpdateRecord endpoint error response (ForbiddenError) with WireMock"""
    test_id = "dns.update_record.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.dns.update_record(
            domain_name="domainName",
            id=1,
            answer="x",
            type="A",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_update_record_throws_not_found_error() -> None:
    """Test UpdateRecord endpoint error response (NotFoundError) with WireMock"""
    test_id = "dns.update_record.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.dns.update_record(
            domain_name="domainName",
            id=1,
            answer="x",
            type="A",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_update_record_throws_method_not_allowed_error() -> None:
    """Test UpdateRecord endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "dns.update_record.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.dns.update_record(
            domain_name="domainName",
            id=1,
            answer="x",
            type="A",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_update_record_throws_unsupported_media_type_error() -> None:
    """Test UpdateRecord endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "dns.update_record.6"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.dns.update_record(
            domain_name="domainName",
            id=1,
            answer="x",
            type="A",
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_update_record_throws_too_many_requests_error() -> None:
    """Test UpdateRecord endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "dns.update_record.7"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.dns.update_record(
            domain_name="domainName",
            id=1,
            answer="x",
            type="A",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_update_record_throws_internal_server_error() -> None:
    """Test UpdateRecord endpoint error response (InternalServerError) with WireMock"""
    test_id = "dns.update_record.8"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.dns.update_record(
            domain_name="domainName",
            id=1,
            answer="x",
            type="A",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_update_record_throws_bad_gateway_error() -> None:
    """Test UpdateRecord endpoint error response (BadGatewayError) with WireMock"""
    test_id = "dns.update_record.9"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.dns.update_record(
            domain_name="domainName",
            id=1,
            answer="x",
            type="A",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_update_record_throws_service_unavailable_error() -> None:
    """Test UpdateRecord endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "dns.update_record.10"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.dns.update_record(
            domain_name="domainName",
            id=1,
            answer="x",
            type="A",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_update_record_throws_gateway_timeout_error() -> None:
    """Test UpdateRecord endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "dns.update_record.11"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.dns.update_record(
            domain_name="domainName",
            id=1,
            answer="x",
            type="A",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_delete_record() -> None:
    """Test DeleteRecord endpoint with WireMock"""
    test_id = "dns.delete_record.0"
    client = get_client(test_id)
    client.dns.delete_record(
        domain_name="domainName",
        id=1,
    )
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_delete_record_throws_bad_request_error() -> None:
    """Test DeleteRecord endpoint error response (BadRequestError) with WireMock"""
    test_id = "dns.delete_record.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.dns.delete_record(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_delete_record_throws_unauthorized_error() -> None:
    """Test DeleteRecord endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "dns.delete_record.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.dns.delete_record(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_delete_record_throws_forbidden_error() -> None:
    """Test DeleteRecord endpoint error response (ForbiddenError) with WireMock"""
    test_id = "dns.delete_record.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.dns.delete_record(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_delete_record_throws_not_found_error() -> None:
    """Test DeleteRecord endpoint error response (NotFoundError) with WireMock"""
    test_id = "dns.delete_record.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.dns.delete_record(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_delete_record_throws_method_not_allowed_error() -> None:
    """Test DeleteRecord endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "dns.delete_record.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.dns.delete_record(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_delete_record_throws_too_many_requests_error() -> None:
    """Test DeleteRecord endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "dns.delete_record.6"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.dns.delete_record(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_delete_record_throws_internal_server_error() -> None:
    """Test DeleteRecord endpoint error response (InternalServerError) with WireMock"""
    test_id = "dns.delete_record.7"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.dns.delete_record(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_delete_record_throws_bad_gateway_error() -> None:
    """Test DeleteRecord endpoint error response (BadGatewayError) with WireMock"""
    test_id = "dns.delete_record.8"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.dns.delete_record(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_delete_record_throws_service_unavailable_error() -> None:
    """Test DeleteRecord endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "dns.delete_record.9"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.dns.delete_record(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/records/1", None, 1)


def test_dns_delete_record_throws_gateway_timeout_error() -> None:
    """Test DeleteRecord endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "dns.delete_record.10"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.dns.delete_record(
            domain_name="domainName",
            id=1,
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/records/1", None, 1)

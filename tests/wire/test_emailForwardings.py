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


def test_emailForwardings_list_email_forwardings() -> None:
    """Test ListEmailForwardings endpoint with WireMock"""
    test_id = "email_forwardings.list_email_forwardings.0"
    client = get_client(test_id)
    client.email_forwardings.list_email_forwardings(
        domain_name="domainName",
        per_page=100,
        page=1,
    )
    verify_request_count(
        test_id, "GET", "/core/v1/domains/domainName/email/forwarding", {"perPage": "100", "page": "1"}, 1
    )


def test_emailForwardings_list_email_forwardings_throws_bad_request_error() -> None:
    """Test ListEmailForwardings endpoint error response (BadRequestError) with WireMock"""
    test_id = "email_forwardings.list_email_forwardings.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.email_forwardings.list_email_forwardings(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/email/forwarding", None, 1)


def test_emailForwardings_list_email_forwardings_throws_unauthorized_error() -> None:
    """Test ListEmailForwardings endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "email_forwardings.list_email_forwardings.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.email_forwardings.list_email_forwardings(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/email/forwarding", None, 1)


def test_emailForwardings_list_email_forwardings_throws_forbidden_error() -> None:
    """Test ListEmailForwardings endpoint error response (ForbiddenError) with WireMock"""
    test_id = "email_forwardings.list_email_forwardings.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.email_forwardings.list_email_forwardings(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/email/forwarding", None, 1)


def test_emailForwardings_list_email_forwardings_throws_not_found_error() -> None:
    """Test ListEmailForwardings endpoint error response (NotFoundError) with WireMock"""
    test_id = "email_forwardings.list_email_forwardings.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.email_forwardings.list_email_forwardings(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/email/forwarding", None, 1)


def test_emailForwardings_list_email_forwardings_throws_method_not_allowed_error() -> None:
    """Test ListEmailForwardings endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "email_forwardings.list_email_forwardings.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.email_forwardings.list_email_forwardings(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/email/forwarding", None, 1)


def test_emailForwardings_list_email_forwardings_throws_too_many_requests_error() -> None:
    """Test ListEmailForwardings endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "email_forwardings.list_email_forwardings.6"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.email_forwardings.list_email_forwardings(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/email/forwarding", None, 1)


def test_emailForwardings_list_email_forwardings_throws_internal_server_error() -> None:
    """Test ListEmailForwardings endpoint error response (InternalServerError) with WireMock"""
    test_id = "email_forwardings.list_email_forwardings.7"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.email_forwardings.list_email_forwardings(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/email/forwarding", None, 1)


def test_emailForwardings_list_email_forwardings_throws_bad_gateway_error() -> None:
    """Test ListEmailForwardings endpoint error response (BadGatewayError) with WireMock"""
    test_id = "email_forwardings.list_email_forwardings.8"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.email_forwardings.list_email_forwardings(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/email/forwarding", None, 1)


def test_emailForwardings_list_email_forwardings_throws_service_unavailable_error() -> None:
    """Test ListEmailForwardings endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "email_forwardings.list_email_forwardings.9"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.email_forwardings.list_email_forwardings(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/email/forwarding", None, 1)


def test_emailForwardings_list_email_forwardings_throws_gateway_timeout_error() -> None:
    """Test ListEmailForwardings endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "email_forwardings.list_email_forwardings.10"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.email_forwardings.list_email_forwardings(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/email/forwarding", None, 1)


def test_emailForwardings_create_email_forwarding() -> None:
    """Test CreateEmailForwarding endpoint with WireMock"""
    test_id = "email_forwardings.create_email_forwarding.0"
    client = get_client(test_id)
    client.email_forwardings.create_email_forwarding(
        domain_name="example.com",
        email_box="admin",
        email_to="webmaster@example.com",
    )
    verify_request_count(test_id, "POST", "/core/v1/domains/example.com/email/forwarding", None, 1)


def test_emailForwardings_create_email_forwarding_throws_bad_request_error() -> None:
    """Test CreateEmailForwarding endpoint error response (BadRequestError) with WireMock"""
    test_id = "email_forwardings.create_email_forwarding.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.email_forwardings.create_email_forwarding(
            domain_name="domainName",
            email_box="x",
            email_to="x",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/email/forwarding", None, 1)


def test_emailForwardings_create_email_forwarding_throws_unauthorized_error() -> None:
    """Test CreateEmailForwarding endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "email_forwardings.create_email_forwarding.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.email_forwardings.create_email_forwarding(
            domain_name="domainName",
            email_box="x",
            email_to="x",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/email/forwarding", None, 1)


def test_emailForwardings_create_email_forwarding_throws_forbidden_error() -> None:
    """Test CreateEmailForwarding endpoint error response (ForbiddenError) with WireMock"""
    test_id = "email_forwardings.create_email_forwarding.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.email_forwardings.create_email_forwarding(
            domain_name="domainName",
            email_box="x",
            email_to="x",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/email/forwarding", None, 1)


def test_emailForwardings_create_email_forwarding_throws_not_found_error() -> None:
    """Test CreateEmailForwarding endpoint error response (NotFoundError) with WireMock"""
    test_id = "email_forwardings.create_email_forwarding.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.email_forwardings.create_email_forwarding(
            domain_name="domainName",
            email_box="x",
            email_to="x",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/email/forwarding", None, 1)


def test_emailForwardings_create_email_forwarding_throws_method_not_allowed_error() -> None:
    """Test CreateEmailForwarding endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "email_forwardings.create_email_forwarding.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.email_forwardings.create_email_forwarding(
            domain_name="domainName",
            email_box="x",
            email_to="x",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/email/forwarding", None, 1)


def test_emailForwardings_create_email_forwarding_throws_unsupported_media_type_error() -> None:
    """Test CreateEmailForwarding endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "email_forwardings.create_email_forwarding.6"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.email_forwardings.create_email_forwarding(
            domain_name="domainName",
            email_box="x",
            email_to="x",
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/email/forwarding", None, 1)


def test_emailForwardings_create_email_forwarding_throws_too_many_requests_error() -> None:
    """Test CreateEmailForwarding endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "email_forwardings.create_email_forwarding.7"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.email_forwardings.create_email_forwarding(
            domain_name="domainName",
            email_box="x",
            email_to="x",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/email/forwarding", None, 1)


def test_emailForwardings_create_email_forwarding_throws_internal_server_error() -> None:
    """Test CreateEmailForwarding endpoint error response (InternalServerError) with WireMock"""
    test_id = "email_forwardings.create_email_forwarding.8"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.email_forwardings.create_email_forwarding(
            domain_name="domainName",
            email_box="x",
            email_to="x",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/email/forwarding", None, 1)


def test_emailForwardings_create_email_forwarding_throws_bad_gateway_error() -> None:
    """Test CreateEmailForwarding endpoint error response (BadGatewayError) with WireMock"""
    test_id = "email_forwardings.create_email_forwarding.9"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.email_forwardings.create_email_forwarding(
            domain_name="domainName",
            email_box="x",
            email_to="x",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/email/forwarding", None, 1)


def test_emailForwardings_create_email_forwarding_throws_service_unavailable_error() -> None:
    """Test CreateEmailForwarding endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "email_forwardings.create_email_forwarding.10"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.email_forwardings.create_email_forwarding(
            domain_name="domainName",
            email_box="x",
            email_to="x",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/email/forwarding", None, 1)


def test_emailForwardings_create_email_forwarding_throws_gateway_timeout_error() -> None:
    """Test CreateEmailForwarding endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "email_forwardings.create_email_forwarding.11"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.email_forwardings.create_email_forwarding(
            domain_name="domainName",
            email_box="x",
            email_to="x",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName/email/forwarding", None, 1)


def test_emailForwardings_get_email_forwarding() -> None:
    """Test GetEmailForwarding endpoint with WireMock"""
    test_id = "email_forwardings.get_email_forwarding.0"
    client = get_client(test_id)
    client.email_forwardings.get_email_forwarding(
        domain_name="domainName",
        email_box="emailBox",
    )
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_get_email_forwarding_throws_unauthorized_error() -> None:
    """Test GetEmailForwarding endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "email_forwardings.get_email_forwarding.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.email_forwardings.get_email_forwarding(
            domain_name="domainName",
            email_box="emailBox",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_get_email_forwarding_throws_forbidden_error() -> None:
    """Test GetEmailForwarding endpoint error response (ForbiddenError) with WireMock"""
    test_id = "email_forwardings.get_email_forwarding.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.email_forwardings.get_email_forwarding(
            domain_name="domainName",
            email_box="emailBox",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_get_email_forwarding_throws_not_found_error() -> None:
    """Test GetEmailForwarding endpoint error response (NotFoundError) with WireMock"""
    test_id = "email_forwardings.get_email_forwarding.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.email_forwardings.get_email_forwarding(
            domain_name="domainName",
            email_box="emailBox",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_get_email_forwarding_throws_method_not_allowed_error() -> None:
    """Test GetEmailForwarding endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "email_forwardings.get_email_forwarding.4"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.email_forwardings.get_email_forwarding(
            domain_name="domainName",
            email_box="emailBox",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_get_email_forwarding_throws_too_many_requests_error() -> None:
    """Test GetEmailForwarding endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "email_forwardings.get_email_forwarding.5"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.email_forwardings.get_email_forwarding(
            domain_name="domainName",
            email_box="emailBox",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_get_email_forwarding_throws_internal_server_error() -> None:
    """Test GetEmailForwarding endpoint error response (InternalServerError) with WireMock"""
    test_id = "email_forwardings.get_email_forwarding.6"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.email_forwardings.get_email_forwarding(
            domain_name="domainName",
            email_box="emailBox",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_get_email_forwarding_throws_bad_gateway_error() -> None:
    """Test GetEmailForwarding endpoint error response (BadGatewayError) with WireMock"""
    test_id = "email_forwardings.get_email_forwarding.7"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.email_forwardings.get_email_forwarding(
            domain_name="domainName",
            email_box="emailBox",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_get_email_forwarding_throws_service_unavailable_error() -> None:
    """Test GetEmailForwarding endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "email_forwardings.get_email_forwarding.8"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.email_forwardings.get_email_forwarding(
            domain_name="domainName",
            email_box="emailBox",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_get_email_forwarding_throws_gateway_timeout_error() -> None:
    """Test GetEmailForwarding endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "email_forwardings.get_email_forwarding.9"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.email_forwardings.get_email_forwarding(
            domain_name="domainName",
            email_box="emailBox",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_update_email_forwarding() -> None:
    """Test UpdateEmailForwarding endpoint with WireMock"""
    test_id = "email_forwardings.update_email_forwarding.0"
    client = get_client(test_id)
    client.email_forwardings.update_email_forwarding(
        domain_name="domainName",
        email_box="emailBox",
        email_to="emailTo",
    )
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_update_email_forwarding_throws_unauthorized_error() -> None:
    """Test UpdateEmailForwarding endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "email_forwardings.update_email_forwarding.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.email_forwardings.update_email_forwarding(
            domain_name="domainName",
            email_box="emailBox",
            email_to="x",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_update_email_forwarding_throws_forbidden_error() -> None:
    """Test UpdateEmailForwarding endpoint error response (ForbiddenError) with WireMock"""
    test_id = "email_forwardings.update_email_forwarding.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.email_forwardings.update_email_forwarding(
            domain_name="domainName",
            email_box="emailBox",
            email_to="x",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_update_email_forwarding_throws_not_found_error() -> None:
    """Test UpdateEmailForwarding endpoint error response (NotFoundError) with WireMock"""
    test_id = "email_forwardings.update_email_forwarding.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.email_forwardings.update_email_forwarding(
            domain_name="domainName",
            email_box="emailBox",
            email_to="x",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_update_email_forwarding_throws_method_not_allowed_error() -> None:
    """Test UpdateEmailForwarding endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "email_forwardings.update_email_forwarding.4"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.email_forwardings.update_email_forwarding(
            domain_name="domainName",
            email_box="emailBox",
            email_to="x",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_update_email_forwarding_throws_unsupported_media_type_error() -> None:
    """Test UpdateEmailForwarding endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "email_forwardings.update_email_forwarding.5"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.email_forwardings.update_email_forwarding(
            domain_name="domainName",
            email_box="emailBox",
            email_to="x",
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_update_email_forwarding_throws_too_many_requests_error() -> None:
    """Test UpdateEmailForwarding endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "email_forwardings.update_email_forwarding.6"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.email_forwardings.update_email_forwarding(
            domain_name="domainName",
            email_box="emailBox",
            email_to="x",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_update_email_forwarding_throws_internal_server_error() -> None:
    """Test UpdateEmailForwarding endpoint error response (InternalServerError) with WireMock"""
    test_id = "email_forwardings.update_email_forwarding.7"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.email_forwardings.update_email_forwarding(
            domain_name="domainName",
            email_box="emailBox",
            email_to="x",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_update_email_forwarding_throws_bad_gateway_error() -> None:
    """Test UpdateEmailForwarding endpoint error response (BadGatewayError) with WireMock"""
    test_id = "email_forwardings.update_email_forwarding.8"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.email_forwardings.update_email_forwarding(
            domain_name="domainName",
            email_box="emailBox",
            email_to="x",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_update_email_forwarding_throws_service_unavailable_error() -> None:
    """Test UpdateEmailForwarding endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "email_forwardings.update_email_forwarding.9"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.email_forwardings.update_email_forwarding(
            domain_name="domainName",
            email_box="emailBox",
            email_to="x",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_update_email_forwarding_throws_gateway_timeout_error() -> None:
    """Test UpdateEmailForwarding endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "email_forwardings.update_email_forwarding.10"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.email_forwardings.update_email_forwarding(
            domain_name="domainName",
            email_box="emailBox",
            email_to="x",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_delete_email_forwarding() -> None:
    """Test DeleteEmailForwarding endpoint with WireMock"""
    test_id = "email_forwardings.delete_email_forwarding.0"
    client = get_client(test_id)
    client.email_forwardings.delete_email_forwarding(
        domain_name="domainName",
        email_box="emailBox",
    )
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_delete_email_forwarding_throws_unauthorized_error() -> None:
    """Test DeleteEmailForwarding endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "email_forwardings.delete_email_forwarding.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.email_forwardings.delete_email_forwarding(
            domain_name="domainName",
            email_box="emailBox",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_delete_email_forwarding_throws_forbidden_error() -> None:
    """Test DeleteEmailForwarding endpoint error response (ForbiddenError) with WireMock"""
    test_id = "email_forwardings.delete_email_forwarding.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.email_forwardings.delete_email_forwarding(
            domain_name="domainName",
            email_box="emailBox",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_delete_email_forwarding_throws_not_found_error() -> None:
    """Test DeleteEmailForwarding endpoint error response (NotFoundError) with WireMock"""
    test_id = "email_forwardings.delete_email_forwarding.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.email_forwardings.delete_email_forwarding(
            domain_name="domainName",
            email_box="emailBox",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_delete_email_forwarding_throws_method_not_allowed_error() -> None:
    """Test DeleteEmailForwarding endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "email_forwardings.delete_email_forwarding.4"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.email_forwardings.delete_email_forwarding(
            domain_name="domainName",
            email_box="emailBox",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_delete_email_forwarding_throws_too_many_requests_error() -> None:
    """Test DeleteEmailForwarding endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "email_forwardings.delete_email_forwarding.5"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.email_forwardings.delete_email_forwarding(
            domain_name="domainName",
            email_box="emailBox",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_delete_email_forwarding_throws_internal_server_error() -> None:
    """Test DeleteEmailForwarding endpoint error response (InternalServerError) with WireMock"""
    test_id = "email_forwardings.delete_email_forwarding.6"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.email_forwardings.delete_email_forwarding(
            domain_name="domainName",
            email_box="emailBox",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_delete_email_forwarding_throws_bad_gateway_error() -> None:
    """Test DeleteEmailForwarding endpoint error response (BadGatewayError) with WireMock"""
    test_id = "email_forwardings.delete_email_forwarding.7"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.email_forwardings.delete_email_forwarding(
            domain_name="domainName",
            email_box="emailBox",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_delete_email_forwarding_throws_service_unavailable_error() -> None:
    """Test DeleteEmailForwarding endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "email_forwardings.delete_email_forwarding.8"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.email_forwardings.delete_email_forwarding(
            domain_name="domainName",
            email_box="emailBox",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)


def test_emailForwardings_delete_email_forwarding_throws_gateway_timeout_error() -> None:
    """Test DeleteEmailForwarding endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "email_forwardings.delete_email_forwarding.9"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.email_forwardings.delete_email_forwarding(
            domain_name="domainName",
            email_box="emailBox",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/domains/domainName/email/forwarding/emailBox", None, 1)

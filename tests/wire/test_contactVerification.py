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


def test_contactVerification_unverified_contacts_list() -> None:
    """Test UnverifiedContactsList endpoint with WireMock"""
    test_id = "contact_verification.unverified_contacts_list.0"
    client = get_client(test_id)
    client.contact_verification.unverified_contacts_list(
        per_page=100,
        page=2,
    )
    verify_request_count(test_id, "GET", "/core/v1/contacts/unverified", {"perPage": "100", "page": "2"}, 1)


def test_contactVerification_unverified_contacts_list_throws_bad_request_error() -> None:
    """Test UnverifiedContactsList endpoint error response (BadRequestError) with WireMock"""
    test_id = "contact_verification.unverified_contacts_list.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.contact_verification.unverified_contacts_list()
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/contacts/unverified", None, 1)


def test_contactVerification_unverified_contacts_list_throws_unauthorized_error() -> None:
    """Test UnverifiedContactsList endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "contact_verification.unverified_contacts_list.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.contact_verification.unverified_contacts_list()
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/contacts/unverified", None, 1)


def test_contactVerification_unverified_contacts_list_throws_forbidden_error() -> None:
    """Test UnverifiedContactsList endpoint error response (ForbiddenError) with WireMock"""
    test_id = "contact_verification.unverified_contacts_list.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.contact_verification.unverified_contacts_list()
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/contacts/unverified", None, 1)


def test_contactVerification_unverified_contacts_list_throws_method_not_allowed_error() -> None:
    """Test UnverifiedContactsList endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "contact_verification.unverified_contacts_list.4"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.contact_verification.unverified_contacts_list()
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/contacts/unverified", None, 1)


def test_contactVerification_unverified_contacts_list_throws_too_many_requests_error() -> None:
    """Test UnverifiedContactsList endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "contact_verification.unverified_contacts_list.5"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.contact_verification.unverified_contacts_list()
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/contacts/unverified", None, 1)


def test_contactVerification_unverified_contacts_list_throws_internal_server_error() -> None:
    """Test UnverifiedContactsList endpoint error response (InternalServerError) with WireMock"""
    test_id = "contact_verification.unverified_contacts_list.6"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.contact_verification.unverified_contacts_list()
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/contacts/unverified", None, 1)


def test_contactVerification_unverified_contacts_list_throws_bad_gateway_error() -> None:
    """Test UnverifiedContactsList endpoint error response (BadGatewayError) with WireMock"""
    test_id = "contact_verification.unverified_contacts_list.7"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.contact_verification.unverified_contacts_list()
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/contacts/unverified", None, 1)


def test_contactVerification_unverified_contacts_list_throws_service_unavailable_error() -> None:
    """Test UnverifiedContactsList endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "contact_verification.unverified_contacts_list.8"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.contact_verification.unverified_contacts_list()
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/contacts/unverified", None, 1)


def test_contactVerification_unverified_contacts_list_throws_gateway_timeout_error() -> None:
    """Test UnverifiedContactsList endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "contact_verification.unverified_contacts_list.9"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.contact_verification.unverified_contacts_list()
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/contacts/unverified", None, 1)


def test_contactVerification_verify_contact() -> None:
    """Test VerifyContact endpoint with WireMock"""
    test_id = "contact_verification.verify_contact.0"
    client = get_client(test_id)
    client.contact_verification.verify_contact(
        verification_id=1,
    )
    verify_request_count(test_id, "POST", "/core/v1/contacts/verify/1", None, 1)


def test_contactVerification_verify_contact_throws_unauthorized_error() -> None:
    """Test VerifyContact endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "contact_verification.verify_contact.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.contact_verification.verify_contact(
            verification_id=1,
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/contacts/verify/1", None, 1)


def test_contactVerification_verify_contact_throws_forbidden_error() -> None:
    """Test VerifyContact endpoint error response (ForbiddenError) with WireMock"""
    test_id = "contact_verification.verify_contact.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.contact_verification.verify_contact(
            verification_id=1,
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/contacts/verify/1", None, 1)


def test_contactVerification_verify_contact_throws_not_found_error() -> None:
    """Test VerifyContact endpoint error response (NotFoundError) with WireMock"""
    test_id = "contact_verification.verify_contact.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.contact_verification.verify_contact(
            verification_id=1,
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/contacts/verify/1", None, 1)


def test_contactVerification_verify_contact_throws_method_not_allowed_error() -> None:
    """Test VerifyContact endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "contact_verification.verify_contact.4"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.contact_verification.verify_contact(
            verification_id=1,
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/contacts/verify/1", None, 1)


def test_contactVerification_verify_contact_throws_conflict_error() -> None:
    """Test VerifyContact endpoint error response (ConflictError) with WireMock"""
    test_id = "contact_verification.verify_contact.5"
    client = get_client(test_id)
    with pytest.raises(ConflictError) as exc_info:
        client.contact_verification.verify_contact(
            verification_id=1,
        )
    assert exc_info.value.status_code == 409
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/contacts/verify/1", None, 1)


def test_contactVerification_verify_contact_throws_unsupported_media_type_error() -> None:
    """Test VerifyContact endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "contact_verification.verify_contact.6"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.contact_verification.verify_contact(
            verification_id=1,
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/contacts/verify/1", None, 1)


def test_contactVerification_verify_contact_throws_too_many_requests_error() -> None:
    """Test VerifyContact endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "contact_verification.verify_contact.7"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.contact_verification.verify_contact(
            verification_id=1,
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/contacts/verify/1", None, 1)


def test_contactVerification_verify_contact_throws_internal_server_error() -> None:
    """Test VerifyContact endpoint error response (InternalServerError) with WireMock"""
    test_id = "contact_verification.verify_contact.8"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.contact_verification.verify_contact(
            verification_id=1,
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/contacts/verify/1", None, 1)


def test_contactVerification_verify_contact_throws_bad_gateway_error() -> None:
    """Test VerifyContact endpoint error response (BadGatewayError) with WireMock"""
    test_id = "contact_verification.verify_contact.9"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.contact_verification.verify_contact(
            verification_id=1,
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/contacts/verify/1", None, 1)


def test_contactVerification_verify_contact_throws_service_unavailable_error() -> None:
    """Test VerifyContact endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "contact_verification.verify_contact.10"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.contact_verification.verify_contact(
            verification_id=1,
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/contacts/verify/1", None, 1)


def test_contactVerification_verify_contact_throws_gateway_timeout_error() -> None:
    """Test VerifyContact endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "contact_verification.verify_contact.11"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.contact_verification.verify_contact(
            verification_id=1,
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/contacts/verify/1", None, 1)


def test_contactVerification_resend_contact_verification_email() -> None:
    """Test ResendContactVerificationEmail endpoint with WireMock"""
    test_id = "contact_verification.resend_contact_verification_email.0"
    client = get_client(test_id)
    client.contact_verification.resend_contact_verification_email(
        verification_id=1,
    )
    verify_request_count(test_id, "POST", "/core/v1/contacts/verify/1:resend", None, 1)


def test_contactVerification_resend_contact_verification_email_no_op_already_verified_nothing_to_send() -> None:
    """Test ResendContactVerificationEmail endpoint (No-op (already verified / nothing to send) example) with WireMock"""
    test_id = "contact_verification.resend_contact_verification_email.1"
    client = get_client(test_id)
    client.contact_verification.resend_contact_verification_email(
        verification_id=1,
    )
    verify_request_count(test_id, "POST", "/core/v1/contacts/verify/1:resend", None, 1)


def test_contactVerification_resend_contact_verification_email_throws_unauthorized_error() -> None:
    """Test ResendContactVerificationEmail endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "contact_verification.resend_contact_verification_email.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.contact_verification.resend_contact_verification_email(
            verification_id=1,
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/contacts/verify/1:resend", None, 1)


def test_contactVerification_resend_contact_verification_email_throws_forbidden_error() -> None:
    """Test ResendContactVerificationEmail endpoint error response (ForbiddenError) with WireMock"""
    test_id = "contact_verification.resend_contact_verification_email.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.contact_verification.resend_contact_verification_email(
            verification_id=1,
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/contacts/verify/1:resend", None, 1)


def test_contactVerification_resend_contact_verification_email_throws_not_found_error() -> None:
    """Test ResendContactVerificationEmail endpoint error response (NotFoundError) with WireMock"""
    test_id = "contact_verification.resend_contact_verification_email.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.contact_verification.resend_contact_verification_email(
            verification_id=1,
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/contacts/verify/1:resend", None, 1)


def test_contactVerification_resend_contact_verification_email_throws_method_not_allowed_error() -> None:
    """Test ResendContactVerificationEmail endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "contact_verification.resend_contact_verification_email.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.contact_verification.resend_contact_verification_email(
            verification_id=1,
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/contacts/verify/1:resend", None, 1)


def test_contactVerification_resend_contact_verification_email_throws_conflict_error() -> None:
    """Test ResendContactVerificationEmail endpoint error response (ConflictError) with WireMock"""
    test_id = "contact_verification.resend_contact_verification_email.6"
    client = get_client(test_id)
    with pytest.raises(ConflictError) as exc_info:
        client.contact_verification.resend_contact_verification_email(
            verification_id=1,
        )
    assert exc_info.value.status_code == 409
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/contacts/verify/1:resend", None, 1)


def test_contactVerification_resend_contact_verification_email_throws_unsupported_media_type_error() -> None:
    """Test ResendContactVerificationEmail endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "contact_verification.resend_contact_verification_email.7"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.contact_verification.resend_contact_verification_email(
            verification_id=1,
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/contacts/verify/1:resend", None, 1)


def test_contactVerification_resend_contact_verification_email_throws_too_many_requests_error() -> None:
    """Test ResendContactVerificationEmail endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "contact_verification.resend_contact_verification_email.8"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.contact_verification.resend_contact_verification_email(
            verification_id=1,
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/contacts/verify/1:resend", None, 1)


def test_contactVerification_resend_contact_verification_email_throws_internal_server_error() -> None:
    """Test ResendContactVerificationEmail endpoint error response (InternalServerError) with WireMock"""
    test_id = "contact_verification.resend_contact_verification_email.9"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.contact_verification.resend_contact_verification_email(
            verification_id=1,
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/contacts/verify/1:resend", None, 1)


def test_contactVerification_resend_contact_verification_email_throws_bad_gateway_error() -> None:
    """Test ResendContactVerificationEmail endpoint error response (BadGatewayError) with WireMock"""
    test_id = "contact_verification.resend_contact_verification_email.10"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.contact_verification.resend_contact_verification_email(
            verification_id=1,
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/contacts/verify/1:resend", None, 1)


def test_contactVerification_resend_contact_verification_email_throws_service_unavailable_error() -> None:
    """Test ResendContactVerificationEmail endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "contact_verification.resend_contact_verification_email.11"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.contact_verification.resend_contact_verification_email(
            verification_id=1,
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/contacts/verify/1:resend", None, 1)


def test_contactVerification_resend_contact_verification_email_throws_gateway_timeout_error() -> None:
    """Test ResendContactVerificationEmail endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "contact_verification.resend_contact_verification_email.12"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.contact_verification.resend_contact_verification_email(
            verification_id=1,
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/contacts/verify/1:resend", None, 1)

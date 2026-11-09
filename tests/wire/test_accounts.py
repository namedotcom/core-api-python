import pytest
from .conftest import get_client, verify_request_count

from namecom_core_api import (
    AccountRequest,
    BadGatewayError,
    BadRequestError,
    ContactsRequest,
    ForbiddenError,
    GatewayTimeoutError,
    InternalServerError,
    MethodNotAllowedError,
    RegistrantContactRequest,
    ServiceUnavailableError,
    TooManyRequestsError,
    UnauthorizedError,
    UnsupportedMediaTypeError,
)
from namecom_core_api.core.jsonable_encoder import jsonable_encoder


def test_accounts_create_account() -> None:
    """Test CreateAccount endpoint with WireMock"""
    test_id = "accounts.create_account.0"
    client = get_client(test_id)
    client.accounts.create_account(
        account=AccountRequest(
            contacts=ContactsRequest(
                registrant=RegistrantContactRequest(
                    first_name="Jane",
                    last_name="Doe",
                    address1="123 Main St.",
                    city="Denver",
                    state="CO",
                    zip="12345",
                    country="US",
                    email="admin@example.net",
                    phone="+13035551212",
                ),
            ),
            account_name="reseller_subaccount",
            password="SecureP4ss!",
        ),
        api_tos=True,
        tos=True,
    )
    verify_request_count(test_id, "POST", "/core/v1/accounts", None, 1)


def test_accounts_create_account_throws_bad_request_error() -> None:
    """Test CreateAccount endpoint error response (BadRequestError) with WireMock"""
    test_id = "accounts.create_account.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.accounts.create_account(
            account=AccountRequest(),
            api_tos=True,
            tos=True,
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/accounts", None, 1)


def test_accounts_create_account_throws_unauthorized_error() -> None:
    """Test CreateAccount endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "accounts.create_account.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.accounts.create_account(
            account=AccountRequest(),
            api_tos=True,
            tos=True,
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/accounts", None, 1)


def test_accounts_create_account_throws_forbidden_error() -> None:
    """Test CreateAccount endpoint error response (ForbiddenError) with WireMock"""
    test_id = "accounts.create_account.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.accounts.create_account(
            account=AccountRequest(),
            api_tos=True,
            tos=True,
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/accounts", None, 1)


def test_accounts_create_account_throws_method_not_allowed_error() -> None:
    """Test CreateAccount endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "accounts.create_account.4"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.accounts.create_account(
            account=AccountRequest(),
            api_tos=True,
            tos=True,
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/accounts", None, 1)


def test_accounts_create_account_throws_unsupported_media_type_error() -> None:
    """Test CreateAccount endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "accounts.create_account.5"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.accounts.create_account(
            account=AccountRequest(),
            api_tos=True,
            tos=True,
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/accounts", None, 1)


def test_accounts_create_account_throws_too_many_requests_error() -> None:
    """Test CreateAccount endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "accounts.create_account.6"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.accounts.create_account(
            account=AccountRequest(),
            api_tos=True,
            tos=True,
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/accounts", None, 1)


def test_accounts_create_account_throws_internal_server_error() -> None:
    """Test CreateAccount endpoint error response (InternalServerError) with WireMock"""
    test_id = "accounts.create_account.7"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.accounts.create_account(
            account=AccountRequest(),
            api_tos=True,
            tos=True,
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/accounts", None, 1)


def test_accounts_create_account_throws_bad_gateway_error() -> None:
    """Test CreateAccount endpoint error response (BadGatewayError) with WireMock"""
    test_id = "accounts.create_account.8"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.accounts.create_account(
            account=AccountRequest(),
            api_tos=True,
            tos=True,
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/accounts", None, 1)


def test_accounts_create_account_throws_service_unavailable_error() -> None:
    """Test CreateAccount endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "accounts.create_account.9"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.accounts.create_account(
            account=AccountRequest(),
            api_tos=True,
            tos=True,
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/accounts", None, 1)


def test_accounts_create_account_throws_gateway_timeout_error() -> None:
    """Test CreateAccount endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "accounts.create_account.10"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.accounts.create_account(
            account=AccountRequest(),
            api_tos=True,
            tos=True,
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/accounts", None, 1)

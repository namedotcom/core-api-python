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
    PaymentRequiredError,
    ServiceUnavailableError,
    TooManyRequestsError,
    UnauthorizedError,
    UnprocessableEntityError,
    UnsupportedMediaTypeError,
)
from namecom_core_api.core.jsonable_encoder import jsonable_encoder


def test_transfers_list_transfers() -> None:
    """Test ListTransfers endpoint with WireMock"""
    test_id = "transfers.list_transfers.0"
    client = get_client(test_id)
    client.transfers.list_transfers()
    verify_request_count(test_id, "GET", "/core/v1/transfers", None, 1)


def test_transfers_list_transfers_throws_bad_request_error() -> None:
    """Test ListTransfers endpoint error response (BadRequestError) with WireMock"""
    test_id = "transfers.list_transfers.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.transfers.list_transfers()
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/transfers", None, 1)


def test_transfers_list_transfers_throws_unauthorized_error() -> None:
    """Test ListTransfers endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "transfers.list_transfers.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.transfers.list_transfers()
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/transfers", None, 1)


def test_transfers_list_transfers_throws_payment_required_error() -> None:
    """Test ListTransfers endpoint error response (PaymentRequiredError) with WireMock"""
    test_id = "transfers.list_transfers.3"
    client = get_client(test_id)
    with pytest.raises(PaymentRequiredError) as exc_info:
        client.transfers.list_transfers()
    assert exc_info.value.status_code == 402
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/transfers", None, 1)


def test_transfers_list_transfers_throws_forbidden_error() -> None:
    """Test ListTransfers endpoint error response (ForbiddenError) with WireMock"""
    test_id = "transfers.list_transfers.4"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.transfers.list_transfers()
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/transfers", None, 1)


def test_transfers_list_transfers_throws_method_not_allowed_error() -> None:
    """Test ListTransfers endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "transfers.list_transfers.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.transfers.list_transfers()
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/transfers", None, 1)


def test_transfers_list_transfers_throws_too_many_requests_error() -> None:
    """Test ListTransfers endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "transfers.list_transfers.6"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.transfers.list_transfers()
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/transfers", None, 1)


def test_transfers_list_transfers_throws_internal_server_error() -> None:
    """Test ListTransfers endpoint error response (InternalServerError) with WireMock"""
    test_id = "transfers.list_transfers.7"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.transfers.list_transfers()
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/transfers", None, 1)


def test_transfers_list_transfers_throws_bad_gateway_error() -> None:
    """Test ListTransfers endpoint error response (BadGatewayError) with WireMock"""
    test_id = "transfers.list_transfers.8"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.transfers.list_transfers()
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/transfers", None, 1)


def test_transfers_list_transfers_throws_service_unavailable_error() -> None:
    """Test ListTransfers endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "transfers.list_transfers.9"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.transfers.list_transfers()
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/transfers", None, 1)


def test_transfers_list_transfers_throws_gateway_timeout_error() -> None:
    """Test ListTransfers endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "transfers.list_transfers.10"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.transfers.list_transfers()
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/transfers", None, 1)


def test_transfers_create_transfer() -> None:
    """Test CreateTransfer endpoint with WireMock"""
    test_id = "transfers.create_transfer.0"
    client = get_client(test_id)
    client.transfers.create_transfer(
        auth_code="ABC123",
        domain_name="example.com",
    )
    verify_request_count(test_id, "POST", "/core/v1/transfers", None, 1)


def test_transfers_create_transfer_throws_bad_request_error() -> None:
    """Test CreateTransfer endpoint error response (BadRequestError) with WireMock"""
    test_id = "transfers.create_transfer.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.transfers.create_transfer(
            auth_code="x",
            domain_name="x",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers", None, 1)


def test_transfers_create_transfer_throws_unauthorized_error() -> None:
    """Test CreateTransfer endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "transfers.create_transfer.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.transfers.create_transfer(
            auth_code="x",
            domain_name="x",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers", None, 1)


def test_transfers_create_transfer_throws_payment_required_error() -> None:
    """Test CreateTransfer endpoint error response (PaymentRequiredError) with WireMock"""
    test_id = "transfers.create_transfer.3"
    client = get_client(test_id)
    with pytest.raises(PaymentRequiredError) as exc_info:
        client.transfers.create_transfer(
            auth_code="x",
            domain_name="x",
        )
    assert exc_info.value.status_code == 402
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers", None, 1)


def test_transfers_create_transfer_throws_forbidden_error() -> None:
    """Test CreateTransfer endpoint error response (ForbiddenError) with WireMock"""
    test_id = "transfers.create_transfer.4"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.transfers.create_transfer(
            auth_code="x",
            domain_name="x",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers", None, 1)


def test_transfers_create_transfer_throws_method_not_allowed_error() -> None:
    """Test CreateTransfer endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "transfers.create_transfer.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.transfers.create_transfer(
            auth_code="x",
            domain_name="x",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers", None, 1)


def test_transfers_create_transfer_throws_conflict_error() -> None:
    """Test CreateTransfer endpoint error response (ConflictError) with WireMock"""
    test_id = "transfers.create_transfer.6"
    client = get_client(test_id)
    with pytest.raises(ConflictError) as exc_info:
        client.transfers.create_transfer(
            auth_code="x",
            domain_name="x",
        )
    assert exc_info.value.status_code == 409
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers", None, 1)


def test_transfers_create_transfer_throws_unsupported_media_type_error() -> None:
    """Test CreateTransfer endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "transfers.create_transfer.7"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.transfers.create_transfer(
            auth_code="x",
            domain_name="x",
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/transfers", None, 1)


def test_transfers_create_transfer_throws_unprocessable_entity_error() -> None:
    """Test CreateTransfer endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "transfers.create_transfer.8"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.transfers.create_transfer(
            auth_code="x",
            domain_name="x",
        )
    assert exc_info.value.status_code == 422
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/transfers", None, 1)


def test_transfers_create_transfer_throws_too_many_requests_error() -> None:
    """Test CreateTransfer endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "transfers.create_transfer.9"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.transfers.create_transfer(
            auth_code="x",
            domain_name="x",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers", None, 1)


def test_transfers_create_transfer_throws_internal_server_error() -> None:
    """Test CreateTransfer endpoint error response (InternalServerError) with WireMock"""
    test_id = "transfers.create_transfer.10"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.transfers.create_transfer(
            auth_code="x",
            domain_name="x",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers", None, 1)


def test_transfers_create_transfer_throws_bad_gateway_error() -> None:
    """Test CreateTransfer endpoint error response (BadGatewayError) with WireMock"""
    test_id = "transfers.create_transfer.11"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.transfers.create_transfer(
            auth_code="x",
            domain_name="x",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers", None, 1)


def test_transfers_create_transfer_throws_service_unavailable_error() -> None:
    """Test CreateTransfer endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "transfers.create_transfer.12"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.transfers.create_transfer(
            auth_code="x",
            domain_name="x",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers", None, 1)


def test_transfers_create_transfer_throws_gateway_timeout_error() -> None:
    """Test CreateTransfer endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "transfers.create_transfer.13"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.transfers.create_transfer(
            auth_code="x",
            domain_name="x",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers", None, 1)


def test_transfers_get_transfer() -> None:
    """Test GetTransfer endpoint with WireMock"""
    test_id = "transfers.get_transfer.0"
    client = get_client(test_id)
    client.transfers.get_transfer(
        domain_name="domainName",
    )
    verify_request_count(test_id, "GET", "/core/v1/transfers/domainName", None, 1)


def test_transfers_get_transfer_throws_unauthorized_error() -> None:
    """Test GetTransfer endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "transfers.get_transfer.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.transfers.get_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/transfers/domainName", None, 1)


def test_transfers_get_transfer_throws_forbidden_error() -> None:
    """Test GetTransfer endpoint error response (ForbiddenError) with WireMock"""
    test_id = "transfers.get_transfer.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.transfers.get_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/transfers/domainName", None, 1)


def test_transfers_get_transfer_throws_not_found_error() -> None:
    """Test GetTransfer endpoint error response (NotFoundError) with WireMock"""
    test_id = "transfers.get_transfer.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.transfers.get_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "GET", "/core/v1/transfers/domainName", None, 1)


def test_transfers_get_transfer_throws_method_not_allowed_error() -> None:
    """Test GetTransfer endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "transfers.get_transfer.4"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.transfers.get_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/transfers/domainName", None, 1)


def test_transfers_get_transfer_throws_unprocessable_entity_error() -> None:
    """Test GetTransfer endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "transfers.get_transfer.5"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.transfers.get_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 422
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "GET", "/core/v1/transfers/domainName", None, 1)


def test_transfers_get_transfer_throws_too_many_requests_error() -> None:
    """Test GetTransfer endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "transfers.get_transfer.6"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.transfers.get_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/transfers/domainName", None, 1)


def test_transfers_get_transfer_throws_internal_server_error() -> None:
    """Test GetTransfer endpoint error response (InternalServerError) with WireMock"""
    test_id = "transfers.get_transfer.7"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.transfers.get_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/transfers/domainName", None, 1)


def test_transfers_get_transfer_throws_bad_gateway_error() -> None:
    """Test GetTransfer endpoint error response (BadGatewayError) with WireMock"""
    test_id = "transfers.get_transfer.8"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.transfers.get_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/transfers/domainName", None, 1)


def test_transfers_get_transfer_throws_service_unavailable_error() -> None:
    """Test GetTransfer endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "transfers.get_transfer.9"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.transfers.get_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/transfers/domainName", None, 1)


def test_transfers_get_transfer_throws_gateway_timeout_error() -> None:
    """Test GetTransfer endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "transfers.get_transfer.10"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.transfers.get_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/transfers/domainName", None, 1)


def test_transfers_cancel_transfer() -> None:
    """Test CancelTransfer endpoint with WireMock"""
    test_id = "transfers.cancel_transfer.0"
    client = get_client(test_id)
    client.transfers.cancel_transfer(
        domain_name="domainName",
    )
    verify_request_count(test_id, "POST", "/core/v1/transfers/domainName:cancel", None, 1)


def test_transfers_cancel_transfer_throws_bad_request_error() -> None:
    """Test CancelTransfer endpoint error response (BadRequestError) with WireMock"""
    test_id = "transfers.cancel_transfer.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.transfers.cancel_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/domainName:cancel", None, 1)


def test_transfers_cancel_transfer_throws_unauthorized_error() -> None:
    """Test CancelTransfer endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "transfers.cancel_transfer.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.transfers.cancel_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/domainName:cancel", None, 1)


def test_transfers_cancel_transfer_throws_forbidden_error() -> None:
    """Test CancelTransfer endpoint error response (ForbiddenError) with WireMock"""
    test_id = "transfers.cancel_transfer.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.transfers.cancel_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/domainName:cancel", None, 1)


def test_transfers_cancel_transfer_throws_not_found_error() -> None:
    """Test CancelTransfer endpoint error response (NotFoundError) with WireMock"""
    test_id = "transfers.cancel_transfer.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.transfers.cancel_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/domainName:cancel", None, 1)


def test_transfers_cancel_transfer_throws_method_not_allowed_error() -> None:
    """Test CancelTransfer endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "transfers.cancel_transfer.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.transfers.cancel_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/domainName:cancel", None, 1)


def test_transfers_cancel_transfer_throws_conflict_error() -> None:
    """Test CancelTransfer endpoint error response (ConflictError) with WireMock"""
    test_id = "transfers.cancel_transfer.6"
    client = get_client(test_id)
    with pytest.raises(ConflictError) as exc_info:
        client.transfers.cancel_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 409
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/domainName:cancel", None, 1)


def test_transfers_cancel_transfer_throws_unsupported_media_type_error() -> None:
    """Test CancelTransfer endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "transfers.cancel_transfer.7"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.transfers.cancel_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/domainName:cancel", None, 1)


def test_transfers_cancel_transfer_throws_too_many_requests_error() -> None:
    """Test CancelTransfer endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "transfers.cancel_transfer.8"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.transfers.cancel_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/domainName:cancel", None, 1)


def test_transfers_cancel_transfer_throws_internal_server_error() -> None:
    """Test CancelTransfer endpoint error response (InternalServerError) with WireMock"""
    test_id = "transfers.cancel_transfer.9"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.transfers.cancel_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/domainName:cancel", None, 1)


def test_transfers_cancel_transfer_throws_bad_gateway_error() -> None:
    """Test CancelTransfer endpoint error response (BadGatewayError) with WireMock"""
    test_id = "transfers.cancel_transfer.10"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.transfers.cancel_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/domainName:cancel", None, 1)


def test_transfers_cancel_transfer_throws_service_unavailable_error() -> None:
    """Test CancelTransfer endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "transfers.cancel_transfer.11"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.transfers.cancel_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/domainName:cancel", None, 1)


def test_transfers_cancel_transfer_throws_gateway_timeout_error() -> None:
    """Test CancelTransfer endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "transfers.cancel_transfer.12"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.transfers.cancel_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/domainName:cancel", None, 1)


def test_transfers_cancel_outbound_transfer() -> None:
    """Test CancelOutboundTransfer endpoint with WireMock"""
    test_id = "transfers.cancel_outbound_transfer.0"
    client = get_client(test_id)
    client.transfers.cancel_outbound_transfer(
        domain_name="example.com",
    )
    verify_request_count(test_id, "POST", "/core/v1/transfers/external/out/example.com:cancel", None, 1)


def test_transfers_cancel_outbound_transfer_throws_unauthorized_error() -> None:
    """Test CancelOutboundTransfer endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "transfers.cancel_outbound_transfer.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.transfers.cancel_outbound_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/external/out/domainName:cancel", None, 1)


def test_transfers_cancel_outbound_transfer_throws_forbidden_error() -> None:
    """Test CancelOutboundTransfer endpoint error response (ForbiddenError) with WireMock"""
    test_id = "transfers.cancel_outbound_transfer.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.transfers.cancel_outbound_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/external/out/domainName:cancel", None, 1)


def test_transfers_cancel_outbound_transfer_throws_not_found_error() -> None:
    """Test CancelOutboundTransfer endpoint error response (NotFoundError) with WireMock"""
    test_id = "transfers.cancel_outbound_transfer.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.transfers.cancel_outbound_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/external/out/domainName:cancel", None, 1)


def test_transfers_cancel_outbound_transfer_throws_method_not_allowed_error() -> None:
    """Test CancelOutboundTransfer endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "transfers.cancel_outbound_transfer.4"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.transfers.cancel_outbound_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/external/out/domainName:cancel", None, 1)


def test_transfers_cancel_outbound_transfer_throws_conflict_error() -> None:
    """Test CancelOutboundTransfer endpoint error response (ConflictError) with WireMock"""
    test_id = "transfers.cancel_outbound_transfer.5"
    client = get_client(test_id)
    with pytest.raises(ConflictError) as exc_info:
        client.transfers.cancel_outbound_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 409
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/external/out/domainName:cancel", None, 1)


def test_transfers_cancel_outbound_transfer_throws_unsupported_media_type_error() -> None:
    """Test CancelOutboundTransfer endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "transfers.cancel_outbound_transfer.6"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.transfers.cancel_outbound_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/external/out/domainName:cancel", None, 1)


def test_transfers_cancel_outbound_transfer_throws_unprocessable_entity_error() -> None:
    """Test CancelOutboundTransfer endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "transfers.cancel_outbound_transfer.7"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.transfers.cancel_outbound_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 422
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/external/out/domainName:cancel", None, 1)


def test_transfers_cancel_outbound_transfer_throws_too_many_requests_error() -> None:
    """Test CancelOutboundTransfer endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "transfers.cancel_outbound_transfer.8"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.transfers.cancel_outbound_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/external/out/domainName:cancel", None, 1)


def test_transfers_cancel_outbound_transfer_throws_internal_server_error() -> None:
    """Test CancelOutboundTransfer endpoint error response (InternalServerError) with WireMock"""
    test_id = "transfers.cancel_outbound_transfer.9"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.transfers.cancel_outbound_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/external/out/domainName:cancel", None, 1)


def test_transfers_cancel_outbound_transfer_throws_bad_gateway_error() -> None:
    """Test CancelOutboundTransfer endpoint error response (BadGatewayError) with WireMock"""
    test_id = "transfers.cancel_outbound_transfer.10"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.transfers.cancel_outbound_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/external/out/domainName:cancel", None, 1)


def test_transfers_cancel_outbound_transfer_throws_service_unavailable_error() -> None:
    """Test CancelOutboundTransfer endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "transfers.cancel_outbound_transfer.11"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.transfers.cancel_outbound_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/external/out/domainName:cancel", None, 1)


def test_transfers_cancel_outbound_transfer_throws_gateway_timeout_error() -> None:
    """Test CancelOutboundTransfer endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "transfers.cancel_outbound_transfer.12"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.transfers.cancel_outbound_transfer(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/external/out/domainName:cancel", None, 1)


def test_transfers_create_internal_transfer_in() -> None:
    """Test CreateInternalTransferIn endpoint with WireMock"""
    test_id = "transfers.create_internal_transfer_in.0"
    client = get_client(test_id)
    client.transfers.create_internal_transfer_in(
        domain_name="example.com",
        auth_code="ABC123",
    )
    verify_request_count(test_id, "POST", "/core/v1/transfers/internal/in", None, 1)


def test_transfers_create_internal_transfer_in_throws_bad_request_error() -> None:
    """Test CreateInternalTransferIn endpoint error response (BadRequestError) with WireMock"""
    test_id = "transfers.create_internal_transfer_in.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.transfers.create_internal_transfer_in(
            domain_name="x",
            auth_code="x",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/internal/in", None, 1)


def test_transfers_create_internal_transfer_in_throws_unauthorized_error() -> None:
    """Test CreateInternalTransferIn endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "transfers.create_internal_transfer_in.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.transfers.create_internal_transfer_in(
            domain_name="x",
            auth_code="x",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/internal/in", None, 1)


def test_transfers_create_internal_transfer_in_throws_forbidden_error() -> None:
    """Test CreateInternalTransferIn endpoint error response (ForbiddenError) with WireMock"""
    test_id = "transfers.create_internal_transfer_in.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.transfers.create_internal_transfer_in(
            domain_name="x",
            auth_code="x",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/internal/in", None, 1)


def test_transfers_create_internal_transfer_in_throws_not_found_error() -> None:
    """Test CreateInternalTransferIn endpoint error response (NotFoundError) with WireMock"""
    test_id = "transfers.create_internal_transfer_in.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.transfers.create_internal_transfer_in(
            domain_name="x",
            auth_code="x",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/internal/in", None, 1)


def test_transfers_create_internal_transfer_in_throws_method_not_allowed_error() -> None:
    """Test CreateInternalTransferIn endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "transfers.create_internal_transfer_in.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.transfers.create_internal_transfer_in(
            domain_name="x",
            auth_code="x",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/internal/in", None, 1)


def test_transfers_create_internal_transfer_in_throws_conflict_error() -> None:
    """Test CreateInternalTransferIn endpoint error response (ConflictError) with WireMock"""
    test_id = "transfers.create_internal_transfer_in.6"
    client = get_client(test_id)
    with pytest.raises(ConflictError) as exc_info:
        client.transfers.create_internal_transfer_in(
            domain_name="x",
            auth_code="x",
        )
    assert exc_info.value.status_code == 409
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/internal/in", None, 1)


def test_transfers_create_internal_transfer_in_throws_unsupported_media_type_error() -> None:
    """Test CreateInternalTransferIn endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "transfers.create_internal_transfer_in.7"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.transfers.create_internal_transfer_in(
            domain_name="x",
            auth_code="x",
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/internal/in", None, 1)


def test_transfers_create_internal_transfer_in_throws_too_many_requests_error() -> None:
    """Test CreateInternalTransferIn endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "transfers.create_internal_transfer_in.8"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.transfers.create_internal_transfer_in(
            domain_name="x",
            auth_code="x",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/internal/in", None, 1)


def test_transfers_create_internal_transfer_in_throws_internal_server_error() -> None:
    """Test CreateInternalTransferIn endpoint error response (InternalServerError) with WireMock"""
    test_id = "transfers.create_internal_transfer_in.9"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.transfers.create_internal_transfer_in(
            domain_name="x",
            auth_code="x",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/internal/in", None, 1)


def test_transfers_create_internal_transfer_in_throws_bad_gateway_error() -> None:
    """Test CreateInternalTransferIn endpoint error response (BadGatewayError) with WireMock"""
    test_id = "transfers.create_internal_transfer_in.10"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.transfers.create_internal_transfer_in(
            domain_name="x",
            auth_code="x",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/internal/in", None, 1)


def test_transfers_create_internal_transfer_in_throws_service_unavailable_error() -> None:
    """Test CreateInternalTransferIn endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "transfers.create_internal_transfer_in.11"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.transfers.create_internal_transfer_in(
            domain_name="x",
            auth_code="x",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/internal/in", None, 1)


def test_transfers_create_internal_transfer_in_throws_gateway_timeout_error() -> None:
    """Test CreateInternalTransferIn endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "transfers.create_internal_transfer_in.12"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.transfers.create_internal_transfer_in(
            domain_name="x",
            auth_code="x",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/transfers/internal/in", None, 1)


def test_transfers_get_transfer_eligibility() -> None:
    """Test GetTransferEligibility endpoint with WireMock"""
    test_id = "transfers.get_transfer_eligibility.0"
    client = get_client(test_id)
    client.transfers.get_transfer_eligibility(
        domain_name="domainName",
    )
    verify_request_count(test_id, "GET", "/core/v1/transfers/eligibility/domainName", None, 1)


def test_transfers_get_transfer_eligibility_domain_is_at_an_external_registrar() -> None:
    """Test GetTransferEligibility endpoint (Domain is at an external registrar example) with WireMock"""
    test_id = "transfers.get_transfer_eligibility.1"
    client = get_client(test_id)
    client.transfers.get_transfer_eligibility(
        domain_name="domainName",
    )
    verify_request_count(test_id, "GET", "/core/v1/transfers/eligibility/domainName", None, 1)


def test_transfers_get_transfer_eligibility_throws_bad_request_error() -> None:
    """Test GetTransferEligibility endpoint error response (BadRequestError) with WireMock"""
    test_id = "transfers.get_transfer_eligibility.2"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.transfers.get_transfer_eligibility(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/transfers/eligibility/domainName", None, 1)


def test_transfers_get_transfer_eligibility_throws_unauthorized_error() -> None:
    """Test GetTransferEligibility endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "transfers.get_transfer_eligibility.3"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.transfers.get_transfer_eligibility(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/transfers/eligibility/domainName", None, 1)


def test_transfers_get_transfer_eligibility_throws_forbidden_error() -> None:
    """Test GetTransferEligibility endpoint error response (ForbiddenError) with WireMock"""
    test_id = "transfers.get_transfer_eligibility.4"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.transfers.get_transfer_eligibility(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/transfers/eligibility/domainName", None, 1)


def test_transfers_get_transfer_eligibility_throws_method_not_allowed_error() -> None:
    """Test GetTransferEligibility endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "transfers.get_transfer_eligibility.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.transfers.get_transfer_eligibility(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/transfers/eligibility/domainName", None, 1)


def test_transfers_get_transfer_eligibility_throws_unprocessable_entity_error() -> None:
    """Test GetTransferEligibility endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "transfers.get_transfer_eligibility.6"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.transfers.get_transfer_eligibility(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 422
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "GET", "/core/v1/transfers/eligibility/domainName", None, 1)


def test_transfers_get_transfer_eligibility_throws_too_many_requests_error() -> None:
    """Test GetTransferEligibility endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "transfers.get_transfer_eligibility.7"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.transfers.get_transfer_eligibility(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/transfers/eligibility/domainName", None, 1)


def test_transfers_get_transfer_eligibility_throws_internal_server_error() -> None:
    """Test GetTransferEligibility endpoint error response (InternalServerError) with WireMock"""
    test_id = "transfers.get_transfer_eligibility.8"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.transfers.get_transfer_eligibility(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/transfers/eligibility/domainName", None, 1)


def test_transfers_get_transfer_eligibility_throws_bad_gateway_error() -> None:
    """Test GetTransferEligibility endpoint error response (BadGatewayError) with WireMock"""
    test_id = "transfers.get_transfer_eligibility.9"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.transfers.get_transfer_eligibility(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/transfers/eligibility/domainName", None, 1)


def test_transfers_get_transfer_eligibility_throws_service_unavailable_error() -> None:
    """Test GetTransferEligibility endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "transfers.get_transfer_eligibility.10"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.transfers.get_transfer_eligibility(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/transfers/eligibility/domainName", None, 1)


def test_transfers_get_transfer_eligibility_throws_gateway_timeout_error() -> None:
    """Test GetTransferEligibility endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "transfers.get_transfer_eligibility.11"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.transfers.get_transfer_eligibility(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/transfers/eligibility/domainName", None, 1)

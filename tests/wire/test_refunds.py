import pytest
from .conftest import get_client, verify_request_count

from namecom_core_api import (
    BadGatewayError,
    BadRequestError,
    ConflictError,
    ForbiddenError,
    GatewayTimeoutError,
    InternalServerError,
    LockedError,
    MethodNotAllowedError,
    NotFoundError,
    ServiceUnavailableError,
    TooManyRequestsError,
    UnauthorizedError,
    UnsupportedMediaTypeError,
)
from namecom_core_api.core.jsonable_encoder import jsonable_encoder


def test_refunds_process_refund() -> None:
    """Test ProcessRefund endpoint with WireMock"""
    test_id = "refunds.process_refund.0"
    client = get_client(test_id)
    client.refunds.process_refund(
        order_id=123456,
        order_item_ids=[987654],
    )
    verify_request_count(test_id, "POST", "/core/v1/refund", None, 1)


def test_refunds_process_refund_refund_multiple_order_items() -> None:
    """Test ProcessRefund endpoint (Refund multiple order items example) with WireMock"""
    test_id = "refunds.process_refund.1"
    client = get_client(test_id)
    client.refunds.process_refund(
        order_id=123456,
        order_item_ids=[987654, 987655],
    )
    verify_request_count(test_id, "POST", "/core/v1/refund", None, 1)


def test_refunds_process_refund_throws_bad_request_error() -> None:
    """Test ProcessRefund endpoint error response (BadRequestError) with WireMock"""
    test_id = "refunds.process_refund.2"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.refunds.process_refund(
            order_id=1,
            order_item_ids=[1, 1],
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/refund", None, 1)


def test_refunds_process_refund_throws_unauthorized_error() -> None:
    """Test ProcessRefund endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "refunds.process_refund.3"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.refunds.process_refund(
            order_id=1,
            order_item_ids=[1, 1],
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/refund", None, 1)


def test_refunds_process_refund_throws_forbidden_error() -> None:
    """Test ProcessRefund endpoint error response (ForbiddenError) with WireMock"""
    test_id = "refunds.process_refund.4"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.refunds.process_refund(
            order_id=1,
            order_item_ids=[1, 1],
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/refund", None, 1)


def test_refunds_process_refund_throws_not_found_error() -> None:
    """Test ProcessRefund endpoint error response (NotFoundError) with WireMock"""
    test_id = "refunds.process_refund.5"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.refunds.process_refund(
            order_id=1,
            order_item_ids=[1, 1],
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/refund", None, 1)


def test_refunds_process_refund_throws_method_not_allowed_error() -> None:
    """Test ProcessRefund endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "refunds.process_refund.6"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.refunds.process_refund(
            order_id=1,
            order_item_ids=[1, 1],
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/refund", None, 1)


def test_refunds_process_refund_throws_conflict_error() -> None:
    """Test ProcessRefund endpoint error response (ConflictError) with WireMock"""
    test_id = "refunds.process_refund.7"
    client = get_client(test_id)
    with pytest.raises(ConflictError) as exc_info:
        client.refunds.process_refund(
            order_id=1,
            order_item_ids=[1, 1],
        )
    assert exc_info.value.status_code == 409
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/refund", None, 1)


def test_refunds_process_refund_throws_unsupported_media_type_error() -> None:
    """Test ProcessRefund endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "refunds.process_refund.8"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.refunds.process_refund(
            order_id=1,
            order_item_ids=[1, 1],
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/refund", None, 1)


def test_refunds_process_refund_throws_locked_error() -> None:
    """Test ProcessRefund endpoint error response (LockedError) with WireMock"""
    test_id = "refunds.process_refund.9"
    client = get_client(test_id)
    with pytest.raises(LockedError) as exc_info:
        client.refunds.process_refund(
            order_id=1,
            order_item_ids=[1, 1],
        )
    assert exc_info.value.status_code == 423
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/refund", None, 1)


def test_refunds_process_refund_throws_too_many_requests_error() -> None:
    """Test ProcessRefund endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "refunds.process_refund.10"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.refunds.process_refund(
            order_id=1,
            order_item_ids=[1, 1],
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/refund", None, 1)


def test_refunds_process_refund_throws_internal_server_error() -> None:
    """Test ProcessRefund endpoint error response (InternalServerError) with WireMock"""
    test_id = "refunds.process_refund.11"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.refunds.process_refund(
            order_id=1,
            order_item_ids=[1, 1],
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/refund", None, 1)


def test_refunds_process_refund_throws_bad_gateway_error() -> None:
    """Test ProcessRefund endpoint error response (BadGatewayError) with WireMock"""
    test_id = "refunds.process_refund.12"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.refunds.process_refund(
            order_id=1,
            order_item_ids=[1, 1],
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/refund", None, 1)


def test_refunds_process_refund_throws_service_unavailable_error() -> None:
    """Test ProcessRefund endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "refunds.process_refund.13"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.refunds.process_refund(
            order_id=1,
            order_item_ids=[1, 1],
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/refund", None, 1)


def test_refunds_process_refund_throws_gateway_timeout_error() -> None:
    """Test ProcessRefund endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "refunds.process_refund.14"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.refunds.process_refund(
            order_id=1,
            order_item_ids=[1, 1],
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/refund", None, 1)

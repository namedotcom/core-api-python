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
)
from namecom_core_api.core.jsonable_encoder import jsonable_encoder


def test_orders_list_orders() -> None:
    """Test ListOrders endpoint with WireMock"""
    test_id = "orders.list_orders.0"
    client = get_client(test_id)
    client.orders.list_orders()
    verify_request_count(test_id, "GET", "/core/v1/orders", None, 1)


def test_orders_list_orders_throws_bad_request_error() -> None:
    """Test ListOrders endpoint error response (BadRequestError) with WireMock"""
    test_id = "orders.list_orders.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.orders.list_orders()
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/orders", None, 1)


def test_orders_list_orders_throws_unauthorized_error() -> None:
    """Test ListOrders endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "orders.list_orders.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.orders.list_orders()
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/orders", None, 1)


def test_orders_list_orders_throws_forbidden_error() -> None:
    """Test ListOrders endpoint error response (ForbiddenError) with WireMock"""
    test_id = "orders.list_orders.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.orders.list_orders()
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/orders", None, 1)


def test_orders_list_orders_throws_method_not_allowed_error() -> None:
    """Test ListOrders endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "orders.list_orders.4"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.orders.list_orders()
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/orders", None, 1)


def test_orders_list_orders_throws_too_many_requests_error() -> None:
    """Test ListOrders endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "orders.list_orders.5"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.orders.list_orders()
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/orders", None, 1)


def test_orders_list_orders_throws_internal_server_error() -> None:
    """Test ListOrders endpoint error response (InternalServerError) with WireMock"""
    test_id = "orders.list_orders.6"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.orders.list_orders()
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/orders", None, 1)


def test_orders_list_orders_throws_bad_gateway_error() -> None:
    """Test ListOrders endpoint error response (BadGatewayError) with WireMock"""
    test_id = "orders.list_orders.7"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.orders.list_orders()
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/orders", None, 1)


def test_orders_list_orders_throws_service_unavailable_error() -> None:
    """Test ListOrders endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "orders.list_orders.8"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.orders.list_orders()
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/orders", None, 1)


def test_orders_list_orders_throws_gateway_timeout_error() -> None:
    """Test ListOrders endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "orders.list_orders.9"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.orders.list_orders()
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/orders", None, 1)


def test_orders_get_order() -> None:
    """Test GetOrder endpoint with WireMock"""
    test_id = "orders.get_order.0"
    client = get_client(test_id)
    client.orders.get_order(
        order_id=1,
    )
    verify_request_count(test_id, "GET", "/core/v1/orders/1", None, 1)


def test_orders_get_order_throws_unauthorized_error() -> None:
    """Test GetOrder endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "orders.get_order.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.orders.get_order(
            order_id=1,
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/orders/1", None, 1)


def test_orders_get_order_throws_forbidden_error() -> None:
    """Test GetOrder endpoint error response (ForbiddenError) with WireMock"""
    test_id = "orders.get_order.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.orders.get_order(
            order_id=1,
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/orders/1", None, 1)


def test_orders_get_order_throws_not_found_error() -> None:
    """Test GetOrder endpoint error response (NotFoundError) with WireMock"""
    test_id = "orders.get_order.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.orders.get_order(
            order_id=1,
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "GET", "/core/v1/orders/1", None, 1)


def test_orders_get_order_throws_method_not_allowed_error() -> None:
    """Test GetOrder endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "orders.get_order.4"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.orders.get_order(
            order_id=1,
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/orders/1", None, 1)


def test_orders_get_order_throws_too_many_requests_error() -> None:
    """Test GetOrder endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "orders.get_order.5"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.orders.get_order(
            order_id=1,
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/orders/1", None, 1)


def test_orders_get_order_throws_internal_server_error() -> None:
    """Test GetOrder endpoint error response (InternalServerError) with WireMock"""
    test_id = "orders.get_order.6"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.orders.get_order(
            order_id=1,
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/orders/1", None, 1)


def test_orders_get_order_throws_bad_gateway_error() -> None:
    """Test GetOrder endpoint error response (BadGatewayError) with WireMock"""
    test_id = "orders.get_order.7"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.orders.get_order(
            order_id=1,
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/orders/1", None, 1)


def test_orders_get_order_throws_service_unavailable_error() -> None:
    """Test GetOrder endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "orders.get_order.8"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.orders.get_order(
            order_id=1,
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/orders/1", None, 1)


def test_orders_get_order_throws_gateway_timeout_error() -> None:
    """Test GetOrder endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "orders.get_order.9"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.orders.get_order(
            order_id=1,
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/orders/1", None, 1)

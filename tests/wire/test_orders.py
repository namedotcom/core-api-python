from .conftest import get_client, verify_request_count


def test_orders_list_orders() -> None:
    """Test ListOrders endpoint with WireMock"""
    test_id = "orders.list_orders.0"
    client = get_client(test_id)
    client.orders.list_orders()
    verify_request_count(test_id, "GET", "/core/v1/orders", None, 1)


def test_orders_get_order() -> None:
    """Test GetOrder endpoint with WireMock"""
    test_id = "orders.get_order.0"
    client = get_client(test_id)
    client.orders.get_order(
        order_id=1,
    )
    verify_request_count(test_id, "GET", "/core/v1/orders/1", None, 1)

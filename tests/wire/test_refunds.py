from .conftest import get_client, verify_request_count


def test_refunds_process_refund() -> None:
    """Test ProcessRefund endpoint with WireMock"""
    test_id = "refunds.process_refund.0"
    client = get_client(test_id)
    client.refunds.process_refund(
        order_id=123456,
        order_item_ids=[987654],
    )
    verify_request_count(test_id, "POST", "/core/v1/refund", None, 1)

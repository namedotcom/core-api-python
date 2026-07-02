from .conftest import get_client, verify_request_count


def test_accountInfo_check_account_balance() -> None:
    """Test CheckAccountBalance endpoint with WireMock"""
    test_id = "account_info.check_account_balance.0"
    client = get_client(test_id)
    client.account_info.check_account_balance()
    verify_request_count(test_id, "GET", "/core/v1/accountinfo/balance", None, 1)

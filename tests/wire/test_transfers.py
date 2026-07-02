from .conftest import get_client, verify_request_count


def test_transfers_list_transfers() -> None:
    """Test ListTransfers endpoint with WireMock"""
    test_id = "transfers.list_transfers.0"
    client = get_client(test_id)
    client.transfers.list_transfers()
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


def test_transfers_get_transfer() -> None:
    """Test GetTransfer endpoint with WireMock"""
    test_id = "transfers.get_transfer.0"
    client = get_client(test_id)
    client.transfers.get_transfer(
        domain_name="domainName",
    )
    verify_request_count(test_id, "GET", "/core/v1/transfers/domainName", None, 1)


def test_transfers_cancel_transfer() -> None:
    """Test CancelTransfer endpoint with WireMock"""
    test_id = "transfers.cancel_transfer.0"
    client = get_client(test_id)
    client.transfers.cancel_transfer(
        domain_name="domainName",
    )
    verify_request_count(test_id, "POST", "/core/v1/transfers/domainName:cancel", None, 1)


def test_transfers_cancel_outbound_transfer() -> None:
    """Test CancelOutboundTransfer endpoint with WireMock"""
    test_id = "transfers.cancel_outbound_transfer.0"
    client = get_client(test_id)
    client.transfers.cancel_outbound_transfer(
        domain_name="example.com",
    )
    verify_request_count(test_id, "POST", "/core/v1/transfers/external/out/example.com:cancel", None, 1)


def test_transfers_create_internal_transfer_in() -> None:
    """Test CreateInternalTransferIn endpoint with WireMock"""
    test_id = "transfers.create_internal_transfer_in.0"
    client = get_client(test_id)
    client.transfers.create_internal_transfer_in(
        domain_name="example.com",
        auth_code="ABC123",
    )
    verify_request_count(test_id, "POST", "/core/v1/transfers/internal/in", None, 1)


def test_transfers_get_transfer_eligibility() -> None:
    """Test GetTransferEligibility endpoint with WireMock"""
    test_id = "transfers.get_transfer_eligibility.0"
    client = get_client(test_id)
    client.transfers.get_transfer_eligibility(
        domain_name="domainName",
    )
    verify_request_count(test_id, "GET", "/core/v1/transfers/eligibility/domainName", None, 1)

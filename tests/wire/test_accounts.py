from .conftest import get_client, verify_request_count

from namecom_core_api import AccountRequest, ContactsRequest, RegistrantContactRequest


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

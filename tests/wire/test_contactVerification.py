from .conftest import get_client, verify_request_count


def test_contactVerification_unverified_contacts_list() -> None:
    """Test UnverifiedContactsList endpoint with WireMock"""
    test_id = "contact_verification.unverified_contacts_list.0"
    client = get_client(test_id)
    client.contact_verification.unverified_contacts_list(
        per_page=100,
        page=2,
    )
    verify_request_count(test_id, "GET", "/core/v1/contacts/unverified", {"perPage": "100", "page": "2"}, 1)


def test_contactVerification_verify_contact() -> None:
    """Test VerifyContact endpoint with WireMock"""
    test_id = "contact_verification.verify_contact.0"
    client = get_client(test_id)
    client.contact_verification.verify_contact(
        verification_id=1,
    )
    verify_request_count(test_id, "POST", "/core/v1/contacts/verify/1", None, 1)


def test_contactVerification_resend_contact_verification_email() -> None:
    """Test ResendContactVerificationEmail endpoint with WireMock"""
    test_id = "contact_verification.resend_contact_verification_email.0"
    client = get_client(test_id)
    client.contact_verification.resend_contact_verification_email(
        verification_id=1,
    )
    verify_request_count(test_id, "POST", "/core/v1/contacts/verify/1:resend", None, 1)

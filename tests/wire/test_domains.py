import datetime

import pytest
from .conftest import get_client, verify_request_count

from namecom_core_api import (
    BadGatewayError,
    BadRequestError,
    ConflictError,
    ContactRequest,
    ContactsRequest,
    DomainClaimsInfo,
    DomainCreatePayload,
    ForbiddenError,
    GatewayTimeoutError,
    InternalServerError,
    MethodNotAllowedError,
    NotAcceptableError,
    NotFoundError,
    NotImplementedError,
    PaymentRequiredError,
    ServiceUnavailableError,
    TooManyRequestsError,
    UnauthorizedError,
    UnavailableForLegalReasonsError,
    UnprocessableEntityError,
    UnsupportedMediaTypeError,
)
from namecom_core_api.core.jsonable_encoder import jsonable_encoder


def test_domains_list_domains() -> None:
    """Test ListDomains endpoint with WireMock"""
    test_id = "domains.list_domains.0"
    client = get_client(test_id)
    client.domains.list_domains()
    verify_request_count(test_id, "GET", "/core/v1/domains", None, 1)


def test_domains_list_domains_throws_bad_request_error() -> None:
    """Test ListDomains endpoint error response (BadRequestError) with WireMock"""
    test_id = "domains.list_domains.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.domains.list_domains()
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains", None, 1)


def test_domains_list_domains_throws_unauthorized_error() -> None:
    """Test ListDomains endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "domains.list_domains.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.domains.list_domains()
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains", None, 1)


def test_domains_list_domains_throws_forbidden_error() -> None:
    """Test ListDomains endpoint error response (ForbiddenError) with WireMock"""
    test_id = "domains.list_domains.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.domains.list_domains()
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains", None, 1)


def test_domains_list_domains_throws_method_not_allowed_error() -> None:
    """Test ListDomains endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "domains.list_domains.4"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.domains.list_domains()
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains", None, 1)


def test_domains_list_domains_throws_too_many_requests_error() -> None:
    """Test ListDomains endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "domains.list_domains.5"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.domains.list_domains()
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains", None, 1)


def test_domains_list_domains_throws_internal_server_error() -> None:
    """Test ListDomains endpoint error response (InternalServerError) with WireMock"""
    test_id = "domains.list_domains.6"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.domains.list_domains()
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains", None, 1)


def test_domains_list_domains_throws_bad_gateway_error() -> None:
    """Test ListDomains endpoint error response (BadGatewayError) with WireMock"""
    test_id = "domains.list_domains.7"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.domains.list_domains()
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains", None, 1)


def test_domains_list_domains_throws_service_unavailable_error() -> None:
    """Test ListDomains endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "domains.list_domains.8"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.domains.list_domains()
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains", None, 1)


def test_domains_list_domains_throws_gateway_timeout_error() -> None:
    """Test ListDomains endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "domains.list_domains.9"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.domains.list_domains()
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains", None, 1)


def test_domains_create_domain() -> None:
    """Test CreateDomain endpoint with WireMock"""
    test_id = "domains.create_domain.0"
    client = get_client(test_id)
    client.domains.create_domain(
        domain=DomainCreatePayload(
            domain_name="example.com",
        ),
    )
    verify_request_count(test_id, "POST", "/core/v1/domains", None, 1)


def test_domains_create_domain_standard_registration_2_years_omit_purchase_price() -> None:
    """Test CreateDomain endpoint (Standard registration, 2 years (omit purchasePrice). example) with WireMock"""
    test_id = "domains.create_domain.1"
    client = get_client(test_id)
    client.domains.create_domain(
        domain=DomainCreatePayload(
            domain_name="example.com",
        ),
        years=2,
    )
    verify_request_count(test_id, "POST", "/core/v1/domains", None, 1)


def test_domains_create_domain_standard_registration_with_a_promo_code() -> None:
    """Test CreateDomain endpoint (Standard registration with a promo code. example) with WireMock"""
    test_id = "domains.create_domain.2"
    client = get_client(test_id)
    client.domains.create_domain(
        domain=DomainCreatePayload(
            domain_name="example.com",
        ),
        years=1,
        promo_code="SPRING26",
    )
    verify_request_count(test_id, "POST", "/core/v1/domains", None, 1)


def test_domains_create_domain_registry_premium_domain_1_year() -> None:
    """Test CreateDomain endpoint (Registry premium domain, 1 year. example) with WireMock"""
    test_id = "domains.create_domain.3"
    client = get_client(test_id)
    client.domains.create_domain(
        domain=DomainCreatePayload(
            domain_name="premiumexample.com",
        ),
        purchase_price=349.95,
        purchase_type="registration",
        years=1,
    )
    verify_request_count(test_id, "POST", "/core/v1/domains", None, 1)


def test_domains_create_domain_registry_premium_domain_2_years_from_get_pricing() -> None:
    """Test CreateDomain endpoint (Registry premium domain, 2 years (from Get Pricing). example) with WireMock"""
    test_id = "domains.create_domain.4"
    client = get_client(test_id)
    client.domains.create_domain(
        domain=DomainCreatePayload(
            domain_name="premiumexample.com",
        ),
        purchase_price=699.9,
        purchase_type="registration",
        years=2,
    )
    verify_request_count(test_id, "POST", "/core/v1/domains", None, 1)


def test_domains_create_domain_aftermarket_domain_flat_acquisition_fee() -> None:
    """Test CreateDomain endpoint (Aftermarket domain — flat acquisition fee. example) with WireMock"""
    test_id = "domains.create_domain.5"
    client = get_client(test_id)
    client.domains.create_domain(
        domain=DomainCreatePayload(
            domain_name="rarename.com",
        ),
        purchase_price=5000,
        purchase_type="aftermarket_s",
        years=1,
    )
    verify_request_count(test_id, "POST", "/core/v1/domains", None, 1)


def test_domains_create_domain_expiring_domain_non_registration_purchase_type() -> None:
    """Test CreateDomain endpoint (Expiring domain (non-registration purchaseType). example) with WireMock"""
    test_id = "domains.create_domain.6"
    client = get_client(test_id)
    client.domains.create_domain(
        domain=DomainCreatePayload(
            domain_name="expiringexample.com",
        ),
        purchase_price=349.95,
        purchase_type="expiring",
        years=1,
    )
    verify_request_count(test_id, "POST", "/core/v1/domains", None, 1)


def test_domains_create_domain_backorder_domain_non_registration_purchase_type() -> None:
    """Test CreateDomain endpoint (Backorder domain (non-registration purchaseType). example) with WireMock"""
    test_id = "domains.create_domain.7"
    client = get_client(test_id)
    client.domains.create_domain(
        domain=DomainCreatePayload(
            domain_name="backorderexample.com",
        ),
        purchase_price=79.99,
        purchase_type="backorder",
    )
    verify_request_count(test_id, "POST", "/core/v1/domains", None, 1)


def test_domains_create_domain_send_single_specific_contact_with_domain_create() -> None:
    """Test CreateDomain endpoint (Send single, specific contact with domain create example) with WireMock"""
    test_id = "domains.create_domain.8"
    client = get_client(test_id)
    client.domains.create_domain(
        domain=DomainCreatePayload(
            contacts=ContactsRequest(
                tech=ContactRequest(
                    first_name="Jonny",
                    last_name="IT Guy",
                    company_name="My Company",
                    address1="1234 Any Street",
                    city="Anytown",
                    state="NY",
                    zip="11222",
                    country="US",
                    email="support@example.com",
                    phone="+15555555",
                ),
            ),
            domain_name="example.com",
        ),
    )
    verify_request_count(test_id, "POST", "/core/v1/domains", None, 1)


def test_domains_create_domain_registering_an_idn_domain() -> None:
    """Test CreateDomain endpoint (Registering an IDN domain example) with WireMock"""
    test_id = "domains.create_domain.9"
    client = get_client(test_id)
    client.domains.create_domain(
        domain=DomainCreatePayload(
            domain_name="exámple.com",
        ),
        tld_requirements={"language": "ES"},
        years=1,
    )
    verify_request_count(test_id, "POST", "/core/v1/domains", None, 1)


def test_domains_create_domain_registering_a_se_domain_with_tld_requirements() -> None:
    """Test CreateDomain endpoint (Registering a .se domain with TLD requirements example) with WireMock"""
    test_id = "domains.create_domain.10"
    client = get_client(test_id)
    client.domains.create_domain(
        domain=DomainCreatePayload(
            domain_name="example.se",
        ),
        tld_requirements={"X-NICSE-IDNUMBER": "5566778899"},
        years=1,
    )
    verify_request_count(test_id, "POST", "/core/v1/domains", None, 1)


def test_domains_create_domain_creating_a_domain_with_trademark_claims_acknowledgment() -> None:
    """Test CreateDomain endpoint (Creating a domain with trademark claims acknowledgment example) with WireMock"""
    test_id = "domains.create_domain.11"
    client = get_client(test_id)
    client.domains.create_domain(
        domain=DomainCreatePayload(
            domain_name="tiktok.page",
        ),
        claims=DomainClaimsInfo(
            claim_id="8c3027d30000000000382500785",
            not_before=datetime.datetime.fromisoformat("2020-01-01T00:00:00+00:00"),
            not_after=datetime.datetime.fromisoformat("2030-01-01T00:00:00+00:00"),
        ),
    )
    verify_request_count(test_id, "POST", "/core/v1/domains", None, 1)


def test_domains_create_domain_throws_bad_request_error() -> None:
    """Test CreateDomain endpoint error response (BadRequestError) with WireMock"""
    test_id = "domains.create_domain.12"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.domains.create_domain(
            domain=DomainCreatePayload(),
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains", None, 1)


def test_domains_create_domain_throws_unauthorized_error() -> None:
    """Test CreateDomain endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "domains.create_domain.13"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.domains.create_domain(
            domain=DomainCreatePayload(),
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains", None, 1)


def test_domains_create_domain_throws_payment_required_error() -> None:
    """Test CreateDomain endpoint error response (PaymentRequiredError) with WireMock"""
    test_id = "domains.create_domain.14"
    client = get_client(test_id)
    with pytest.raises(PaymentRequiredError) as exc_info:
        client.domains.create_domain(
            domain=DomainCreatePayload(),
        )
    assert exc_info.value.status_code == 402
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains", None, 1)


def test_domains_create_domain_throws_forbidden_error() -> None:
    """Test CreateDomain endpoint error response (ForbiddenError) with WireMock"""
    test_id = "domains.create_domain.15"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.domains.create_domain(
            domain=DomainCreatePayload(),
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains", None, 1)


def test_domains_create_domain_throws_not_found_error() -> None:
    """Test CreateDomain endpoint error response (NotFoundError) with WireMock"""
    test_id = "domains.create_domain.16"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.domains.create_domain(
            domain=DomainCreatePayload(),
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains", None, 1)


def test_domains_create_domain_throws_method_not_allowed_error() -> None:
    """Test CreateDomain endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "domains.create_domain.17"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.domains.create_domain(
            domain=DomainCreatePayload(),
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains", None, 1)


def test_domains_create_domain_throws_conflict_error() -> None:
    """Test CreateDomain endpoint error response (ConflictError) with WireMock"""
    test_id = "domains.create_domain.18"
    client = get_client(test_id)
    with pytest.raises(ConflictError) as exc_info:
        client.domains.create_domain(
            domain=DomainCreatePayload(),
        )
    assert exc_info.value.status_code == 409
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains", None, 1)


def test_domains_create_domain_throws_unsupported_media_type_error() -> None:
    """Test CreateDomain endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "domains.create_domain.19"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.domains.create_domain(
            domain=DomainCreatePayload(),
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains", None, 1)


def test_domains_create_domain_throws_unprocessable_entity_error() -> None:
    """Test CreateDomain endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "domains.create_domain.20"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.domains.create_domain(
            domain=DomainCreatePayload(),
        )
    assert exc_info.value.status_code == 422
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains", None, 1)


def test_domains_create_domain_throws_too_many_requests_error() -> None:
    """Test CreateDomain endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "domains.create_domain.21"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.domains.create_domain(
            domain=DomainCreatePayload(),
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains", None, 1)


def test_domains_create_domain_throws_unavailable_for_legal_reasons_error() -> None:
    """Test CreateDomain endpoint error response (UnavailableForLegalReasonsError) with WireMock"""
    test_id = "domains.create_domain.22"
    client = get_client(test_id)
    with pytest.raises(UnavailableForLegalReasonsError) as exc_info:
        client.domains.create_domain(
            domain=DomainCreatePayload(),
        )
    assert exc_info.value.status_code == 451
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains", None, 1)


def test_domains_create_domain_throws_internal_server_error() -> None:
    """Test CreateDomain endpoint error response (InternalServerError) with WireMock"""
    test_id = "domains.create_domain.23"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.domains.create_domain(
            domain=DomainCreatePayload(),
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains", None, 1)


def test_domains_create_domain_throws_not_implemented_error() -> None:
    """Test CreateDomain endpoint error response (NotImplementedError) with WireMock"""
    test_id = "domains.create_domain.24"
    client = get_client(test_id)
    with pytest.raises(NotImplementedError) as exc_info:
        client.domains.create_domain(
            domain=DomainCreatePayload(),
        )
    assert exc_info.value.status_code == 501
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains", None, 1)


def test_domains_create_domain_throws_bad_gateway_error() -> None:
    """Test CreateDomain endpoint error response (BadGatewayError) with WireMock"""
    test_id = "domains.create_domain.25"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.domains.create_domain(
            domain=DomainCreatePayload(),
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains", None, 1)


def test_domains_create_domain_throws_service_unavailable_error() -> None:
    """Test CreateDomain endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "domains.create_domain.26"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.domains.create_domain(
            domain=DomainCreatePayload(),
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains", None, 1)


def test_domains_create_domain_throws_gateway_timeout_error() -> None:
    """Test CreateDomain endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "domains.create_domain.27"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.domains.create_domain(
            domain=DomainCreatePayload(),
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains", None, 1)


def test_domains_get_domain() -> None:
    """Test GetDomain endpoint with WireMock"""
    test_id = "domains.get_domain.0"
    client = get_client(test_id)
    client.domains.get_domain(
        domain_name="example.com",
    )
    verify_request_count(test_id, "GET", "/core/v1/domains/example.com", None, 1)


def test_domains_get_domain_throws_unauthorized_error() -> None:
    """Test GetDomain endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "domains.get_domain.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.domains.get_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName", None, 1)


def test_domains_get_domain_throws_forbidden_error() -> None:
    """Test GetDomain endpoint error response (ForbiddenError) with WireMock"""
    test_id = "domains.get_domain.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.domains.get_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName", None, 1)


def test_domains_get_domain_throws_not_found_error() -> None:
    """Test GetDomain endpoint error response (NotFoundError) with WireMock"""
    test_id = "domains.get_domain.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.domains.get_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName", None, 1)


def test_domains_get_domain_throws_method_not_allowed_error() -> None:
    """Test GetDomain endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "domains.get_domain.4"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.domains.get_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName", None, 1)


def test_domains_get_domain_throws_too_many_requests_error() -> None:
    """Test GetDomain endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "domains.get_domain.5"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.domains.get_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName", None, 1)


def test_domains_get_domain_throws_internal_server_error() -> None:
    """Test GetDomain endpoint error response (InternalServerError) with WireMock"""
    test_id = "domains.get_domain.6"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.domains.get_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName", None, 1)


def test_domains_get_domain_throws_bad_gateway_error() -> None:
    """Test GetDomain endpoint error response (BadGatewayError) with WireMock"""
    test_id = "domains.get_domain.7"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.domains.get_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName", None, 1)


def test_domains_get_domain_throws_service_unavailable_error() -> None:
    """Test GetDomain endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "domains.get_domain.8"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.domains.get_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName", None, 1)


def test_domains_get_domain_throws_gateway_timeout_error() -> None:
    """Test GetDomain endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "domains.get_domain.9"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.domains.get_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName", None, 1)


def test_domains_update_domain() -> None:
    """Test UpdateDomain endpoint with WireMock"""
    test_id = "domains.update_domain.0"
    client = get_client(test_id)
    client.domains.update_domain(
        domain_name="domainName",
    )
    verify_request_count(test_id, "PATCH", "/core/v1/domains/domainName", None, 1)


def test_domains_update_domain_throws_bad_request_error() -> None:
    """Test UpdateDomain endpoint error response (BadRequestError) with WireMock"""
    test_id = "domains.update_domain.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.domains.update_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/core/v1/domains/domainName", None, 1)


def test_domains_update_domain_throws_unauthorized_error() -> None:
    """Test UpdateDomain endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "domains.update_domain.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.domains.update_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/core/v1/domains/domainName", None, 1)


def test_domains_update_domain_throws_forbidden_error() -> None:
    """Test UpdateDomain endpoint error response (ForbiddenError) with WireMock"""
    test_id = "domains.update_domain.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.domains.update_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/core/v1/domains/domainName", None, 1)


def test_domains_update_domain_throws_not_found_error() -> None:
    """Test UpdateDomain endpoint error response (NotFoundError) with WireMock"""
    test_id = "domains.update_domain.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.domains.update_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "PATCH", "/core/v1/domains/domainName", None, 1)


def test_domains_update_domain_throws_method_not_allowed_error() -> None:
    """Test UpdateDomain endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "domains.update_domain.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.domains.update_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/core/v1/domains/domainName", None, 1)


def test_domains_update_domain_throws_conflict_error() -> None:
    """Test UpdateDomain endpoint error response (ConflictError) with WireMock"""
    test_id = "domains.update_domain.6"
    client = get_client(test_id)
    with pytest.raises(ConflictError) as exc_info:
        client.domains.update_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 409
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/core/v1/domains/domainName", None, 1)


def test_domains_update_domain_throws_unsupported_media_type_error() -> None:
    """Test UpdateDomain endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "domains.update_domain.7"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.domains.update_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "PATCH", "/core/v1/domains/domainName", None, 1)


def test_domains_update_domain_throws_too_many_requests_error() -> None:
    """Test UpdateDomain endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "domains.update_domain.8"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.domains.update_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/core/v1/domains/domainName", None, 1)


def test_domains_update_domain_throws_internal_server_error() -> None:
    """Test UpdateDomain endpoint error response (InternalServerError) with WireMock"""
    test_id = "domains.update_domain.9"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.domains.update_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/core/v1/domains/domainName", None, 1)


def test_domains_update_domain_throws_bad_gateway_error() -> None:
    """Test UpdateDomain endpoint error response (BadGatewayError) with WireMock"""
    test_id = "domains.update_domain.10"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.domains.update_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/core/v1/domains/domainName", None, 1)


def test_domains_update_domain_throws_service_unavailable_error() -> None:
    """Test UpdateDomain endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "domains.update_domain.11"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.domains.update_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/core/v1/domains/domainName", None, 1)


def test_domains_update_domain_throws_gateway_timeout_error() -> None:
    """Test UpdateDomain endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "domains.update_domain.12"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.domains.update_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/core/v1/domains/domainName", None, 1)


def test_domains_disable_autorenew() -> None:
    """Test DisableAutorenew endpoint with WireMock"""
    test_id = "domains.disable_autorenew.0"
    client = get_client(test_id)
    client.domains.disable_autorenew(
        domain_name="example.com",
    )
    verify_request_count(test_id, "POST", "/core/v1/domains/example.com:disableAutorenew", None, 1)


def test_domains_disable_autorenew_throws_bad_request_error() -> None:
    """Test DisableAutorenew endpoint error response (BadRequestError) with WireMock"""
    test_id = "domains.disable_autorenew.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.domains.disable_autorenew(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:disableAutorenew", None, 1)


def test_domains_disable_autorenew_throws_unauthorized_error() -> None:
    """Test DisableAutorenew endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "domains.disable_autorenew.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.domains.disable_autorenew(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:disableAutorenew", None, 1)


def test_domains_disable_autorenew_throws_forbidden_error() -> None:
    """Test DisableAutorenew endpoint error response (ForbiddenError) with WireMock"""
    test_id = "domains.disable_autorenew.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.domains.disable_autorenew(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:disableAutorenew", None, 1)


def test_domains_disable_autorenew_throws_not_found_error() -> None:
    """Test DisableAutorenew endpoint error response (NotFoundError) with WireMock"""
    test_id = "domains.disable_autorenew.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.domains.disable_autorenew(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:disableAutorenew", None, 1)


def test_domains_disable_autorenew_throws_method_not_allowed_error() -> None:
    """Test DisableAutorenew endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "domains.disable_autorenew.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.domains.disable_autorenew(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:disableAutorenew", None, 1)


def test_domains_disable_autorenew_throws_unsupported_media_type_error() -> None:
    """Test DisableAutorenew endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "domains.disable_autorenew.6"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.domains.disable_autorenew(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:disableAutorenew", None, 1)


def test_domains_disable_autorenew_throws_too_many_requests_error() -> None:
    """Test DisableAutorenew endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "domains.disable_autorenew.7"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.domains.disable_autorenew(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:disableAutorenew", None, 1)


def test_domains_disable_autorenew_throws_internal_server_error() -> None:
    """Test DisableAutorenew endpoint error response (InternalServerError) with WireMock"""
    test_id = "domains.disable_autorenew.8"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.domains.disable_autorenew(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:disableAutorenew", None, 1)


def test_domains_disable_autorenew_throws_bad_gateway_error() -> None:
    """Test DisableAutorenew endpoint error response (BadGatewayError) with WireMock"""
    test_id = "domains.disable_autorenew.9"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.domains.disable_autorenew(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:disableAutorenew", None, 1)


def test_domains_disable_autorenew_throws_service_unavailable_error() -> None:
    """Test DisableAutorenew endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "domains.disable_autorenew.10"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.domains.disable_autorenew(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:disableAutorenew", None, 1)


def test_domains_disable_autorenew_throws_gateway_timeout_error() -> None:
    """Test DisableAutorenew endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "domains.disable_autorenew.11"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.domains.disable_autorenew(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:disableAutorenew", None, 1)


def test_domains_disable_whois_privacy() -> None:
    """Test DisableWhoisPrivacy endpoint with WireMock"""
    test_id = "domains.disable_whois_privacy.0"
    client = get_client(test_id)
    client.domains.disable_whois_privacy(
        domain_name="example.com",
    )
    verify_request_count(test_id, "POST", "/core/v1/domains/example.com:disableWhoisPrivacy", None, 1)


def test_domains_disable_whois_privacy_throws_bad_request_error() -> None:
    """Test DisableWhoisPrivacy endpoint error response (BadRequestError) with WireMock"""
    test_id = "domains.disable_whois_privacy.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.domains.disable_whois_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:disableWhoisPrivacy", None, 1)


def test_domains_disable_whois_privacy_throws_unauthorized_error() -> None:
    """Test DisableWhoisPrivacy endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "domains.disable_whois_privacy.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.domains.disable_whois_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:disableWhoisPrivacy", None, 1)


def test_domains_disable_whois_privacy_throws_forbidden_error() -> None:
    """Test DisableWhoisPrivacy endpoint error response (ForbiddenError) with WireMock"""
    test_id = "domains.disable_whois_privacy.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.domains.disable_whois_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:disableWhoisPrivacy", None, 1)


def test_domains_disable_whois_privacy_throws_not_found_error() -> None:
    """Test DisableWhoisPrivacy endpoint error response (NotFoundError) with WireMock"""
    test_id = "domains.disable_whois_privacy.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.domains.disable_whois_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:disableWhoisPrivacy", None, 1)


def test_domains_disable_whois_privacy_throws_method_not_allowed_error() -> None:
    """Test DisableWhoisPrivacy endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "domains.disable_whois_privacy.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.domains.disable_whois_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:disableWhoisPrivacy", None, 1)


def test_domains_disable_whois_privacy_throws_unsupported_media_type_error() -> None:
    """Test DisableWhoisPrivacy endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "domains.disable_whois_privacy.6"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.domains.disable_whois_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:disableWhoisPrivacy", None, 1)


def test_domains_disable_whois_privacy_throws_too_many_requests_error() -> None:
    """Test DisableWhoisPrivacy endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "domains.disable_whois_privacy.7"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.domains.disable_whois_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:disableWhoisPrivacy", None, 1)


def test_domains_disable_whois_privacy_throws_internal_server_error() -> None:
    """Test DisableWhoisPrivacy endpoint error response (InternalServerError) with WireMock"""
    test_id = "domains.disable_whois_privacy.8"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.domains.disable_whois_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:disableWhoisPrivacy", None, 1)


def test_domains_disable_whois_privacy_throws_bad_gateway_error() -> None:
    """Test DisableWhoisPrivacy endpoint error response (BadGatewayError) with WireMock"""
    test_id = "domains.disable_whois_privacy.9"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.domains.disable_whois_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:disableWhoisPrivacy", None, 1)


def test_domains_disable_whois_privacy_throws_service_unavailable_error() -> None:
    """Test DisableWhoisPrivacy endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "domains.disable_whois_privacy.10"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.domains.disable_whois_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:disableWhoisPrivacy", None, 1)


def test_domains_disable_whois_privacy_throws_gateway_timeout_error() -> None:
    """Test DisableWhoisPrivacy endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "domains.disable_whois_privacy.11"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.domains.disable_whois_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:disableWhoisPrivacy", None, 1)


def test_domains_enable_autorenew() -> None:
    """Test EnableAutorenew endpoint with WireMock"""
    test_id = "domains.enable_autorenew.0"
    client = get_client(test_id)
    client.domains.enable_autorenew(
        domain_name="example.com",
    )
    verify_request_count(test_id, "POST", "/core/v1/domains/example.com:enableAutorenew", None, 1)


def test_domains_enable_autorenew_throws_bad_request_error() -> None:
    """Test EnableAutorenew endpoint error response (BadRequestError) with WireMock"""
    test_id = "domains.enable_autorenew.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.domains.enable_autorenew(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:enableAutorenew", None, 1)


def test_domains_enable_autorenew_throws_unauthorized_error() -> None:
    """Test EnableAutorenew endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "domains.enable_autorenew.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.domains.enable_autorenew(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:enableAutorenew", None, 1)


def test_domains_enable_autorenew_throws_forbidden_error() -> None:
    """Test EnableAutorenew endpoint error response (ForbiddenError) with WireMock"""
    test_id = "domains.enable_autorenew.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.domains.enable_autorenew(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:enableAutorenew", None, 1)


def test_domains_enable_autorenew_throws_not_found_error() -> None:
    """Test EnableAutorenew endpoint error response (NotFoundError) with WireMock"""
    test_id = "domains.enable_autorenew.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.domains.enable_autorenew(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:enableAutorenew", None, 1)


def test_domains_enable_autorenew_throws_method_not_allowed_error() -> None:
    """Test EnableAutorenew endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "domains.enable_autorenew.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.domains.enable_autorenew(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:enableAutorenew", None, 1)


def test_domains_enable_autorenew_throws_unsupported_media_type_error() -> None:
    """Test EnableAutorenew endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "domains.enable_autorenew.6"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.domains.enable_autorenew(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:enableAutorenew", None, 1)


def test_domains_enable_autorenew_throws_too_many_requests_error() -> None:
    """Test EnableAutorenew endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "domains.enable_autorenew.7"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.domains.enable_autorenew(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:enableAutorenew", None, 1)


def test_domains_enable_autorenew_throws_internal_server_error() -> None:
    """Test EnableAutorenew endpoint error response (InternalServerError) with WireMock"""
    test_id = "domains.enable_autorenew.8"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.domains.enable_autorenew(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:enableAutorenew", None, 1)


def test_domains_enable_autorenew_throws_bad_gateway_error() -> None:
    """Test EnableAutorenew endpoint error response (BadGatewayError) with WireMock"""
    test_id = "domains.enable_autorenew.9"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.domains.enable_autorenew(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:enableAutorenew", None, 1)


def test_domains_enable_autorenew_throws_service_unavailable_error() -> None:
    """Test EnableAutorenew endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "domains.enable_autorenew.10"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.domains.enable_autorenew(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:enableAutorenew", None, 1)


def test_domains_enable_autorenew_throws_gateway_timeout_error() -> None:
    """Test EnableAutorenew endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "domains.enable_autorenew.11"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.domains.enable_autorenew(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:enableAutorenew", None, 1)


def test_domains_enable_whois_privacy() -> None:
    """Test EnableWhoisPrivacy endpoint with WireMock"""
    test_id = "domains.enable_whois_privacy.0"
    client = get_client(test_id)
    client.domains.enable_whois_privacy(
        domain_name="domainName",
    )
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:enableWhoisPrivacy", None, 1)


def test_domains_enable_whois_privacy_throws_bad_request_error() -> None:
    """Test EnableWhoisPrivacy endpoint error response (BadRequestError) with WireMock"""
    test_id = "domains.enable_whois_privacy.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.domains.enable_whois_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:enableWhoisPrivacy", None, 1)


def test_domains_enable_whois_privacy_throws_unauthorized_error() -> None:
    """Test EnableWhoisPrivacy endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "domains.enable_whois_privacy.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.domains.enable_whois_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:enableWhoisPrivacy", None, 1)


def test_domains_enable_whois_privacy_throws_forbidden_error() -> None:
    """Test EnableWhoisPrivacy endpoint error response (ForbiddenError) with WireMock"""
    test_id = "domains.enable_whois_privacy.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.domains.enable_whois_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:enableWhoisPrivacy", None, 1)


def test_domains_enable_whois_privacy_throws_not_found_error() -> None:
    """Test EnableWhoisPrivacy endpoint error response (NotFoundError) with WireMock"""
    test_id = "domains.enable_whois_privacy.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.domains.enable_whois_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:enableWhoisPrivacy", None, 1)


def test_domains_enable_whois_privacy_throws_method_not_allowed_error() -> None:
    """Test EnableWhoisPrivacy endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "domains.enable_whois_privacy.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.domains.enable_whois_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:enableWhoisPrivacy", None, 1)


def test_domains_enable_whois_privacy_throws_unsupported_media_type_error() -> None:
    """Test EnableWhoisPrivacy endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "domains.enable_whois_privacy.6"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.domains.enable_whois_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:enableWhoisPrivacy", None, 1)


def test_domains_enable_whois_privacy_throws_too_many_requests_error() -> None:
    """Test EnableWhoisPrivacy endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "domains.enable_whois_privacy.7"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.domains.enable_whois_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:enableWhoisPrivacy", None, 1)


def test_domains_enable_whois_privacy_throws_internal_server_error() -> None:
    """Test EnableWhoisPrivacy endpoint error response (InternalServerError) with WireMock"""
    test_id = "domains.enable_whois_privacy.8"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.domains.enable_whois_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:enableWhoisPrivacy", None, 1)


def test_domains_enable_whois_privacy_throws_bad_gateway_error() -> None:
    """Test EnableWhoisPrivacy endpoint error response (BadGatewayError) with WireMock"""
    test_id = "domains.enable_whois_privacy.9"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.domains.enable_whois_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:enableWhoisPrivacy", None, 1)


def test_domains_enable_whois_privacy_throws_service_unavailable_error() -> None:
    """Test EnableWhoisPrivacy endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "domains.enable_whois_privacy.10"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.domains.enable_whois_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:enableWhoisPrivacy", None, 1)


def test_domains_enable_whois_privacy_throws_gateway_timeout_error() -> None:
    """Test EnableWhoisPrivacy endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "domains.enable_whois_privacy.11"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.domains.enable_whois_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:enableWhoisPrivacy", None, 1)


def test_domains_get_auth_code_for_domain() -> None:
    """Test GetAuthCodeForDomain endpoint with WireMock"""
    test_id = "domains.get_auth_code_for_domain.0"
    client = get_client(test_id)
    client.domains.get_auth_code_for_domain(
        domain_name="domainName",
    )
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName:getAuthCode", None, 1)


def test_domains_get_auth_code_for_domain_throws_unauthorized_error() -> None:
    """Test GetAuthCodeForDomain endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "domains.get_auth_code_for_domain.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.domains.get_auth_code_for_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName:getAuthCode", None, 1)


def test_domains_get_auth_code_for_domain_throws_forbidden_error() -> None:
    """Test GetAuthCodeForDomain endpoint error response (ForbiddenError) with WireMock"""
    test_id = "domains.get_auth_code_for_domain.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.domains.get_auth_code_for_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName:getAuthCode", None, 1)


def test_domains_get_auth_code_for_domain_throws_not_found_error() -> None:
    """Test GetAuthCodeForDomain endpoint error response (NotFoundError) with WireMock"""
    test_id = "domains.get_auth_code_for_domain.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.domains.get_auth_code_for_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName:getAuthCode", None, 1)


def test_domains_get_auth_code_for_domain_throws_method_not_allowed_error() -> None:
    """Test GetAuthCodeForDomain endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "domains.get_auth_code_for_domain.4"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.domains.get_auth_code_for_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName:getAuthCode", None, 1)


def test_domains_get_auth_code_for_domain_throws_not_acceptable_error() -> None:
    """Test GetAuthCodeForDomain endpoint error response (NotAcceptableError) with WireMock"""
    test_id = "domains.get_auth_code_for_domain.5"
    client = get_client(test_id)
    with pytest.raises(NotAcceptableError) as exc_info:
        client.domains.get_auth_code_for_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 406
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName:getAuthCode", None, 1)


def test_domains_get_auth_code_for_domain_throws_too_many_requests_error() -> None:
    """Test GetAuthCodeForDomain endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "domains.get_auth_code_for_domain.6"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.domains.get_auth_code_for_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName:getAuthCode", None, 1)


def test_domains_get_auth_code_for_domain_throws_internal_server_error() -> None:
    """Test GetAuthCodeForDomain endpoint error response (InternalServerError) with WireMock"""
    test_id = "domains.get_auth_code_for_domain.7"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.domains.get_auth_code_for_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName:getAuthCode", None, 1)


def test_domains_get_auth_code_for_domain_throws_bad_gateway_error() -> None:
    """Test GetAuthCodeForDomain endpoint error response (BadGatewayError) with WireMock"""
    test_id = "domains.get_auth_code_for_domain.8"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.domains.get_auth_code_for_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName:getAuthCode", None, 1)


def test_domains_get_auth_code_for_domain_throws_service_unavailable_error() -> None:
    """Test GetAuthCodeForDomain endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "domains.get_auth_code_for_domain.9"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.domains.get_auth_code_for_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName:getAuthCode", None, 1)


def test_domains_get_auth_code_for_domain_throws_gateway_timeout_error() -> None:
    """Test GetAuthCodeForDomain endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "domains.get_auth_code_for_domain.10"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.domains.get_auth_code_for_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName:getAuthCode", None, 1)


def test_domains_get_pricing_for_domain() -> None:
    """Test GetPricingForDomain endpoint with WireMock"""
    test_id = "domains.get_pricing_for_domain.0"
    client = get_client(test_id)
    client.domains.get_pricing_for_domain(
        domain_name="domainName",
        years=2,
    )
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName:getPricing", {"years": "2"}, 1)


def test_domains_get_pricing_for_domain_throws_bad_request_error() -> None:
    """Test GetPricingForDomain endpoint error response (BadRequestError) with WireMock"""
    test_id = "domains.get_pricing_for_domain.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.domains.get_pricing_for_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName:getPricing", None, 1)


def test_domains_get_pricing_for_domain_throws_unauthorized_error() -> None:
    """Test GetPricingForDomain endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "domains.get_pricing_for_domain.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.domains.get_pricing_for_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName:getPricing", None, 1)


def test_domains_get_pricing_for_domain_throws_forbidden_error() -> None:
    """Test GetPricingForDomain endpoint error response (ForbiddenError) with WireMock"""
    test_id = "domains.get_pricing_for_domain.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.domains.get_pricing_for_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName:getPricing", None, 1)


def test_domains_get_pricing_for_domain_throws_not_found_error() -> None:
    """Test GetPricingForDomain endpoint error response (NotFoundError) with WireMock"""
    test_id = "domains.get_pricing_for_domain.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.domains.get_pricing_for_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName:getPricing", None, 1)


def test_domains_get_pricing_for_domain_throws_method_not_allowed_error() -> None:
    """Test GetPricingForDomain endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "domains.get_pricing_for_domain.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.domains.get_pricing_for_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName:getPricing", None, 1)


def test_domains_get_pricing_for_domain_throws_unprocessable_entity_error() -> None:
    """Test GetPricingForDomain endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "domains.get_pricing_for_domain.6"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.domains.get_pricing_for_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 422
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName:getPricing", None, 1)


def test_domains_get_pricing_for_domain_throws_too_many_requests_error() -> None:
    """Test GetPricingForDomain endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "domains.get_pricing_for_domain.7"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.domains.get_pricing_for_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName:getPricing", None, 1)


def test_domains_get_pricing_for_domain_throws_internal_server_error() -> None:
    """Test GetPricingForDomain endpoint error response (InternalServerError) with WireMock"""
    test_id = "domains.get_pricing_for_domain.8"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.domains.get_pricing_for_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName:getPricing", None, 1)


def test_domains_get_pricing_for_domain_throws_bad_gateway_error() -> None:
    """Test GetPricingForDomain endpoint error response (BadGatewayError) with WireMock"""
    test_id = "domains.get_pricing_for_domain.9"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.domains.get_pricing_for_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName:getPricing", None, 1)


def test_domains_get_pricing_for_domain_throws_service_unavailable_error() -> None:
    """Test GetPricingForDomain endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "domains.get_pricing_for_domain.10"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.domains.get_pricing_for_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName:getPricing", None, 1)


def test_domains_get_pricing_for_domain_throws_gateway_timeout_error() -> None:
    """Test GetPricingForDomain endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "domains.get_pricing_for_domain.11"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.domains.get_pricing_for_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domains/domainName:getPricing", None, 1)


def test_domains_lock_domain() -> None:
    """Test LockDomain endpoint with WireMock"""
    test_id = "domains.lock_domain.0"
    client = get_client(test_id)
    client.domains.lock_domain(
        domain_name="example.com",
    )
    verify_request_count(test_id, "POST", "/core/v1/domains/example.com:lock", None, 1)


def test_domains_lock_domain_throws_bad_request_error() -> None:
    """Test LockDomain endpoint error response (BadRequestError) with WireMock"""
    test_id = "domains.lock_domain.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.domains.lock_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:lock", None, 1)


def test_domains_lock_domain_throws_unauthorized_error() -> None:
    """Test LockDomain endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "domains.lock_domain.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.domains.lock_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:lock", None, 1)


def test_domains_lock_domain_throws_forbidden_error() -> None:
    """Test LockDomain endpoint error response (ForbiddenError) with WireMock"""
    test_id = "domains.lock_domain.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.domains.lock_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:lock", None, 1)


def test_domains_lock_domain_throws_not_found_error() -> None:
    """Test LockDomain endpoint error response (NotFoundError) with WireMock"""
    test_id = "domains.lock_domain.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.domains.lock_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:lock", None, 1)


def test_domains_lock_domain_throws_method_not_allowed_error() -> None:
    """Test LockDomain endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "domains.lock_domain.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.domains.lock_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:lock", None, 1)


def test_domains_lock_domain_throws_unsupported_media_type_error() -> None:
    """Test LockDomain endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "domains.lock_domain.6"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.domains.lock_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:lock", None, 1)


def test_domains_lock_domain_throws_too_many_requests_error() -> None:
    """Test LockDomain endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "domains.lock_domain.7"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.domains.lock_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:lock", None, 1)


def test_domains_lock_domain_throws_internal_server_error() -> None:
    """Test LockDomain endpoint error response (InternalServerError) with WireMock"""
    test_id = "domains.lock_domain.8"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.domains.lock_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:lock", None, 1)


def test_domains_lock_domain_throws_bad_gateway_error() -> None:
    """Test LockDomain endpoint error response (BadGatewayError) with WireMock"""
    test_id = "domains.lock_domain.9"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.domains.lock_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:lock", None, 1)


def test_domains_lock_domain_throws_service_unavailable_error() -> None:
    """Test LockDomain endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "domains.lock_domain.10"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.domains.lock_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:lock", None, 1)


def test_domains_lock_domain_throws_gateway_timeout_error() -> None:
    """Test LockDomain endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "domains.lock_domain.11"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.domains.lock_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:lock", None, 1)


def test_domains_purchase_privacy() -> None:
    """Test PurchasePrivacy endpoint with WireMock"""
    test_id = "domains.purchase_privacy.0"
    client = get_client(test_id)
    client.domains.purchase_privacy(
        domain_name="domainName",
    )
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:purchasePrivacy", None, 1)


def test_domains_purchase_privacy_throws_unauthorized_error() -> None:
    """Test PurchasePrivacy endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "domains.purchase_privacy.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.domains.purchase_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:purchasePrivacy", None, 1)


def test_domains_purchase_privacy_throws_payment_required_error() -> None:
    """Test PurchasePrivacy endpoint error response (PaymentRequiredError) with WireMock"""
    test_id = "domains.purchase_privacy.2"
    client = get_client(test_id)
    with pytest.raises(PaymentRequiredError) as exc_info:
        client.domains.purchase_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 402
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:purchasePrivacy", None, 1)


def test_domains_purchase_privacy_throws_forbidden_error() -> None:
    """Test PurchasePrivacy endpoint error response (ForbiddenError) with WireMock"""
    test_id = "domains.purchase_privacy.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.domains.purchase_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:purchasePrivacy", None, 1)


def test_domains_purchase_privacy_throws_not_found_error() -> None:
    """Test PurchasePrivacy endpoint error response (NotFoundError) with WireMock"""
    test_id = "domains.purchase_privacy.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.domains.purchase_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:purchasePrivacy", None, 1)


def test_domains_purchase_privacy_throws_method_not_allowed_error() -> None:
    """Test PurchasePrivacy endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "domains.purchase_privacy.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.domains.purchase_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:purchasePrivacy", None, 1)


def test_domains_purchase_privacy_throws_conflict_error() -> None:
    """Test PurchasePrivacy endpoint error response (ConflictError) with WireMock"""
    test_id = "domains.purchase_privacy.6"
    client = get_client(test_id)
    with pytest.raises(ConflictError) as exc_info:
        client.domains.purchase_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 409
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:purchasePrivacy", None, 1)


def test_domains_purchase_privacy_throws_unsupported_media_type_error() -> None:
    """Test PurchasePrivacy endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "domains.purchase_privacy.7"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.domains.purchase_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:purchasePrivacy", None, 1)


def test_domains_purchase_privacy_throws_unprocessable_entity_error() -> None:
    """Test PurchasePrivacy endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "domains.purchase_privacy.8"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.domains.purchase_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 422
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:purchasePrivacy", None, 1)


def test_domains_purchase_privacy_throws_too_many_requests_error() -> None:
    """Test PurchasePrivacy endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "domains.purchase_privacy.9"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.domains.purchase_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:purchasePrivacy", None, 1)


def test_domains_purchase_privacy_throws_internal_server_error() -> None:
    """Test PurchasePrivacy endpoint error response (InternalServerError) with WireMock"""
    test_id = "domains.purchase_privacy.10"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.domains.purchase_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:purchasePrivacy", None, 1)


def test_domains_purchase_privacy_throws_bad_gateway_error() -> None:
    """Test PurchasePrivacy endpoint error response (BadGatewayError) with WireMock"""
    test_id = "domains.purchase_privacy.11"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.domains.purchase_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:purchasePrivacy", None, 1)


def test_domains_purchase_privacy_throws_service_unavailable_error() -> None:
    """Test PurchasePrivacy endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "domains.purchase_privacy.12"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.domains.purchase_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:purchasePrivacy", None, 1)


def test_domains_purchase_privacy_throws_gateway_timeout_error() -> None:
    """Test PurchasePrivacy endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "domains.purchase_privacy.13"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.domains.purchase_privacy(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:purchasePrivacy", None, 1)


def test_domains_renew_domain() -> None:
    """Test RenewDomain endpoint with WireMock"""
    test_id = "domains.renew_domain.0"
    client = get_client(test_id)
    client.domains.renew_domain(
        domain_name="domainName",
    )
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:renew", None, 1)


def test_domains_renew_domain_throws_bad_request_error() -> None:
    """Test RenewDomain endpoint error response (BadRequestError) with WireMock"""
    test_id = "domains.renew_domain.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.domains.renew_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:renew", None, 1)


def test_domains_renew_domain_throws_unauthorized_error() -> None:
    """Test RenewDomain endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "domains.renew_domain.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.domains.renew_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:renew", None, 1)


def test_domains_renew_domain_throws_forbidden_error() -> None:
    """Test RenewDomain endpoint error response (ForbiddenError) with WireMock"""
    test_id = "domains.renew_domain.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.domains.renew_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:renew", None, 1)


def test_domains_renew_domain_throws_not_found_error() -> None:
    """Test RenewDomain endpoint error response (NotFoundError) with WireMock"""
    test_id = "domains.renew_domain.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.domains.renew_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:renew", None, 1)


def test_domains_renew_domain_throws_method_not_allowed_error() -> None:
    """Test RenewDomain endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "domains.renew_domain.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.domains.renew_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:renew", None, 1)


def test_domains_renew_domain_throws_unsupported_media_type_error() -> None:
    """Test RenewDomain endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "domains.renew_domain.6"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.domains.renew_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:renew", None, 1)


def test_domains_renew_domain_throws_unprocessable_entity_error() -> None:
    """Test RenewDomain endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "domains.renew_domain.7"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.domains.renew_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 422
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:renew", None, 1)


def test_domains_renew_domain_throws_too_many_requests_error() -> None:
    """Test RenewDomain endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "domains.renew_domain.8"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.domains.renew_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:renew", None, 1)


def test_domains_renew_domain_throws_internal_server_error() -> None:
    """Test RenewDomain endpoint error response (InternalServerError) with WireMock"""
    test_id = "domains.renew_domain.9"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.domains.renew_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:renew", None, 1)


def test_domains_renew_domain_throws_bad_gateway_error() -> None:
    """Test RenewDomain endpoint error response (BadGatewayError) with WireMock"""
    test_id = "domains.renew_domain.10"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.domains.renew_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:renew", None, 1)


def test_domains_renew_domain_throws_service_unavailable_error() -> None:
    """Test RenewDomain endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "domains.renew_domain.11"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.domains.renew_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:renew", None, 1)


def test_domains_renew_domain_throws_gateway_timeout_error() -> None:
    """Test RenewDomain endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "domains.renew_domain.12"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.domains.renew_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:renew", None, 1)


def test_domains_set_contacts() -> None:
    """Test SetContacts endpoint with WireMock"""
    test_id = "domains.set_contacts.0"
    client = get_client(test_id)
    client.domains.set_contacts(
        domain_name="example.com",
        contacts=ContactsRequest(),
    )
    verify_request_count(test_id, "POST", "/core/v1/domains/example.com:setContacts", None, 1)


def test_domains_set_contacts_throws_bad_request_error() -> None:
    """Test SetContacts endpoint error response (BadRequestError) with WireMock"""
    test_id = "domains.set_contacts.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.domains.set_contacts(
            domain_name="domainName",
            contacts=ContactsRequest(),
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:setContacts", None, 1)


def test_domains_set_contacts_throws_unauthorized_error() -> None:
    """Test SetContacts endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "domains.set_contacts.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.domains.set_contacts(
            domain_name="domainName",
            contacts=ContactsRequest(),
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:setContacts", None, 1)


def test_domains_set_contacts_throws_forbidden_error() -> None:
    """Test SetContacts endpoint error response (ForbiddenError) with WireMock"""
    test_id = "domains.set_contacts.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.domains.set_contacts(
            domain_name="domainName",
            contacts=ContactsRequest(),
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:setContacts", None, 1)


def test_domains_set_contacts_throws_not_found_error() -> None:
    """Test SetContacts endpoint error response (NotFoundError) with WireMock"""
    test_id = "domains.set_contacts.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.domains.set_contacts(
            domain_name="domainName",
            contacts=ContactsRequest(),
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:setContacts", None, 1)


def test_domains_set_contacts_throws_method_not_allowed_error() -> None:
    """Test SetContacts endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "domains.set_contacts.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.domains.set_contacts(
            domain_name="domainName",
            contacts=ContactsRequest(),
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:setContacts", None, 1)


def test_domains_set_contacts_throws_unsupported_media_type_error() -> None:
    """Test SetContacts endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "domains.set_contacts.6"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.domains.set_contacts(
            domain_name="domainName",
            contacts=ContactsRequest(),
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:setContacts", None, 1)


def test_domains_set_contacts_throws_too_many_requests_error() -> None:
    """Test SetContacts endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "domains.set_contacts.7"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.domains.set_contacts(
            domain_name="domainName",
            contacts=ContactsRequest(),
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:setContacts", None, 1)


def test_domains_set_contacts_throws_internal_server_error() -> None:
    """Test SetContacts endpoint error response (InternalServerError) with WireMock"""
    test_id = "domains.set_contacts.8"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.domains.set_contacts(
            domain_name="domainName",
            contacts=ContactsRequest(),
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:setContacts", None, 1)


def test_domains_set_contacts_throws_bad_gateway_error() -> None:
    """Test SetContacts endpoint error response (BadGatewayError) with WireMock"""
    test_id = "domains.set_contacts.9"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.domains.set_contacts(
            domain_name="domainName",
            contacts=ContactsRequest(),
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:setContacts", None, 1)


def test_domains_set_contacts_throws_service_unavailable_error() -> None:
    """Test SetContacts endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "domains.set_contacts.10"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.domains.set_contacts(
            domain_name="domainName",
            contacts=ContactsRequest(),
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:setContacts", None, 1)


def test_domains_set_contacts_throws_gateway_timeout_error() -> None:
    """Test SetContacts endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "domains.set_contacts.11"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.domains.set_contacts(
            domain_name="domainName",
            contacts=ContactsRequest(),
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:setContacts", None, 1)


def test_domains_set_nameservers() -> None:
    """Test SetNameservers endpoint with WireMock"""
    test_id = "domains.set_nameservers.0"
    client = get_client(test_id)
    client.domains.set_nameservers(
        domain_name="example.com",
        nameservers=["ns1.name.com", "ns2.name.com"],
    )
    verify_request_count(test_id, "POST", "/core/v1/domains/example.com:setNameservers", None, 1)


def test_domains_set_nameservers_throws_bad_request_error() -> None:
    """Test SetNameservers endpoint error response (BadRequestError) with WireMock"""
    test_id = "domains.set_nameservers.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.domains.set_nameservers(
            domain_name="domainName",
            nameservers=["nameservers", "nameservers"],
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:setNameservers", None, 1)


def test_domains_set_nameservers_throws_unauthorized_error() -> None:
    """Test SetNameservers endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "domains.set_nameservers.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.domains.set_nameservers(
            domain_name="domainName",
            nameservers=["nameservers", "nameservers"],
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:setNameservers", None, 1)


def test_domains_set_nameservers_throws_forbidden_error() -> None:
    """Test SetNameservers endpoint error response (ForbiddenError) with WireMock"""
    test_id = "domains.set_nameservers.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.domains.set_nameservers(
            domain_name="domainName",
            nameservers=["nameservers", "nameservers"],
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:setNameservers", None, 1)


def test_domains_set_nameservers_throws_not_found_error() -> None:
    """Test SetNameservers endpoint error response (NotFoundError) with WireMock"""
    test_id = "domains.set_nameservers.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.domains.set_nameservers(
            domain_name="domainName",
            nameservers=["nameservers", "nameservers"],
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:setNameservers", None, 1)


def test_domains_set_nameservers_throws_method_not_allowed_error() -> None:
    """Test SetNameservers endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "domains.set_nameservers.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.domains.set_nameservers(
            domain_name="domainName",
            nameservers=["nameservers", "nameservers"],
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:setNameservers", None, 1)


def test_domains_set_nameservers_throws_unsupported_media_type_error() -> None:
    """Test SetNameservers endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "domains.set_nameservers.6"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.domains.set_nameservers(
            domain_name="domainName",
            nameservers=["nameservers", "nameservers"],
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:setNameservers", None, 1)


def test_domains_set_nameservers_throws_too_many_requests_error() -> None:
    """Test SetNameservers endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "domains.set_nameservers.7"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.domains.set_nameservers(
            domain_name="domainName",
            nameservers=["nameservers", "nameservers"],
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:setNameservers", None, 1)


def test_domains_set_nameservers_throws_internal_server_error() -> None:
    """Test SetNameservers endpoint error response (InternalServerError) with WireMock"""
    test_id = "domains.set_nameservers.8"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.domains.set_nameservers(
            domain_name="domainName",
            nameservers=["nameservers", "nameservers"],
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:setNameservers", None, 1)


def test_domains_set_nameservers_throws_bad_gateway_error() -> None:
    """Test SetNameservers endpoint error response (BadGatewayError) with WireMock"""
    test_id = "domains.set_nameservers.9"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.domains.set_nameservers(
            domain_name="domainName",
            nameservers=["nameservers", "nameservers"],
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:setNameservers", None, 1)


def test_domains_set_nameservers_throws_service_unavailable_error() -> None:
    """Test SetNameservers endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "domains.set_nameservers.10"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.domains.set_nameservers(
            domain_name="domainName",
            nameservers=["nameservers", "nameservers"],
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:setNameservers", None, 1)


def test_domains_set_nameservers_throws_gateway_timeout_error() -> None:
    """Test SetNameservers endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "domains.set_nameservers.11"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.domains.set_nameservers(
            domain_name="domainName",
            nameservers=["nameservers", "nameservers"],
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:setNameservers", None, 1)


def test_domains_unlock_domain() -> None:
    """Test UnlockDomain endpoint with WireMock"""
    test_id = "domains.unlock_domain.0"
    client = get_client(test_id)
    client.domains.unlock_domain(
        domain_name="domainName",
    )
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:unlock", None, 1)


def test_domains_unlock_domain_throws_bad_request_error() -> None:
    """Test UnlockDomain endpoint error response (BadRequestError) with WireMock"""
    test_id = "domains.unlock_domain.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.domains.unlock_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:unlock", None, 1)


def test_domains_unlock_domain_throws_unauthorized_error() -> None:
    """Test UnlockDomain endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "domains.unlock_domain.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.domains.unlock_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:unlock", None, 1)


def test_domains_unlock_domain_throws_forbidden_error() -> None:
    """Test UnlockDomain endpoint error response (ForbiddenError) with WireMock"""
    test_id = "domains.unlock_domain.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.domains.unlock_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:unlock", None, 1)


def test_domains_unlock_domain_throws_not_found_error() -> None:
    """Test UnlockDomain endpoint error response (NotFoundError) with WireMock"""
    test_id = "domains.unlock_domain.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.domains.unlock_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:unlock", None, 1)


def test_domains_unlock_domain_throws_method_not_allowed_error() -> None:
    """Test UnlockDomain endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "domains.unlock_domain.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.domains.unlock_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:unlock", None, 1)


def test_domains_unlock_domain_throws_unsupported_media_type_error() -> None:
    """Test UnlockDomain endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "domains.unlock_domain.6"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.domains.unlock_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:unlock", None, 1)


def test_domains_unlock_domain_throws_too_many_requests_error() -> None:
    """Test UnlockDomain endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "domains.unlock_domain.7"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.domains.unlock_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:unlock", None, 1)


def test_domains_unlock_domain_throws_internal_server_error() -> None:
    """Test UnlockDomain endpoint error response (InternalServerError) with WireMock"""
    test_id = "domains.unlock_domain.8"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.domains.unlock_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:unlock", None, 1)


def test_domains_unlock_domain_throws_bad_gateway_error() -> None:
    """Test UnlockDomain endpoint error response (BadGatewayError) with WireMock"""
    test_id = "domains.unlock_domain.9"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.domains.unlock_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:unlock", None, 1)


def test_domains_unlock_domain_throws_service_unavailable_error() -> None:
    """Test UnlockDomain endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "domains.unlock_domain.10"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.domains.unlock_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:unlock", None, 1)


def test_domains_unlock_domain_throws_gateway_timeout_error() -> None:
    """Test UnlockDomain endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "domains.unlock_domain.11"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.domains.unlock_domain(
            domain_name="domainName",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains/domainName:unlock", None, 1)


def test_domains_check_availability() -> None:
    """Test CheckAvailability endpoint with WireMock"""
    test_id = "domains.check_availability.0"
    client = get_client(test_id)
    client.domains.check_availability(
        domain_names=["domainNames"],
    )
    verify_request_count(test_id, "POST", "/core/v1/domains:checkAvailability", None, 1)


def test_domains_check_availability_throws_unauthorized_error() -> None:
    """Test CheckAvailability endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "domains.check_availability.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.domains.check_availability(
            domain_names=["domainNames", "domainNames"],
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains:checkAvailability", None, 1)


def test_domains_check_availability_throws_forbidden_error() -> None:
    """Test CheckAvailability endpoint error response (ForbiddenError) with WireMock"""
    test_id = "domains.check_availability.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.domains.check_availability(
            domain_names=["domainNames", "domainNames"],
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains:checkAvailability", None, 1)


def test_domains_check_availability_throws_method_not_allowed_error() -> None:
    """Test CheckAvailability endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "domains.check_availability.3"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.domains.check_availability(
            domain_names=["domainNames", "domainNames"],
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains:checkAvailability", None, 1)


def test_domains_check_availability_throws_unsupported_media_type_error() -> None:
    """Test CheckAvailability endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "domains.check_availability.4"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.domains.check_availability(
            domain_names=["domainNames", "domainNames"],
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains:checkAvailability", None, 1)


def test_domains_check_availability_throws_unprocessable_entity_error() -> None:
    """Test CheckAvailability endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "domains.check_availability.5"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.domains.check_availability(
            domain_names=["domainNames", "domainNames"],
        )
    assert exc_info.value.status_code == 422
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains:checkAvailability", None, 1)


def test_domains_check_availability_throws_too_many_requests_error() -> None:
    """Test CheckAvailability endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "domains.check_availability.6"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.domains.check_availability(
            domain_names=["domainNames", "domainNames"],
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains:checkAvailability", None, 1)


def test_domains_check_availability_throws_internal_server_error() -> None:
    """Test CheckAvailability endpoint error response (InternalServerError) with WireMock"""
    test_id = "domains.check_availability.7"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.domains.check_availability(
            domain_names=["domainNames", "domainNames"],
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains:checkAvailability", None, 1)


def test_domains_check_availability_throws_bad_gateway_error() -> None:
    """Test CheckAvailability endpoint error response (BadGatewayError) with WireMock"""
    test_id = "domains.check_availability.8"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.domains.check_availability(
            domain_names=["domainNames", "domainNames"],
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains:checkAvailability", None, 1)


def test_domains_check_availability_throws_service_unavailable_error() -> None:
    """Test CheckAvailability endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "domains.check_availability.9"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.domains.check_availability(
            domain_names=["domainNames", "domainNames"],
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains:checkAvailability", None, 1)


def test_domains_check_availability_throws_gateway_timeout_error() -> None:
    """Test CheckAvailability endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "domains.check_availability.10"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.domains.check_availability(
            domain_names=["domainNames", "domainNames"],
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains:checkAvailability", None, 1)


def test_domains_search() -> None:
    """Test Search endpoint with WireMock"""
    test_id = "domains.search.0"
    client = get_client(test_id)
    client.domains.search(
        keyword="mydomain",
    )
    verify_request_count(test_id, "POST", "/core/v1/domains:search", None, 1)


def test_domains_search_throws_bad_request_error() -> None:
    """Test Search endpoint error response (BadRequestError) with WireMock"""
    test_id = "domains.search.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.domains.search(
            keyword="keyword",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains:search", None, 1)


def test_domains_search_throws_unauthorized_error() -> None:
    """Test Search endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "domains.search.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.domains.search(
            keyword="keyword",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains:search", None, 1)


def test_domains_search_throws_forbidden_error() -> None:
    """Test Search endpoint error response (ForbiddenError) with WireMock"""
    test_id = "domains.search.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.domains.search(
            keyword="keyword",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains:search", None, 1)


def test_domains_search_throws_method_not_allowed_error() -> None:
    """Test Search endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "domains.search.4"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.domains.search(
            keyword="keyword",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains:search", None, 1)


def test_domains_search_throws_unsupported_media_type_error() -> None:
    """Test Search endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "domains.search.5"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.domains.search(
            keyword="keyword",
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domains:search", None, 1)


def test_domains_search_throws_too_many_requests_error() -> None:
    """Test Search endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "domains.search.6"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.domains.search(
            keyword="keyword",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains:search", None, 1)


def test_domains_search_throws_internal_server_error() -> None:
    """Test Search endpoint error response (InternalServerError) with WireMock"""
    test_id = "domains.search.7"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.domains.search(
            keyword="keyword",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains:search", None, 1)


def test_domains_search_throws_bad_gateway_error() -> None:
    """Test Search endpoint error response (BadGatewayError) with WireMock"""
    test_id = "domains.search.8"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.domains.search(
            keyword="keyword",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains:search", None, 1)


def test_domains_search_throws_service_unavailable_error() -> None:
    """Test Search endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "domains.search.9"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.domains.search(
            keyword="keyword",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains:search", None, 1)


def test_domains_search_throws_gateway_timeout_error() -> None:
    """Test Search endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "domains.search.10"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.domains.search(
            keyword="keyword",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domains:search", None, 1)


def test_domains_zone_check() -> None:
    """Test ZoneCheck endpoint with WireMock"""
    test_id = "domains.zone_check.0"
    client = get_client(test_id)
    client.domains.zone_check(
        domain_names=["example.com", "example.net", "example.org"],
    )
    verify_request_count(test_id, "POST", "/core/v1/zonecheck", None, 1)


def test_domains_zone_check_throws_bad_request_error() -> None:
    """Test ZoneCheck endpoint error response (BadRequestError) with WireMock"""
    test_id = "domains.zone_check.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.domains.zone_check(
            domain_names=["domainNames", "domainNames"],
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/zonecheck", None, 1)


def test_domains_zone_check_throws_unauthorized_error() -> None:
    """Test ZoneCheck endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "domains.zone_check.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.domains.zone_check(
            domain_names=["domainNames", "domainNames"],
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/zonecheck", None, 1)


def test_domains_zone_check_throws_forbidden_error() -> None:
    """Test ZoneCheck endpoint error response (ForbiddenError) with WireMock"""
    test_id = "domains.zone_check.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.domains.zone_check(
            domain_names=["domainNames", "domainNames"],
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/zonecheck", None, 1)


def test_domains_zone_check_throws_method_not_allowed_error() -> None:
    """Test ZoneCheck endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "domains.zone_check.4"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.domains.zone_check(
            domain_names=["domainNames", "domainNames"],
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/zonecheck", None, 1)


def test_domains_zone_check_throws_unsupported_media_type_error() -> None:
    """Test ZoneCheck endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "domains.zone_check.5"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.domains.zone_check(
            domain_names=["domainNames", "domainNames"],
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/zonecheck", None, 1)


def test_domains_zone_check_throws_unprocessable_entity_error() -> None:
    """Test ZoneCheck endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "domains.zone_check.6"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.domains.zone_check(
            domain_names=["domainNames", "domainNames"],
        )
    assert exc_info.value.status_code == 422
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/zonecheck", None, 1)


def test_domains_zone_check_throws_too_many_requests_error() -> None:
    """Test ZoneCheck endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "domains.zone_check.7"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.domains.zone_check(
            domain_names=["domainNames", "domainNames"],
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/zonecheck", None, 1)


def test_domains_zone_check_throws_internal_server_error() -> None:
    """Test ZoneCheck endpoint error response (InternalServerError) with WireMock"""
    test_id = "domains.zone_check.8"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.domains.zone_check(
            domain_names=["domainNames", "domainNames"],
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/zonecheck", None, 1)


def test_domains_zone_check_throws_bad_gateway_error() -> None:
    """Test ZoneCheck endpoint error response (BadGatewayError) with WireMock"""
    test_id = "domains.zone_check.9"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.domains.zone_check(
            domain_names=["domainNames", "domainNames"],
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/zonecheck", None, 1)


def test_domains_zone_check_throws_service_unavailable_error() -> None:
    """Test ZoneCheck endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "domains.zone_check.10"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.domains.zone_check(
            domain_names=["domainNames", "domainNames"],
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/zonecheck", None, 1)


def test_domains_zone_check_throws_gateway_timeout_error() -> None:
    """Test ZoneCheck endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "domains.zone_check.11"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.domains.zone_check(
            domain_names=["domainNames", "domainNames"],
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/zonecheck", None, 1)

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
    UnprocessableEntityError,
    UnsupportedMediaTypeError,
)
from namecom_core_api.core.jsonable_encoder import jsonable_encoder


def test_domainInfo_get_requirement() -> None:
    """Test GetRequirement endpoint with WireMock"""
    test_id = "domain_info.get_requirement.0"
    client = get_client(test_id)
    client.domain_info.get_requirement(
        tld="fr",
    )
    verify_request_count(test_id, "GET", "/core/v1/domaininfo/requirements/fr", None, 1)


def test_domainInfo_get_requirement_simple_acknowledgement_requirement() -> None:
    """Test GetRequirement endpoint (Simple acknowledgement requirement example) with WireMock"""
    test_id = "domain_info.get_requirement.1"
    client = get_client(test_id)
    client.domain_info.get_requirement(
        tld="fr",
    )
    verify_request_count(test_id, "GET", "/core/v1/domaininfo/requirements/fr", None, 1)


def test_domainInfo_get_requirement_simple_notification_requirement() -> None:
    """Test GetRequirement endpoint (Simple notification requirement example) with WireMock"""
    test_id = "domain_info.get_requirement.2"
    client = get_client(test_id)
    client.domain_info.get_requirement(
        tld="fr",
    )
    verify_request_count(test_id, "GET", "/core/v1/domaininfo/requirements/fr", None, 1)


def test_domainInfo_get_requirement_throws_bad_request_error() -> None:
    """Test GetRequirement endpoint error response (BadRequestError) with WireMock"""
    test_id = "domain_info.get_requirement.3"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.domain_info.get_requirement(
            tld="tld",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domaininfo/requirements/tld", None, 1)


def test_domainInfo_get_requirement_throws_unauthorized_error() -> None:
    """Test GetRequirement endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "domain_info.get_requirement.4"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.domain_info.get_requirement(
            tld="tld",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domaininfo/requirements/tld", None, 1)


def test_domainInfo_get_requirement_throws_forbidden_error() -> None:
    """Test GetRequirement endpoint error response (ForbiddenError) with WireMock"""
    test_id = "domain_info.get_requirement.5"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.domain_info.get_requirement(
            tld="tld",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domaininfo/requirements/tld", None, 1)


def test_domainInfo_get_requirement_throws_not_found_error() -> None:
    """Test GetRequirement endpoint error response (NotFoundError) with WireMock"""
    test_id = "domain_info.get_requirement.6"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.domain_info.get_requirement(
            tld="tld",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "GET", "/core/v1/domaininfo/requirements/tld", None, 1)


def test_domainInfo_get_requirement_throws_method_not_allowed_error() -> None:
    """Test GetRequirement endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "domain_info.get_requirement.7"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.domain_info.get_requirement(
            tld="tld",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domaininfo/requirements/tld", None, 1)


def test_domainInfo_get_requirement_throws_unprocessable_entity_error() -> None:
    """Test GetRequirement endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "domain_info.get_requirement.8"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.domain_info.get_requirement(
            tld="tld",
        )
    assert exc_info.value.status_code == 422
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "GET", "/core/v1/domaininfo/requirements/tld", None, 1)


def test_domainInfo_get_requirement_throws_too_many_requests_error() -> None:
    """Test GetRequirement endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "domain_info.get_requirement.9"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.domain_info.get_requirement(
            tld="tld",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domaininfo/requirements/tld", None, 1)


def test_domainInfo_get_requirement_throws_internal_server_error() -> None:
    """Test GetRequirement endpoint error response (InternalServerError) with WireMock"""
    test_id = "domain_info.get_requirement.10"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.domain_info.get_requirement(
            tld="tld",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domaininfo/requirements/tld", None, 1)


def test_domainInfo_get_requirement_throws_bad_gateway_error() -> None:
    """Test GetRequirement endpoint error response (BadGatewayError) with WireMock"""
    test_id = "domain_info.get_requirement.11"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.domain_info.get_requirement(
            tld="tld",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domaininfo/requirements/tld", None, 1)


def test_domainInfo_get_requirement_throws_service_unavailable_error() -> None:
    """Test GetRequirement endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "domain_info.get_requirement.12"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.domain_info.get_requirement(
            tld="tld",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domaininfo/requirements/tld", None, 1)


def test_domainInfo_get_requirement_throws_gateway_timeout_error() -> None:
    """Test GetRequirement endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "domain_info.get_requirement.13"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.domain_info.get_requirement(
            tld="tld",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domaininfo/requirements/tld", None, 1)


def test_domainInfo_check_domain_claims() -> None:
    """Test CheckDomainClaims endpoint with WireMock"""
    test_id = "domain_info.check_domain_claims.0"
    client = get_client(test_id)
    client.domain_info.check_domain_claims(
        domain="tiktok.page",
    )
    verify_request_count(test_id, "POST", "/core/v1/domaininfo/claims/tiktok.page", None, 1)


def test_domainInfo_check_domain_claims_domain_without_trademark_claims() -> None:
    """Test CheckDomainClaims endpoint (Domain without trademark claims example) with WireMock"""
    test_id = "domain_info.check_domain_claims.1"
    client = get_client(test_id)
    client.domain_info.check_domain_claims(
        domain="tiktok.page",
    )
    verify_request_count(test_id, "POST", "/core/v1/domaininfo/claims/tiktok.page", None, 1)


def test_domainInfo_check_domain_claims_throws_bad_request_error() -> None:
    """Test CheckDomainClaims endpoint error response (BadRequestError) with WireMock"""
    test_id = "domain_info.check_domain_claims.2"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.domain_info.check_domain_claims(
            domain="domain",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domaininfo/claims/domain", None, 1)


def test_domainInfo_check_domain_claims_throws_unauthorized_error() -> None:
    """Test CheckDomainClaims endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "domain_info.check_domain_claims.3"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.domain_info.check_domain_claims(
            domain="domain",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domaininfo/claims/domain", None, 1)


def test_domainInfo_check_domain_claims_throws_forbidden_error() -> None:
    """Test CheckDomainClaims endpoint error response (ForbiddenError) with WireMock"""
    test_id = "domain_info.check_domain_claims.4"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.domain_info.check_domain_claims(
            domain="domain",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domaininfo/claims/domain", None, 1)


def test_domainInfo_check_domain_claims_throws_not_found_error() -> None:
    """Test CheckDomainClaims endpoint error response (NotFoundError) with WireMock"""
    test_id = "domain_info.check_domain_claims.5"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.domain_info.check_domain_claims(
            domain="domain",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domaininfo/claims/domain", None, 1)


def test_domainInfo_check_domain_claims_throws_method_not_allowed_error() -> None:
    """Test CheckDomainClaims endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "domain_info.check_domain_claims.6"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.domain_info.check_domain_claims(
            domain="domain",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domaininfo/claims/domain", None, 1)


def test_domainInfo_check_domain_claims_throws_unsupported_media_type_error() -> None:
    """Test CheckDomainClaims endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "domain_info.check_domain_claims.7"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.domain_info.check_domain_claims(
            domain="domain",
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/domaininfo/claims/domain", None, 1)


def test_domainInfo_check_domain_claims_throws_too_many_requests_error() -> None:
    """Test CheckDomainClaims endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "domain_info.check_domain_claims.8"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.domain_info.check_domain_claims(
            domain="domain",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domaininfo/claims/domain", None, 1)


def test_domainInfo_check_domain_claims_throws_internal_server_error() -> None:
    """Test CheckDomainClaims endpoint error response (InternalServerError) with WireMock"""
    test_id = "domain_info.check_domain_claims.9"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.domain_info.check_domain_claims(
            domain="domain",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domaininfo/claims/domain", None, 1)


def test_domainInfo_check_domain_claims_throws_bad_gateway_error() -> None:
    """Test CheckDomainClaims endpoint error response (BadGatewayError) with WireMock"""
    test_id = "domain_info.check_domain_claims.10"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.domain_info.check_domain_claims(
            domain="domain",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domaininfo/claims/domain", None, 1)


def test_domainInfo_check_domain_claims_throws_service_unavailable_error() -> None:
    """Test CheckDomainClaims endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "domain_info.check_domain_claims.11"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.domain_info.check_domain_claims(
            domain="domain",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domaininfo/claims/domain", None, 1)


def test_domainInfo_check_domain_claims_throws_gateway_timeout_error() -> None:
    """Test CheckDomainClaims endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "domain_info.check_domain_claims.12"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.domain_info.check_domain_claims(
            domain="domain",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/domaininfo/claims/domain", None, 1)


def test_domainInfo_get_tld_requirements_v2() -> None:
    """Test GetTldRequirementsV2 endpoint with WireMock"""
    test_id = "domain_info.get_tld_requirements_v2.0"
    client = get_client(test_id)
    client.domain_info.get_tld_requirements_v2(
        tld="fr",
    )
    verify_request_count(test_id, "GET", "/core/v1/domaininfo/requirementsV2/fr", None, 1)


def test_domainInfo_get_tld_requirements_v2_throws_bad_request_error() -> None:
    """Test GetTldRequirementsV2 endpoint error response (BadRequestError) with WireMock"""
    test_id = "domain_info.get_tld_requirements_v2.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.domain_info.get_tld_requirements_v2(
            tld="tld",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domaininfo/requirementsV2/tld", None, 1)


def test_domainInfo_get_tld_requirements_v2_throws_unauthorized_error() -> None:
    """Test GetTldRequirementsV2 endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "domain_info.get_tld_requirements_v2.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.domain_info.get_tld_requirements_v2(
            tld="tld",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domaininfo/requirementsV2/tld", None, 1)


def test_domainInfo_get_tld_requirements_v2_throws_forbidden_error() -> None:
    """Test GetTldRequirementsV2 endpoint error response (ForbiddenError) with WireMock"""
    test_id = "domain_info.get_tld_requirements_v2.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.domain_info.get_tld_requirements_v2(
            tld="tld",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domaininfo/requirementsV2/tld", None, 1)


def test_domainInfo_get_tld_requirements_v2_throws_not_found_error() -> None:
    """Test GetTldRequirementsV2 endpoint error response (NotFoundError) with WireMock"""
    test_id = "domain_info.get_tld_requirements_v2.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.domain_info.get_tld_requirements_v2(
            tld="tld",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "GET", "/core/v1/domaininfo/requirementsV2/tld", None, 1)


def test_domainInfo_get_tld_requirements_v2_throws_method_not_allowed_error() -> None:
    """Test GetTldRequirementsV2 endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "domain_info.get_tld_requirements_v2.5"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.domain_info.get_tld_requirements_v2(
            tld="tld",
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domaininfo/requirementsV2/tld", None, 1)


def test_domainInfo_get_tld_requirements_v2_throws_unprocessable_entity_error() -> None:
    """Test GetTldRequirementsV2 endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "domain_info.get_tld_requirements_v2.6"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.domain_info.get_tld_requirements_v2(
            tld="tld",
        )
    assert exc_info.value.status_code == 422
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "GET", "/core/v1/domaininfo/requirementsV2/tld", None, 1)


def test_domainInfo_get_tld_requirements_v2_throws_too_many_requests_error() -> None:
    """Test GetTldRequirementsV2 endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "domain_info.get_tld_requirements_v2.7"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.domain_info.get_tld_requirements_v2(
            tld="tld",
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domaininfo/requirementsV2/tld", None, 1)


def test_domainInfo_get_tld_requirements_v2_throws_internal_server_error() -> None:
    """Test GetTldRequirementsV2 endpoint error response (InternalServerError) with WireMock"""
    test_id = "domain_info.get_tld_requirements_v2.8"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.domain_info.get_tld_requirements_v2(
            tld="tld",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domaininfo/requirementsV2/tld", None, 1)


def test_domainInfo_get_tld_requirements_v2_throws_bad_gateway_error() -> None:
    """Test GetTldRequirementsV2 endpoint error response (BadGatewayError) with WireMock"""
    test_id = "domain_info.get_tld_requirements_v2.9"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.domain_info.get_tld_requirements_v2(
            tld="tld",
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domaininfo/requirementsV2/tld", None, 1)


def test_domainInfo_get_tld_requirements_v2_throws_service_unavailable_error() -> None:
    """Test GetTldRequirementsV2 endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "domain_info.get_tld_requirements_v2.10"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.domain_info.get_tld_requirements_v2(
            tld="tld",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domaininfo/requirementsV2/tld", None, 1)


def test_domainInfo_get_tld_requirements_v2_throws_gateway_timeout_error() -> None:
    """Test GetTldRequirementsV2 endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "domain_info.get_tld_requirements_v2.11"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.domain_info.get_tld_requirements_v2(
            tld="tld",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/domaininfo/requirementsV2/tld", None, 1)

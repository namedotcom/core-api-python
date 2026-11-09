import pytest
from .conftest import get_client, verify_request_count

from namecom_core_api import (
    BadGatewayError,
    BadRequestError,
    ConflictError,
    ForbiddenError,
    GatewayTimeoutError,
    InternalServerError,
    MethodNotAllowedError,
    NotFoundError,
    ServiceUnavailableError,
    TooManyRequestsError,
    UnauthorizedError,
    UnsupportedMediaTypeError,
)
from namecom_core_api.core.jsonable_encoder import jsonable_encoder


def test_webhookNotifications_get_subscribed_notifications() -> None:
    """Test GetSubscribedNotifications endpoint with WireMock"""
    test_id = "webhook_notifications.get_subscribed_notifications.0"
    client = get_client(test_id)
    client.webhook_notifications.get_subscribed_notifications()
    verify_request_count(test_id, "GET", "/core/v1/notifications", None, 1)


def test_webhookNotifications_get_subscribed_notifications_throws_unauthorized_error() -> None:
    """Test GetSubscribedNotifications endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "webhook_notifications.get_subscribed_notifications.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.webhook_notifications.get_subscribed_notifications()
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/notifications", None, 1)


def test_webhookNotifications_get_subscribed_notifications_throws_forbidden_error() -> None:
    """Test GetSubscribedNotifications endpoint error response (ForbiddenError) with WireMock"""
    test_id = "webhook_notifications.get_subscribed_notifications.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.webhook_notifications.get_subscribed_notifications()
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/notifications", None, 1)


def test_webhookNotifications_get_subscribed_notifications_throws_method_not_allowed_error() -> None:
    """Test GetSubscribedNotifications endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "webhook_notifications.get_subscribed_notifications.3"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.webhook_notifications.get_subscribed_notifications()
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/notifications", None, 1)


def test_webhookNotifications_get_subscribed_notifications_throws_too_many_requests_error() -> None:
    """Test GetSubscribedNotifications endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "webhook_notifications.get_subscribed_notifications.4"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.webhook_notifications.get_subscribed_notifications()
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/notifications", None, 1)


def test_webhookNotifications_get_subscribed_notifications_throws_internal_server_error() -> None:
    """Test GetSubscribedNotifications endpoint error response (InternalServerError) with WireMock"""
    test_id = "webhook_notifications.get_subscribed_notifications.5"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.webhook_notifications.get_subscribed_notifications()
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/notifications", None, 1)


def test_webhookNotifications_get_subscribed_notifications_throws_bad_gateway_error() -> None:
    """Test GetSubscribedNotifications endpoint error response (BadGatewayError) with WireMock"""
    test_id = "webhook_notifications.get_subscribed_notifications.6"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.webhook_notifications.get_subscribed_notifications()
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/notifications", None, 1)


def test_webhookNotifications_get_subscribed_notifications_throws_service_unavailable_error() -> None:
    """Test GetSubscribedNotifications endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "webhook_notifications.get_subscribed_notifications.7"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.webhook_notifications.get_subscribed_notifications()
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/notifications", None, 1)


def test_webhookNotifications_get_subscribed_notifications_throws_gateway_timeout_error() -> None:
    """Test GetSubscribedNotifications endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "webhook_notifications.get_subscribed_notifications.8"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.webhook_notifications.get_subscribed_notifications()
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/core/v1/notifications", None, 1)


def test_webhookNotifications_subscribe_to_notification() -> None:
    """Test SubscribeToNotification endpoint with WireMock"""
    test_id = "webhook_notifications.subscribe_to_notification.0"
    client = get_client(test_id)
    client.webhook_notifications.subscribe_to_notification(
        event_name="account.credit.balance_change",
        url="https://example.com",
        active=True,
    )
    verify_request_count(test_id, "POST", "/core/v1/notifications", None, 1)


def test_webhookNotifications_subscribe_to_notification_throws_bad_request_error() -> None:
    """Test SubscribeToNotification endpoint error response (BadRequestError) with WireMock"""
    test_id = "webhook_notifications.subscribe_to_notification.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.webhook_notifications.subscribe_to_notification(
            event_name="account.credit.balance_change",
            url="url",
            active=True,
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/notifications", None, 1)


def test_webhookNotifications_subscribe_to_notification_throws_unauthorized_error() -> None:
    """Test SubscribeToNotification endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "webhook_notifications.subscribe_to_notification.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.webhook_notifications.subscribe_to_notification(
            event_name="account.credit.balance_change",
            url="url",
            active=True,
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/notifications", None, 1)


def test_webhookNotifications_subscribe_to_notification_throws_forbidden_error() -> None:
    """Test SubscribeToNotification endpoint error response (ForbiddenError) with WireMock"""
    test_id = "webhook_notifications.subscribe_to_notification.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.webhook_notifications.subscribe_to_notification(
            event_name="account.credit.balance_change",
            url="url",
            active=True,
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/notifications", None, 1)


def test_webhookNotifications_subscribe_to_notification_throws_method_not_allowed_error() -> None:
    """Test SubscribeToNotification endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "webhook_notifications.subscribe_to_notification.4"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.webhook_notifications.subscribe_to_notification(
            event_name="account.credit.balance_change",
            url="url",
            active=True,
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/notifications", None, 1)


def test_webhookNotifications_subscribe_to_notification_throws_conflict_error() -> None:
    """Test SubscribeToNotification endpoint error response (ConflictError) with WireMock"""
    test_id = "webhook_notifications.subscribe_to_notification.5"
    client = get_client(test_id)
    with pytest.raises(ConflictError) as exc_info:
        client.webhook_notifications.subscribe_to_notification(
            event_name="account.credit.balance_change",
            url="url",
            active=True,
        )
    assert exc_info.value.status_code == 409
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/notifications", None, 1)


def test_webhookNotifications_subscribe_to_notification_throws_unsupported_media_type_error() -> None:
    """Test SubscribeToNotification endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "webhook_notifications.subscribe_to_notification.6"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.webhook_notifications.subscribe_to_notification(
            event_name="account.credit.balance_change",
            url="url",
            active=True,
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "POST", "/core/v1/notifications", None, 1)


def test_webhookNotifications_subscribe_to_notification_throws_too_many_requests_error() -> None:
    """Test SubscribeToNotification endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "webhook_notifications.subscribe_to_notification.7"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.webhook_notifications.subscribe_to_notification(
            event_name="account.credit.balance_change",
            url="url",
            active=True,
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/notifications", None, 1)


def test_webhookNotifications_subscribe_to_notification_throws_internal_server_error() -> None:
    """Test SubscribeToNotification endpoint error response (InternalServerError) with WireMock"""
    test_id = "webhook_notifications.subscribe_to_notification.8"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.webhook_notifications.subscribe_to_notification(
            event_name="account.credit.balance_change",
            url="url",
            active=True,
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/notifications", None, 1)


def test_webhookNotifications_subscribe_to_notification_throws_bad_gateway_error() -> None:
    """Test SubscribeToNotification endpoint error response (BadGatewayError) with WireMock"""
    test_id = "webhook_notifications.subscribe_to_notification.9"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.webhook_notifications.subscribe_to_notification(
            event_name="account.credit.balance_change",
            url="url",
            active=True,
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/notifications", None, 1)


def test_webhookNotifications_subscribe_to_notification_throws_service_unavailable_error() -> None:
    """Test SubscribeToNotification endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "webhook_notifications.subscribe_to_notification.10"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.webhook_notifications.subscribe_to_notification(
            event_name="account.credit.balance_change",
            url="url",
            active=True,
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/notifications", None, 1)


def test_webhookNotifications_subscribe_to_notification_throws_gateway_timeout_error() -> None:
    """Test SubscribeToNotification endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "webhook_notifications.subscribe_to_notification.11"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.webhook_notifications.subscribe_to_notification(
            event_name="account.credit.balance_change",
            url="url",
            active=True,
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/core/v1/notifications", None, 1)


def test_webhookNotifications_modify_subscription() -> None:
    """Test ModifySubscription endpoint with WireMock"""
    test_id = "webhook_notifications.modify_subscription.0"
    client = get_client(test_id)
    client.webhook_notifications.modify_subscription(
        id=1,
    )
    verify_request_count(test_id, "PUT", "/core/v1/notifications/1", None, 1)


def test_webhookNotifications_modify_subscription_throws_unauthorized_error() -> None:
    """Test ModifySubscription endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "webhook_notifications.modify_subscription.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.webhook_notifications.modify_subscription(
            id=1,
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/notifications/1", None, 1)


def test_webhookNotifications_modify_subscription_throws_forbidden_error() -> None:
    """Test ModifySubscription endpoint error response (ForbiddenError) with WireMock"""
    test_id = "webhook_notifications.modify_subscription.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.webhook_notifications.modify_subscription(
            id=1,
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/notifications/1", None, 1)


def test_webhookNotifications_modify_subscription_throws_not_found_error() -> None:
    """Test ModifySubscription endpoint error response (NotFoundError) with WireMock"""
    test_id = "webhook_notifications.modify_subscription.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.webhook_notifications.modify_subscription(
            id=1,
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "PUT", "/core/v1/notifications/1", None, 1)


def test_webhookNotifications_modify_subscription_throws_method_not_allowed_error() -> None:
    """Test ModifySubscription endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "webhook_notifications.modify_subscription.4"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.webhook_notifications.modify_subscription(
            id=1,
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/notifications/1", None, 1)


def test_webhookNotifications_modify_subscription_throws_unsupported_media_type_error() -> None:
    """Test ModifySubscription endpoint error response (UnsupportedMediaTypeError) with WireMock"""
    test_id = "webhook_notifications.modify_subscription.5"
    client = get_client(test_id)
    with pytest.raises(UnsupportedMediaTypeError) as exc_info:
        client.webhook_notifications.modify_subscription(
            id=1,
        )
    assert exc_info.value.status_code == 415
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "PUT", "/core/v1/notifications/1", None, 1)


def test_webhookNotifications_modify_subscription_throws_too_many_requests_error() -> None:
    """Test ModifySubscription endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "webhook_notifications.modify_subscription.6"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.webhook_notifications.modify_subscription(
            id=1,
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/notifications/1", None, 1)


def test_webhookNotifications_modify_subscription_throws_internal_server_error() -> None:
    """Test ModifySubscription endpoint error response (InternalServerError) with WireMock"""
    test_id = "webhook_notifications.modify_subscription.7"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.webhook_notifications.modify_subscription(
            id=1,
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/notifications/1", None, 1)


def test_webhookNotifications_modify_subscription_throws_bad_gateway_error() -> None:
    """Test ModifySubscription endpoint error response (BadGatewayError) with WireMock"""
    test_id = "webhook_notifications.modify_subscription.8"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.webhook_notifications.modify_subscription(
            id=1,
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/notifications/1", None, 1)


def test_webhookNotifications_modify_subscription_throws_service_unavailable_error() -> None:
    """Test ModifySubscription endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "webhook_notifications.modify_subscription.9"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.webhook_notifications.modify_subscription(
            id=1,
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/notifications/1", None, 1)


def test_webhookNotifications_modify_subscription_throws_gateway_timeout_error() -> None:
    """Test ModifySubscription endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "webhook_notifications.modify_subscription.10"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.webhook_notifications.modify_subscription(
            id=1,
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/core/v1/notifications/1", None, 1)


def test_webhookNotifications_delete_subscription() -> None:
    """Test DeleteSubscription endpoint with WireMock"""
    test_id = "webhook_notifications.delete_subscription.0"
    client = get_client(test_id)
    client.webhook_notifications.delete_subscription(
        id=1,
    )
    verify_request_count(test_id, "DELETE", "/core/v1/notifications/1", None, 1)


def test_webhookNotifications_delete_subscription_throws_unauthorized_error() -> None:
    """Test DeleteSubscription endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "webhook_notifications.delete_subscription.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.webhook_notifications.delete_subscription(
            id=1,
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/notifications/1", None, 1)


def test_webhookNotifications_delete_subscription_throws_forbidden_error() -> None:
    """Test DeleteSubscription endpoint error response (ForbiddenError) with WireMock"""
    test_id = "webhook_notifications.delete_subscription.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.webhook_notifications.delete_subscription(
            id=1,
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/notifications/1", None, 1)


def test_webhookNotifications_delete_subscription_throws_not_found_error() -> None:
    """Test DeleteSubscription endpoint error response (NotFoundError) with WireMock"""
    test_id = "webhook_notifications.delete_subscription.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.webhook_notifications.delete_subscription(
            id=1,
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"message": "message"}
    verify_request_count(test_id, "DELETE", "/core/v1/notifications/1", None, 1)


def test_webhookNotifications_delete_subscription_throws_method_not_allowed_error() -> None:
    """Test DeleteSubscription endpoint error response (MethodNotAllowedError) with WireMock"""
    test_id = "webhook_notifications.delete_subscription.4"
    client = get_client(test_id)
    with pytest.raises(MethodNotAllowedError) as exc_info:
        client.webhook_notifications.delete_subscription(
            id=1,
        )
    assert exc_info.value.status_code == 405
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/notifications/1", None, 1)


def test_webhookNotifications_delete_subscription_throws_too_many_requests_error() -> None:
    """Test DeleteSubscription endpoint error response (TooManyRequestsError) with WireMock"""
    test_id = "webhook_notifications.delete_subscription.5"
    client = get_client(test_id)
    with pytest.raises(TooManyRequestsError) as exc_info:
        client.webhook_notifications.delete_subscription(
            id=1,
        )
    assert exc_info.value.status_code == 429
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/notifications/1", None, 1)


def test_webhookNotifications_delete_subscription_throws_internal_server_error() -> None:
    """Test DeleteSubscription endpoint error response (InternalServerError) with WireMock"""
    test_id = "webhook_notifications.delete_subscription.6"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.webhook_notifications.delete_subscription(
            id=1,
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/notifications/1", None, 1)


def test_webhookNotifications_delete_subscription_throws_bad_gateway_error() -> None:
    """Test DeleteSubscription endpoint error response (BadGatewayError) with WireMock"""
    test_id = "webhook_notifications.delete_subscription.7"
    client = get_client(test_id)
    with pytest.raises(BadGatewayError) as exc_info:
        client.webhook_notifications.delete_subscription(
            id=1,
        )
    assert exc_info.value.status_code == 502
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/notifications/1", None, 1)


def test_webhookNotifications_delete_subscription_throws_service_unavailable_error() -> None:
    """Test DeleteSubscription endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "webhook_notifications.delete_subscription.8"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.webhook_notifications.delete_subscription(
            id=1,
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/notifications/1", None, 1)


def test_webhookNotifications_delete_subscription_throws_gateway_timeout_error() -> None:
    """Test DeleteSubscription endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "webhook_notifications.delete_subscription.9"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.webhook_notifications.delete_subscription(
            id=1,
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/core/v1/notifications/1", None, 1)

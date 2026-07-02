from .conftest import get_client, verify_request_count

from namecom_core_api.webhook_notifications import ModifySubscriptionRequestBodyUrl


def test_webhookNotifications_get_subscribed_notifications() -> None:
    """Test GetSubscribedNotifications endpoint with WireMock"""
    test_id = "webhook_notifications.get_subscribed_notifications.0"
    client = get_client(test_id)
    client.webhook_notifications.get_subscribed_notifications()
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


def test_webhookNotifications_modify_subscription() -> None:
    """Test ModifySubscription endpoint with WireMock"""
    test_id = "webhook_notifications.modify_subscription.0"
    client = get_client(test_id)
    client.webhook_notifications.modify_subscription(
        id=1,
        request=ModifySubscriptionRequestBodyUrl(
            url="url",
        ),
    )
    verify_request_count(test_id, "PUT", "/core/v1/notifications/1", None, 1)


def test_webhookNotifications_delete_subscription() -> None:
    """Test DeleteSubscription endpoint with WireMock"""
    test_id = "webhook_notifications.delete_subscription.0"
    client = get_client(test_id)
    client.webhook_notifications.delete_subscription(
        id=1,
    )
    verify_request_count(test_id, "DELETE", "/core/v1/notifications/1", None, 1)

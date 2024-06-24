from schemas.config.pusher.pusher import send_notification_via_pusher
from schemas.config.smtp.smtp import send_email_via_smtplib
from models.notification_models import Notification

def send_custom_notification_func(notification: Notification):
    send_email_via_smtplib(notification.user_email, notification.subject, notification.message)
    send_notification_via_pusher('custom_channel', 'custom_notification', {'email': notification.user_email, 'subject': notification.subject, 'message': notification.message})
    return {"detail": "Notification sent successfully"}
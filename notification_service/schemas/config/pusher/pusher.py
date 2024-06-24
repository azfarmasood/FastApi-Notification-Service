from fastapi import HTTPException, status
from database.db import PUSHER_APP_ID, PUSHER_CLUSTER, PUSHER_KEY, PUSHER_SECRET_KEY
from pusher import Pusher # type: ignore
from pusher.errors import PusherError # type: ignore
import time

pusher_client: Pusher = Pusher(
    app_id = str(PUSHER_APP_ID),
    key = str(PUSHER_KEY),
    secret = str(PUSHER_SECRET_KEY),
    cluster = str(PUSHER_CLUSTER),
    ssl= True
)

def send_notification_via_pusher(channel: str, event: str, data: dict):
    retries = 3
    for attempt in range(retries):
        try:
            pusher_client.trigger(channel, event, data)
            print(f"Notification sent to channel {channel} with event {event}")
            break
        except (PusherError, ConnectionError) as error:
            if attempt < retries - 1:
                print(f"Retrying... ({attempt + 1}/{retries})")
                time.sleep(2)  # If The Connection Faild To Send Notification It Will Retries 2 times
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error))
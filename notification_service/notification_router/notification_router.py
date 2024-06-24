from typing import Annotated, Any
from fastapi import APIRouter, Depends, status
from notification_controller.custome_notification import send_custom_notification_func
from models.notification_models import Notificatin_Response_Model

router = APIRouter()

@router.post("/send_notifications/", response_model = Notificatin_Response_Model, status_code = status.HTTP_200_OK)
def send_custom_notification(response: Annotated[Any, Depends(send_custom_notification_func)]):
    return response
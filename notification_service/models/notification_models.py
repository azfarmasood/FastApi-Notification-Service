from sqlmodel import SQLModel

class Notification(SQLModel):
    user_email: str 
    subject: str
    message: str
    
class Notificatin_Response_Model(SQLModel):
    user_email: str = "Secret To Not Show User Email" 
    subject: str = "Any Thing"
    message: str = "Type Any Custome Notification"
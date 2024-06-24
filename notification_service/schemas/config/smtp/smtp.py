from smtplib import SMTP, SMTPException
from fastapi import HTTPException, status
from email.mime.text import MIMEText
from database.db import SMPTP_SERVER, SMTP_APP_PASSWORD, SMTP_PORT, DOMAIN_NAME

def send_email_via_smtplib(user_email: str, subject: str, message: str):
    try:
        msg = MIMEText(message)
        msg['From'] = DOMAIN_NAME
        msg['To'] = user_email
        msg['Subject'] = subject
        
        with SMTP(SMPTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(DOMAIN_NAME, SMTP_APP_PASSWORD)
            server.sendmail(DOMAIN_NAME, user_email, msg.as_string())
            server.quit()
            print(f"Email has been sent to {user_email}")
    except SMTPException as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = str(error))
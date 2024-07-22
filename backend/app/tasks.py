from .worker import app
import smtplib
from email.mime.text import MIMEText

@app.task
def send_email_task(email):
    msg = MIMEText("This is a test email.")
    msg["Subject"] = "Test Email"
    msg["From"] = "your_email@example.com"
    msg["To"] = email

    with smtplib.SMTP("smtp.example.com") as server:
        server.login("your_username", "your_password")
        server.sendmail("your_email@example.com", email, msg.as_string())

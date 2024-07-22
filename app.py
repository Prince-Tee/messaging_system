from flask import Flask, request
import logging
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from celery import Celery

app = Flask(__name__)

# Celery configuration
app.config['CELERY_BROKER_URL'] = 'amqp://localhost//'
app.config['CELERY_RESULT_BACKEND'] = 'rpc://'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task
def send_email(email):
    sender_email = "adebiyi1605@gmail.com"
    receiver_email = email
    password = "taiwogirl#"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Hello from Flask"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = """\
    Hi,
    This is a test email sent from a Flask application using Celery and RabbitMQ."""
    part = MIMEText(text, "plain")
    message.attach(part)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

@app.route('/')
def index():
    sendmail = request.args.get('sendmail')
    talktome = request.args.get('talktome')
    
    if sendmail:
        send_email.apply_async(args=[sendmail])
        return f"Email sent to {sendmail}!"

    if talktome:
        with open("/var/log/messaging_system.log", "a") as log_file:
            log_file.write(f"Current time: {datetime.now()}\n")
        return "Time logged."

    return "Welcome to the messaging system!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import Request
import smtplib
from celery import Celery
from datetime import datetime

app = FastAPI()

# Celery configuration
celery = Celery(
    __name__,
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

sender_email = "adeb@gmail.com"
password = "hhhhh"

@celery.task
def send_email_task(receiver_email: str):
    message = f"""\
    Subject: Hi there

    This message is sent from FastAPI application."""

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

@app.get("/sendmail")
async def sendmail(request: Request):
    receiver_email = request.query_params.get('sendmail')
    if receiver_email:
        send_email_task.delay(receiver_email)
        return JSONResponse(content={"message": "Email sent successfully!"})
    return JSONResponse(content={"error": "No email provided"}, status_code=400)

@app.get("/talktome")
async def talktome():
    log_message = f"Current time: {datetime.now()}\n"
    with open("/var/log/messaging_system.log", "a") as log_file:
        log_file.write(log_message)
    return JSONResponse(content={"message": "Logged successfully!"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)


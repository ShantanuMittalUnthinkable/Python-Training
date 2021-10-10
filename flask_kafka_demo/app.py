import os
import json

# import smtplib, ssl
# from concurrent.futures import ThreadPoolExecutor
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from kafka import KafkaConsumer, KafkaProducer

TOPIC_NAME = "email"
consumer = KafkaConsumer(
    TOPIC_NAME,
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
)
# smtp_server = "smtp.gmail.com"
# port = 587
sender_email = input("Enter sender email: ")
password = input("Enter sender email password: ")
# context = ssl.create_default_context()
# server = smtplib.SMTP(smtp_server, port)
# server.login(sender_email, password)


def sendEmail(data):

    # server.sendmail(
    #     sender_email,
    #     data["receiver_email"],
    #     """\
    #     Subject:{}
    #     Hi here is a reminder for you:
    #     {}
    #     Scheduled at: {}
    # """.format(
    #         data["heading"], data["body"], data["scheduled_at"]
    #     ),
    # )

    message = Mail(
        from_email=sender_email,
        to_emails=data["receiver_email"]
        if "receiver_email" in data
        else "shantanumittal1997@gmail.com",
        subject="Reminder for event at {}".format(data["scheduled_at"]),
        html_content=f"<p>Here is the reminder you set for {data['scheduled_at']}</p>\
            <p><strong>{data['heading']}</strong></p>\
            <p>{data['body']}</p>",
    )
    try:
        sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)


for email in consumer:

    email_data = email.value
    print(email_data)

    sendEmail(email_data)

import smtplib
from email.mime.text import MIMEText
from time import sleep

from celery import shared_task
from django.conf import settings


@shared_task()
def send_email(email_address):
    print('send_email called')
    sleep(5)  # Simulate expensive operation(s) that freeze Django
    print(f'Sending email to: {email_address}')
    me = settings.EMAIL_USERNAME
    password = settings.EMAIL_PASSWORD
    you = email_address

    email_body = """
    <html><body><p>Hello World</p>
    </body></html>
    """

    message = MIMEText(email_body, 'html')

    message['Subject'] = f'New email!'
    message['From'] = me
    message['To'] = you
    try:
        print('Trying to send an email')
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(me, password)
        server.sendmail(me, you, message.as_string())
        server.quit()
        print(f'Email sent: {email_body}')
    except Exception as e:
        print(f'Error in sending email: {e}')

from django.conf import settings
from django.core.mail import send_mail, EmailMessage

def send_email_with_attachment(data):
    email = EmailMessage('Student Report Card', 'Hi Student, Please find your attached Report card herewith.', settings.EMAIL_HOST_USER, 
        [data['email']])
    data['file'].seek(0)
    email.attach(data['report'], data['file'].read())
    email.send()
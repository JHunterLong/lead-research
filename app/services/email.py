import smtplib
from email.mime.text import MIMEText

def send_email(to, subject, body):
    sender_email = "your_email@example.com"
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to

    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login(sender_email, "your_password")
        server.send_message(msg)

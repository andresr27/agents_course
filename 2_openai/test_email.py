import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv(override=True)

def send_html_email(subject: str, html_body: str):
    """Send an HTML email using Gmail SMTP and your Google App Password."""
    sender_email = os.environ.get("GMAIL_USER")  # e.g. yourname@gmail.com
    sender_password = os.environ.get("GMAIL_APP_PASSWORD") # 16-character app password
    receiver_email = "andresrenaud@gmail.com"
    print("Sending email...")
    if not sender_email or not sender_password:
        return {"status": "error", "message": "GMAIL_USER or GMAIL_APP_PASSWORD not set"}

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email
    message.attach(MIMEText(html_body, "html"))


    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent.")
        return {"status": "success"}
    except Exception as e:
        print(f"Email failed: {e}")
        return {"status": "error", "message": str(e)}


subject = "Test Email from Colab"
html = """
    <html>
      <body>
        <h1 style='color: #4A90E2;'>Hello from ComplAI!</h1>
        <p>This is a <b>simple HTML test</b> to verify your SMTP settings.</p>
        <hr>
        <p style='font-size: 12px; color: gray;'>Sent via Python smtplib</p>
      </body>
    </html>
    """


if __name__ == "__main__":
    print (send_html_email(subject=subject, html_body=html))
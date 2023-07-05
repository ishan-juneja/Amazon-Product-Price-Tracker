import smtplib
from email.message import EmailMessage
import os


class Notifier:
    def notify(self, product_name, product_price, product_link):
        # set your email and password
        # please use App Password
        email_address = os.environ.get("MY_EMAIL")
        email_password = os.environ.get("MY_EMAIL_PASSWORD")
        # create email
        msg = EmailMessage()
        msg['Subject'] = f"Price Drop Alert"
        msg['From'] = email_address
        msg['To'] = "ishanj101@gmail.com"
        msg.set_content(f"Hello!\nWe noticed a major price drop for {product_name} and its now priced at $"
                        f"{product_price}. The link to cop it is at {product_link}")

        # send email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)

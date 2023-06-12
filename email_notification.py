import smtplib

# Change the following email credentials with your own
MY_EMAIL = "mail@domain.com"
MY_PASSWORD = "app-password"


def send_email(msg):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=msg
        )

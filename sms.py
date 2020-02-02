from twilio.rest import Client
import config

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure

def message(body):
    account_sid = config.TWILIO_SSID
    auth_token = config.TWILIO_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=body,
            from_= config.FROM,
            to= config.TO
        )

    return message.sid
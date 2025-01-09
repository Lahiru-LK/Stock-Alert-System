# notifier.py
from twilio.rest import Client
from config import ACCOUNT_SID, AUTH_TOKEN, TWILIO_PHONE_NUMBER, YOUR_PHONE_NUMBER

# Function to send SMS notification
def send_sms(message):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    try:
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=YOUR_PHONE_NUMBER
        )
        print("SMS sent successfully!")
    except Exception as e:
        print(f"Error sending SMS: {e}")

# scheduler.py
import schedule
import time
from stock_checker import check_stocks
from notifier import send_sms
import logging

# Set up logging
logging.basicConfig(filename='stock_alert.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Function to check stocks and send notification
def check_and_notify():
    message = check_stocks()
    if message:
        print(f"Notification message:\n{message}")
        send_sms(message)
        logging.info("Stock alert sent successfully.")
    else:
        logging.info("No stocks to alert.")

# Schedule the function to run every 1 minute
schedule.every(1).minutes.do(check_and_notify)

# Keep the script running to handle scheduled tasks
print("Starting stock alert automation every 1 minute...")
while True:
    schedule.run_pending()
    time.sleep(1)

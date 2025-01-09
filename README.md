# 📈 Stock Alert System

This project is a simple Stock Alert System that checks the current prices of stocks from an Excel file and sends notifications if any stock's current price falls below its target price. Notifications are sent via SMS using Twilio.

## ✨ Features
- 📊 Automatically checks stock prices every hour (1 minutes).
- 📲 Sends SMS alerts for stocks below their target price.
- 📝 Logs all alerts and errors to a log file.
- 🔔 Uses Twilio for SMS notifications.

---

## 🗂️ Project Structure
```
stock-alert/
|-- .venv/                # Virtual environment (optional, not included)
|-- config.py             # Configuration file for sensitive data like API keys and phone numbers
|-- notifier.py           # Contains the function to send SMS notifications
|-- scheduler.py          # Main script to schedule and run the stock checks
|-- stock_alert.log       # Log file to store alerts and errors
|-- stock_checker.py      # Script to check stock prices against target prices
|-- stocks.xlsx           # Excel file containing stock data
|-- README.md             # Project documentation
```

---

## 📋 Requirements
### Prerequisites
1. **Python 3.7+** must be installed.
2. Install the required Python libraries:
   ```bash
   pip install pandas schedule twilio openpyxl
   ```
3. A Twilio account with an active phone number to send SMS notifications.

---

## ⚙️ Setup

1. Clone the repository or copy the project files to your local machine.
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Update the `config.py` file with your Twilio credentials and phone numbers:
   ```python
   ACCOUNT_SID = "<Your Twilio Account SID>"
   AUTH_TOKEN = "<Your Twilio Auth Token>"
   TWILIO_PHONE_NUMBER = "<Your Twilio Phone Number>"
   YOUR_PHONE_NUMBER = "<Your Personal Phone Number>"
   EXCEL_FILE_PATH = "stocks.xlsx"  # Path to your Excel file
   ```
5. Ensure your `stocks.xlsx` file follows this format:

   | Stock   | Current Price | Target Price |
   |---------|---------------|--------------|
   | OKTA    | 320.45        | 250.75       |
   | AMAZON  | 220.34        | 150.50       |
   | META    | 446.78        | 480.50       |
   | GOOGLE  | 195.23        | 180.00       |
   | AIRBNB  | 15.45         | 100.00       |
   | TWILIO  | 41.78         | 40.00        |

---

## 🚀 Usage
1. Run the scheduler script to start the stock alert system:
   ```bash
   python scheduler.py
   ```
2. The system will:
   - 🕒 Check stock prices every hour.
   - 📩 Send SMS notifications for stocks below their target price.
   - 📂 Log activities in `stock_alert.log`.

---

## 🗒️ Logs
All logs are stored in the `stock_alert.log` file. Logs include:
- ✅ Notifications sent.
- ⚠️ Errors encountered (e.g., issues reading the Excel file).

---

## 🛠️ Customization
### Changing the Check Interval
To change the frequency of stock price checks, modify the interval in `scheduler.py`:
```python
schedule.every(1).minutes.do(check_and_notify)
```
Replace `1` with your desired interval in minutes.

### Adding More Notifications
To add more notification methods (e.g., email, WhatsApp), update `notifier.py` with the relevant API integrations.

---

## 🐛 Troubleshooting
1. **Twilio errors**: Ensure your `ACCOUNT_SID`, `AUTH_TOKEN`, and phone numbers are correct in `config.py`.
2. **Excel file issues**: Ensure the `stocks.xlsx` file exists and has the required columns: `Stock`, `Current Price`, `Target Price`.
3. **No SMS received**: Check the Twilio dashboard for errors or limits on your account.

---

## 📜 License
This project is licensed under the MIT License.

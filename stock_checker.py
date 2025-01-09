# stock_checker.py
import pandas as pd
from config import EXCEL_FILE_PATH

# Function to check stocks
def check_stocks():
    print("Checking stocks...")  # For debugging/logging

    try:
        # Read the Excel file
        data = pd.read_excel(EXCEL_FILE_PATH)
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None

    # Ensure required columns exist
    if not {"Stock", "Current Price", "Target Price"}.issubset(data.columns):
        print("Error: Required columns (Stock, Current Price, Target Price) are missing in the Excel file.")
        return None

    # Filter stocks where the current price is below the target price
    filtered_stocks = data[data["Current Price"] < data["Target Price"]]

    if filtered_stocks.empty:
        print("No stocks below the target price.")
        return None

    # Prepare the message for stocks below target price
    message = "Stocks below target price:\n\n"
    for _, row in filtered_stocks.iterrows():
        stock = row["Stock"]
        current_price = row["Current Price"]
        target_price = row["Target Price"]
        message += f"{stock}: Current Price = {current_price:.2f}, Target Price = {target_price:.2f}\n"

    return message

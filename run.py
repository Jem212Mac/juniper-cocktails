import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('juniper_cocktails')

print("Welcome to Juniper Cocktails Customer Feedback Application.")
print("Please use this application to input or amend feedback, on behalf of the customer, from a completed feedback form, or to analyse existing customer feedback.\n")
print("Please choose from one of the following options:\n")

print("1. Input Customer Feedback.")
print("2. Amend Customer Feedback.")
print("3. Delete Customer Feedback.")
print("4. Analyse All Feedback.")
print("5. Analyse Feedback By Location.\n")

def input_feedback():
    """
    Input feedback from the customer
    """
    print("Data should be six numbers, seperated by commas.")
    print("e.g.: 10, 9, 10, 8, 9, 8\n")

    data_str = input("Enter your data here:\n")
    print(f"The data provided is {data_str}")

input_feedback()
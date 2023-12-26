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

def get_feedback():
    """
    Get feedback from the user
    """
    print("Please enter customer feedback.")
    print("Data should be six numbers, seperated by commas.")
    print("e.g.: 10, 9, 10, 8, 9, 8\n")

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")

get_feedback()
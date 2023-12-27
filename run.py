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

print("Welcome to Juniper Cocktails Customer Feedback Application.\n")
print("Please use this application to input, amend, or delete customer")
print("feedback, or to analyse existing feedback.\n")

def select_option():

    print("Please select one of the following options and press enter:\n")

    print("1. Input Customer Feedback")
    print("2. Amend Customer Feedback")
    print("3. Delete Customer Feedback")
    print("4. Analyse All Feedback")
    print("5. Analyse Feedback By Location\n")

select_option()

option = int(input())



def input_feedback():
    """
    Input feedback from the customer
    """
    feedback_dict = {}
    print("Please enter a UK venue location (e.g. London, Edinburgh):")
    location = str(input())
    print("Please enter a score from 1-10 for Staff Friendliness:")
    friend = int(input())
    print("Please enter a score from 1-10 for Staff Professionalism:")
    profess = int(input())
    print("Please enter a score from 1-10 for the Venue:")
    venue = int(input())
    print("Please enter a score from 1-10 for Price / Value for Money:")
    price = int(input())
    print("Please enter a score from 1-10 for Quality:")
    quality = int(input())
    print("Please enter a score from 1-10 for Range / Variety of Cocktails:")
    variety = int(input())
    feedback_dict['location'] = location
    feedback_dict['friend'] = friend
    feedback_dict['profess'] = profess
    feedback_dict['venue'] = venue
    feedback_dict['price'] = price
    feedback_dict['quality'] = quality
    feedback_dict['variety'] = variety

    print(f"You entered {feedback_dict.values()}")


if option == 1:
    input_feedback()
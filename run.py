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
print("Please use this application to input new customer feedback,")
print("or to analyse existing feedback.\n")

def select_option():

    print("Please select one of the following options and press enter:\n")

    print("1. Input Customer Feedback")
    print("2. Analyse Feedback For the Last 5 Entries")
    print("3. Analyse Feedback By Location\n")

select_option()

option = int(input())

def input_feedback():
    """
    Input feedback from the customer
    """
    print("Please enter a Juniper Cocktails venue location (e.g. London):")
    location = str(input())
    print("Please enter a score from 1-10 for Staff Friendliness,")
    print("with 1 being poor and 10 being excellent:")
    friend = int(input())
    print("Please enter a score from 1-10 for Staff Professionalism,")
    print("with 1 being poor and 10 being excellent:")
    profess = int(input())
    print("Please enter a score from 1-10 for the Venue,")
    print("with 1 being poor and 10 being excellent:")
    venue = int(input())
    print("Please enter a score from 1-10 for Price / Value for Money,")
    print("with 1 being poor and 10 being excellent:")
    price = int(input())
    print("Please enter a score from 1-10 for Quality,")
    print("with 1 being poor and 10 being excellent:")
    quality = int(input())
    print("Please enter a score from 1-10 for Range / Variety of Cocktails,")
    print("with 1 being poor and 10 being excellent:")
    variety = int(input())
    print("Please enter your favourite cocktail at the venue:")
    cocktail = str(input())
    feedback_list = []
    feedback_list.extend((location, friend, profess, venue))
    feedback_list.extend((price, quality, variety, cocktail))

    print("Updating Juniper Cocktails Worksheet...\n")
    feedback_worksheet = SHEET.worksheet("feedback")
    feedback_worksheet.append_row(feedback_list)
    print("Worksheet Updated Successfully.\n")

def feedback_last_5():
    """
    Analyse last 5 entries in the feedback worksheet
    """
    print("Analysing last 5 entries")

def feedback_loc():
    """
    Analyses feedback in worksheet by location
    """
    print("You are analysing feedback by location")

if option == 1:
    input_feedback()
elif option == 2:
    feedback_last_5()
elif option == 3:
    feedback_loc()

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

def select_option():
    """
    Provides the user with the option to either input new customer feedback, 
    or to analyse existing feedback
    """
    while True:
        print("Please select one of the following options and press enter:\n")
        print("1. Input Customer Feedback")
        print("2. Analyse Existing Feedback\n")
        
        try:
            option = int(input())
        except:
            print("You did not enter a number, you entered a string.")
            print("Please try again\n")
        else:
            if validate_data(option):
                if option == 1:
                    input_feedback()
                elif option == 2:
                    analyse_feedback()
                break

def input_feedback():
    """
    Input feedback from the customer
    """
    print("Please enter a Juniper Cocktails venue location (e.g. London):")
    location = str(input())
    
    print("Please enter a score from 1-10 for Staff Friendliness,")
    print("with 1 being poor and 10 being excellent:")
    
    while True:
        try:
            friend = int(input())
            break
        except ValueError:
            print("Please enter a number between 1 and 10.")
    
    print("Please enter a score from 1-10 for Staff Professionalism,")
    print("with 1 being poor and 10 being excellent:")

    while True:
        try:
            profess = int(input())
            break
        except ValueError:
            print("Please enter a number between 1 and 10.")

    print("Please enter a score from 1-10 for the Venue,")
    print("with 1 being poor and 10 being excellent:")

    while True:
        try:
            venue = int(input())
            break
        except ValueError:
            print("Please enter a number between 1 and 10.")

    print("Please enter a score from 1-10 for Price / Value for Money,")
    print("with 1 being poor and 10 being excellent:")

    while True:
        try:
            price = int(input())
            break
        except ValueError:
            print("Please enter a number between 1 and 10.")

    print("Please enter a score from 1-10 for Quality,")
    print("with 1 being poor and 10 being excellent:")

    while True:
        try:
            quality = int(input())
            break
        except ValueError:
            print("Please enter a number between 1 and 10.")

    print("Please enter a score from 1-10 for Range / Variety of Cocktails,")
    print("with 1 being poor and 10 being excellent:")

    while True:
        try:
            variety = int(input())
            break
        except ValueError:
            print("Please enter a number between 1 and 10.")

    print("Please enter your favourite cocktail at the venue:")
    cocktail = str(input())
    print("Please enter any other feedback or comments the customer wishes to include:")
    comment = str(input())
    feedback_list = []
    feedback_list.extend((location, friend, profess, venue))
    feedback_list.extend((price, quality, variety, cocktail, comment))

    print("Updating Juniper Cocktails Worksheet...\n")
    feedback_worksheet = SHEET.worksheet("feedback")
    feedback_worksheet.append_row(feedback_list)
    print("Worksheet Updated Successfully.\n")

def analyse_feedback():
    """
    Collects columns of data from the feedback worksheet, for each feedback 
    criteria, returning the data as a list of lists.
    """
    feedback_all = SHEET.worksheet("feedback")
    
    columns = []
    for ind in range(2, 8):
        column = feedback_all.col_values(ind)
        columns.append(column)
    print(columns)

def get_average_scores_all():
    """
    Calculates the average scores for each of the feedback criteria
    """
    print("Calculating average scores...\n")

def validate_data(value):
    """
    Checks whether data input is valid, and throws an exception if not
    """
    try:
        if value != 1 and value != 2:
            raise ValueError(
                f"Incorrect value entered.  You entered {value}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

def main():
    """
    Run all program functions
    """
    select_option()

print("Welcome to Juniper Cocktails Customer Feedback Application.\n")
print("Please use this application to either input new customer feedback,")
print("or to analyse existing feedback.\n")

main()

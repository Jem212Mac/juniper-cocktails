import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    or to analyse existing feedback.
    """
    while True:
        print("Please select one of the following options and press enter:\n")
        print("1. Input Customer Feedback")
        print("2. Analyse Existing Feedback\n")
        try:
            option = int(input())
        except ValueError:
            print("You did not enter a number, you entered a string.")
            print("Please try again.\n")
        else:
            if validate_data(option):
                if option == 1:
                    input_feedback()
                elif option == 2:
                    break


def input_feedback():
    """
    Allows the user to input customer feedback into the application
    and updates the feedback worksheet.
    """
    print("Please enter a Juniper Cocktails venue from the following:")
    print("London, Manchester, Birmingham, Edinburgh, Glasgow, or Dundee\n")
    venue_loc = ["London", "Manchester", "Birmingham", "Edinburgh",
                 "Glasgow", "Dundee"]
    while True:
        try:
            location = str(input()).title()
        except ValueError:
            print("Please input a valid location.")
        else:
            if location not in venue_loc:
                print("Please input a valid location.")
            else:
                break
    print("Please enter a score from 1-10 for Staff Friendliness,")
    print("with 1 being poor and 10 being excellent:")
    while True:
        try:
            friend = int(input())
        except ValueError:
            print("Please enter a number rather than a string.")
        else:
            if friend > 10:
                print("Number must be less than or equal to 10.")
            elif friend < 1:
                print("Number must be greater than or equal to 1.")
            else:
                break
    print("Please enter a score from 1-10 for Staff Professionalism,")
    print("with 1 being poor and 10 being excellent:")
    while True:
        try:
            profess = int(input())
        except ValueError:
            print("Please enter a number rather than a string.")
        else:
            if profess > 10:
                print("Number must be less than or equal to 10.")
            elif profess < 1:
                print("Number must be greater than or equal to 1.")
            else:
                break
    print("Please enter a score from 1-10 for the Venue,")
    print("with 1 being poor and 10 being excellent:")
    while True:
        try:
            venue = int(input())
        except ValueError:
            print("Please enter a number rather than a string.")
        else:
            if venue > 10:
                print("Number must be less than or equal to 10.")
            elif venue < 1:
                print("Number must be greater than or equal to 1.")
            else:
                break
    print("Please enter a score from 1-10 for Price / Value for Money,")
    print("with 1 being poor and 10 being excellent:")
    while True:
        try:
            price = int(input())
        except ValueError:
            print("Please enter a number rather than a string.")
        else:
            if price > 10:
                print("Number must be less than or equal to 10.")
            elif price < 1:
                print("Number must be greater than or equal to 1.")
            else:
                break
    print("Please enter a score from 1-10 for Quality,")
    print("with 1 being poor and 10 being excellent:")
    while True:
        try:
            quality = int(input())
        except ValueError:
            print("Please enter a number rather than a string.")
        else:
            if quality > 10:
                print("Number must be less than or equal to 10.")
            elif quality < 1:
                print("Number must be greater than or equal to 1.")
            else:
                break
    print("Please enter a score from 1-10 for Range / Variety of Cocktails,")
    print("with 1 being poor and 10 being excellent:")
    while True:
        try:
            variety = int(input())
        except ValueError:
            print("Please enter a number rather than a string.")
        else:
            if variety > 10:
                print("Number must be less than or equal to 10.")
            elif variety < 1:
                print("Number must be greater than or equal to 1.")
            else:
                break
    print("Please enter your favourite Juniper Cocktails signature cocktail")
    print("from the following list: Mai Tai, Long Island Iced Tea, Manhattan,")
    print("Negroni, Singapore Sling, or Pina Colada\n")
    sig_cocktails = ["Mai Tai   ", "Long Island Iced Tea", "Manhattan",
                     "Negroni", "Singapore Sling", "Pina Colada"]
    while True:
        try:
            cocktail = str(input()).title()
        except ValueError:
            print("Please input a cocktail from the signature list.")
        else:
            if cocktail not in sig_cocktails:
                print("Please input a cocktail from the signature list.")
            else:
                break
    print("Please enter any other customer feedback or comments:")
    comment = str(input()).capitalize()
    feedback_list = []
    feedback_list.extend((location, friend, profess, venue))
    feedback_list.extend((price, quality, variety, cocktail, comment))
    print("Updating Juniper Cocktails Worksheet...\n")
    feedback_worksheet = SHEET.worksheet("feedback")
    feedback_worksheet.append_row(feedback_list)
    print("Worksheet Updated Successfully.\n")


def get_scores_by_criteria():
    """
    Collects columns of data from the feedback worksheet, for each feedback
    criteria, returning the data as a list of lists.
    """
    feedback_all = SHEET.worksheet("feedback")
    columns = []
    for ind in range(2, 8):
        column = feedback_all.col_values(ind)
        column.pop(0)
        columns.append(column)
    return columns


def calculate_averages_by_criteria(data):
    """
    Calculates the average score for each of the feedback criteria
    """
    print("Calculating average scores...\n")

    average_feedback_data = []

    for column in data:
        int_column = [int(num) for num in column]
        average = sum(int_column) / len(int_column)
        average_feedback_data.append(round(average))
    print("Updating Juniper Cocktails Averages Worksheet...\n")
    feedback_worksheet = SHEET.worksheet("averages")
    feedback_worksheet.append_row(average_feedback_data)
    print("Worksheet Updated Successfully.\n")


def validate_data(value):
    """
    Checks whether data input from the user is valid, and raises an exception
    if the data is not valid.
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
    Runs all program functions.
    """
    select_option()
    feedback_columns = get_scores_by_criteria()
    calculate_averages_by_criteria(feedback_columns)


print("Welcome to Juniper Cocktails Customer Feedback Application.\n")
print("Please use this application to input new customer feedback,")
print("or to analyse existing feedback.\n")
main()

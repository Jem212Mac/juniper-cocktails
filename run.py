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


def input_feedback():
    """
    Allows the user to input customer feedback into the application
    to update the feedback worksheet.
    """
    print("Please enter a Juniper Cocktails venue from the following list:")
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
    sig_cocktails = ["Mai Tai", "Long Island Iced Tea", "Manhattan",
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
    return feedback_list


def update_worksheet(data, worksheet):
    """
    Updates the relevant worksheet with the data provided.
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")


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
    return average_feedback_data


def calculate_diff():
    """
    Calculates the difference between the input feedback scores
    and the average scores across all venues.
    """
    print("Calculating difference between input scores")
    print("and average scores...\n")
    feedback_scores = SHEET.worksheet("feedback").get_all_values()
    feedback_row = feedback_scores[-1]
    feedback_row.pop(0)
    feedback_row.pop(7)
    feedback_row.pop(6)
    average_scores = SHEET.worksheet("averages").get_all_values()
    average_row = average_scores[-1]

    feedback_diff = []
    for averages, feedback in zip(average_row, feedback_row):
        diff = int(feedback) - int(averages)
        feedback_diff.append(diff)

    print(f"The difference between your scores")
    print(f"and the averages for staff friendliness,")
    print(f"staff professionalism, venue, price, quality,")
    print(f"and variety are: {feedback_diff}\n")
    print("If any of your scores are more than 3 below the average,")
    print("you should look to make improvements in those areas\n")


def main():
    """
    Runs all program functions.
    """
    feedback_data = input_feedback()
    update_worksheet(feedback_data, "feedback")
    feedback_columns = get_scores_by_criteria()
    averages_data = calculate_averages_by_criteria(feedback_columns)
    update_worksheet(averages_data, "averages")
    calculate_diff()


print("Welcome to Juniper Cocktails Customer Feedback Application.\n")
print("Please use this application to input new customer feedback")
print("and compare it to average feedback from across all")
print("Juniper Cocktails venues.\n")
main()

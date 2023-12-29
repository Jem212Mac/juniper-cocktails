# Juniper Cocktails Customer Feedback Application

Juniper Cocktails is an imaginary chain of cocktail bar's operating at various locations across the UK.

The main purpose of this application is to allow a user (usually a staff member at one of Juniper Cocktails venues) to input customer feedback that will be recorded on a Google sheets feedback worksheet.  This feedback could be input in real-time by asking the customer specific questions while at the venue, or could be gathered and input from a paper-based survey completed by the customer before leaving the venue.

The secondary purpose of the application is to allow user's at the venue (particularly a manager or franchisee owner) to analyse the feedback for their venue and compare it to feedback from other venue's in order to gain insights into what improvements could be made at their venue.

Juniper Cocktails would like to maintain a certain level of consistency across their venues and the aim of this application is to allow franchisee owners or managers to input customer feedback and compare their feedback with the feedback from other venues.  This will allow owners or managers to ensure they are maintaining their feedback scores at an appropriate level, and improve upon underperforming areas where needed.  Use of this application by venues will also allow other Juniper Cocktails stakeholders (e.g. area manager's) to examine and analyse feedback via the Google Sheets worksheets.


## User Stories

* As a User, I would like to be able to input customer feedback directly into the system, real-time, while the customer is still present at the venue.
* As a User, I would like to be able to input customer feedback from a paper-based survey completed by the customer before leaving the venue.
* As a User, I would like to be able to see the average scores, for each feedback criteria, for all Juniper Cocktails venues.
* As a User, I would like to be able to see the average scores, for each feedback criteria, for a specific Juniper Cocktails venue.
* As a User, I would like to be able to compare the average scores for a specific venue (e.g. my venue) with the average scores for all venues so that I can gain insight into what we are doing well and where we need to make improvements.
* As a User, I would like to be able to see the highest and lowest scores, for each feedback criteria, for all Juniper Cocktails venues.
* As a User, I would like to be able to see the highest and lowest scores, for each feedback criteria, for a specific Juniper Cocktails venue.
* As a User, I would like to be able to analyse the feedback data on a regular basis so that I can gain regular insights for potential improvements.
* As a User, I would like the system to update Google Sheets worksheets so that Juniper Cocktails stakeholders can review and analyse the feedback.
* As a User, I would like to be able to input the customer's favourite cocktail recipe so that we can ensure we keep a record of the most favourited cocktail per venue so we never remove this from the menu.


## Features

I originally created a rough flow chart diagram with pen and paper to decide what I wanted the application to do.  This flow chart diagram evolved over time as I decided to remove some features and add other features.  With CRUD operations in mind, I originally planned to add features that would allow a user of the application to amend or delete existing customer feedback.  However, I decided that in a real-world solution, Juniper Cocktails would not want to allow any user to be able to amend or delete existing data; this would be operations reserved only for Juniper Cocktails stakeholders, if needed, and they could easily perform these operations within the resulting Google Sheets worksheets.  Therefore I decided to remove these features.  The final flowchart was created using Lucid Chart (see below).

## Deployment

## Local Development
Codeanywhere was used as the IDE for local development of the application and GitHub was used for version control.

## Testing

I tested the data input for the initial 2 options presented to the user to ensure that the user can select only the number 1 or the number 2.  If the user inputs a string, an error is displayed (see below).

If the user inputs any number other than 1 or 2 another error is displayed (see below).

I tested the data input for the 'Input Customer Feedback' option.  

I tested to ensure that when the venue is requested, only a valid venue from the list can be entered.  The venue can be entered in capitals or lowercase, but will be recorded in the feedback worksheet in the 'title' format.  When an invalid venue is entered, and error is displayed (see below).

I tested to ensure that when a feedback score is required, only an integer can be entered, not a string.  If I string is entered, the below error is displayed.

I also tested to ensure that only a number between 1 and 10 can be entered.  If a number below 1 is entered, the below error is displayed.

If a number greater than 10 is entered, the below error is displayed.

I tested to ensure that when the customers favourite signature cocktail is requested, only a valid cocktail from the list can be entered.  The cocktail can be entered in capitals or lowercase, but will be recorded in the feedback worksheet in the 'title' format.  When an invalid cocktail is entered, and error is displayed (see below).


## Credits

## Acknowledgments

# Juniper Cocktails Customer Feedback Application

Juniper Cocktails is an imaginary chain of cocktail bar's operating at various locations across the UK.

The main purpose of this application is to allow a user (usually a franchisee owner or manager at one of Juniper Cocktails venues) to input customer feedback that will be recorded on a Google sheets feedback worksheet.  This feedback could be input in real-time by asking the customer specific questions while at the venue, or could be gathered and input from a paper-based survey completed by the customer before leaving the venue.

The secondary purpose of the application is to provide the user with information on how the input feedback compares to average feedback scores across all Juniper Cocktails venues.

Juniper Cocktails would like to maintain a certain level of consistency across their venues and the aim of this application is to allow franchisee owners or managers to input customer feedback and compare this feedback with the average feedback from across all venues.  This will allow owners or managers to ensure they are maintaining their feedback scores at an appropriate level, and improve upon underperforming areas where needed.  Use of this application by venues will also allow senior Juniper Cocktails stakeholders to examine and analyse feedback via the Google Sheets worksheets.


## User Stories

* As a User, I would like to be able to input customer feedback directly into the system, real-time, while the customer is still present at the venue.
* As a User, I would like to be able to input customer feedback from a paper-based survey completed by the customer before leaving the venue.
* As a User, I would like to be able to compare the customer feedback scores I input to the average scores, for each feedback criteria, for all Juniper Cocktails venues so that I can monitor where improvements might be needed.
* As a User, I would like the system to update Google Sheets worksheets so that senior Juniper Cocktails stakeholders can review and analyse the feedback to gain insights on where improvements may be needed.
* As a User, I would like to be able to input the customer's favourite cocktail recipe so that Juniper Cocktails can record this to ensure we never remove the most popular cocktails from our menu.


## Features

I originally created a rough flow chart diagram with pen and paper to decide what I wanted the application to do.  This flow chart diagram evolved over time as I decided to remove some features and add other features.  With CRUD operations in mind, I originally planned to add features that would allow a user of the application to amend or delete existing customer feedback.  However, I decided that in a real-world solution, Juniper Cocktails would not want to allow any user to be able to amend or delete existing data; this would be operations reserved only for Juniper Cocktails senior stakeholders, if needed, and they could easily perform these operations within the resulting Google Sheets worksheets.  Therefore I decided to remove these features.  The final flowchart was created using Lucid Chart (see below).


![Lucid Chart](documentation/Lucid%20Chart.png)


The application initially requests the user to 'Input Customer Feedback'; the user is faced with a number of questions to ensure that feedback is provided in a clear and consistent manner, focussing on specific feedback criteria; location, staff friendliness, staff professionalism, venue, price, quality and range/variety of cocktails. All data input is checked to ensure that it is valid, and if not, the user is asked to input the data again.  It should not be possible to input any invalid data.  In addition, valid data is 'tidied up' before it is added to any Google worksheets using the python 'title' and 'capitalize' methods. 


![Application1](documentation/Application%201.png)


The user is also asked to input the customer's favourite Juniper Cocktails signature cocktail (from a list provided) and can input some free text as customer comments if required.  Once all of this data is gathered, the feedback worksheet of a Google Sheets form is updated with this data (see below).


![Feedback Worksheet](documentation/Feedback%20Worksheet.png)


The application then uses this data to calculate the average feedback scores for all input in the feedback worksheet and appends this to the averages worksheet (see below).


![Averages Worksheet](documentation/Averages%20Worksheet.png)


The application then reads in the last rows of both the feedback worksheet and the averages worksheet and uses the data to calculate the difference between the scores.  The differences between the scores is displayed to the user to allow them to determine where improvements might be needed (see below).


![Application2](documentation/Application%202.png)


## Local Development
Codeanywhere was used as the IDE for local development of the application and GitHub was used for version control.


## Forking

If you would like to work on this code you can click on the repository here (https://github.com/Jem212Mac/juniper-cocktails) and click on 'Fork' to create your own fork of the code to work on.


## Deployment

The application was deployed to Heroku.  In order to deploy to Heroku, the following steps were performed:

1. The command 'Pip3 freeze > requirements.txt' was used in the IDE terminal in order to create a requirements.txt file which included the dependencies for the project.  Heroku needs this file to install the required dependencies before the application is run.
2. I created a new Heroku account here: (https://id.heroku.com/login).
3. From the Heroku dashboard I clicked 'Create new app' and input a unique name for the app, a region, and clicked 'create app'.
4. I clicked on the Settings tab and went to the Config Vars section.
5. I added 'CREDS' as a key and copied my credentials for my Google API in as the value and clicked 'Add'.
6. I also added the key PORT and value 8000 to the Config Vars.
7. I added two buildpacks; one for Python and one for Node.js, making sure they were listed in this order, with Python first, and Node.js second.
8. I clicked on the 'Deploy' tab, chose Github as my deployment method, and searched for my github repository to connect.
9. For this project I chose to manually deploy at regular intervals.


## Testing  

* I tested to ensure that when the venue is requested, only a valid venue from the list can be entered.  The venue can be entered in capitals or lowercase, but will be recorded in the feedback worksheet in the 'title' format.  When an invalid venue is entered, an error message is displayed.
* I tested to ensure that when a feedback score is required, only an integer can be entered, not a string.  If I string is entered, an error is displayed.
* I tested to ensure that only a number between 1 and 10 can be entered.  If a number below 1 is entered, an error is displayed.  If a number greater than 10 is entered, an error is displayed.
* I tested to ensure that when the customers favourite signature cocktail is requested, only a valid cocktail from the list can be entered.  The cocktail can be entered in capitals or lowercase, but will be recorded in the feedback worksheet in the 'title' format.  When an invalid cocktail is entered, an error is displayed.
* I tested to ensure that any free text can be added as customer comments, including leaving this input empty if desired.
* I tested to ensure that once all feedback data was input, the correct data, in the expected format, was appended to the feedback worksheet.
* I tested to ensure that once all feedback data was input, the average scores for all feedback was appended to the averages worksheet.  I checked that these values were calculated correctly, and reported as rounded integers.


### Bugs

1. Early on in the development process I realised that I had inadvertantly pushed my creds.json file to github.  I was well aware not to do this, but it happened by accident; the .gitignore file had been open in my IDE and I accidentally typed git into this file on the end of the creds.json filename, instead of into the terminal.  This resulted in the creds.json file being accidentally pushed to GitHub.  I fixed this by revoking the pushed credentials and creating new credentials and a new creds.json file after I had fixed the .gitignore file.
2. After deploying my application to Heroku I discovered a bug whereby I could add anything as a favourite cocktail.  I realised this was because I reused the code I created for validation of the venue selection for validation of the cocktail selected, but I forgot to change all of the variable names.  I updated the code and this was resolved.
3. On completion of testing, I am not aware of any unresolved bugs remaining in the code / application. 


### Validator Testing

Code was run through the PEP validator (https://pep8ci.herokuapp.com/) and no issues were found (see below).


![PEP8](documentation/PEP8.png)


## Future Enhancements

Given additional time, I would like to add the following features to this application:

1. I would add a timestamp when the feedback data is added to the feedback worksheet and use this to pull out the month and year so that the feedback data could be monitored on a monthly basis to check for patterns or issues.
2. I would add the ability for the user to search to find the average score for each feedback criteria for their venue so they could check their average against the overall average scores.
3. I would add the ability for the user to determine their average score for each criteria on a monthly basis.

## Credits & Acknowledgements

At various moments during development, I used the following websites to check my understanding of how to use specific python statements (for example, while true loops and try, except statements):

* https://stackoverflow.com/
* https://www.w3schools.com/

I also referred back to the Code Institute Love Sandwiches walkthrough project, particularly as a reminder of how to use the Python zip() function.

# Dance Cork Firkin Crane (DCFC) Cleaning Schedule.

![Dance Cor Firkin Crane and New Angel Logo](https://github.com/MarMarAgain/DCFC-Cleaning-Schedule/assets/158588349/016f6927-0313-4fb3-9e64-f24b5c43aac5)

### An application for DCFC to easily reformat their cleaning schedule.

This application was developed for Dance Cork Firkin Crane (DCFC) and Angel Cleaning. Angel Cleaning is an external cleaning service regularly employed at the theater, as well as at Jack Lynch House, an artist accommodation managed by DCFC. DCFC uses one format for their cleaning schedules, while Angel Cleaning prefers a different one. This program converts the cleaning schedule from DCFC's format to Angel Cleaning's preferred format, presenting it neatly on Sheet 2.

## Function.

- The program prompts the user to confirm the current month by inputting the data (Month).

- Using datetime, the entered month is validated. An additional precaution is taken to restrict the printing of the month's schedule to the current calendar month, ensuring accurate information is forwarded to Angel Cleaning.

- After confirming the correct month, Sheet 2 is cleared, and the schedule from Sheet 1 is formatted according to Angel Cleaning's requirements and printed on Sheet 2.

- Subsequently, the program computes the total regular billable hours and extra hours separately. It's important to note that "extra hours" refer to Sunday hours, which are billed at time and a half. This term is used internally within the organizations for clarity.

### User flow Diagram.

![User Flow Diagram](https://github.com/MarMarAgain/DCFC-Cleaning-Schedule/assets/158588349/aad127a0-d1ae-414a-8cf6-f49ad08105be)

### Dance Cork Firkin Crane Format
![Dance Cork Firkin Crane](https://github.com/MarMarAgain/DCFC-Cleaning-Schedule/assets/158588349/9dd01e0f-516b-4651-a324-367b8dba1cf3)

### Angel Cleaning Format
![Angel Cleaning's perfered format](https://github.com/MarMarAgain/DCFC-Cleaning-Schedule/assets/158588349/6e43ef13-1580-4219-9ffa-e27625986ce4)

## Checks - Snyk.io 

![Snyk.io check](https://github.com/MarMarAgain/DCFC-Cleaning-Schedule/assets/158588349/39f2218a-d4ae-4139-b781-bcc40ce6c494)

## Deployment

The application deployment faced some obstacles due to errors occurring within the IDE environment. Consequently, the CREDS file had to be added separately to GitHub. This file pertains to a third-party account tailored specifically for this application. It's important to note that access to both companies' data is restricted solely to their cleaning rota and is not accessible beyond that context.

- Deployment achieved via  Heoku.
- The final iteration of the code was copied to the relevent GitHub repository.
- The relavent Creds file was added to the Heroku account.
- Two build packs were also added to the Heroku account in this order :
  1. `heroku/python`
  2. `heroku/nodejs`
- The project was deployed and didn't function as the creds file wasn't picked up by the application ( due to IDE erros ).
- Apon advice from tech/tutor support, the import so method was tried however this was still unsucessful.
- The dcfccreds.json file was added to the GitHub repository.
- The application was redeployed and foud to be fully functional.
  ***CREDS issue documented in issues***

## Further Developmet
This project has potential to develop in a number of ways:
- The "extra hours" section can expand to account for bank holidays
- A projected cost total can be implemented.
- Apon a user prompt, the completed Angel formatted list can be sent directly to the relavent parties.


## Credits

Extra reading / help from the following book : Matthes, Eric. Python Crash Course, 3rd Edition: A Hands-on, Project-Based Introduction to Programming. No Starch Press, Incorporated, 2023. 

datetime method used : [Datetime](https://stackoverflow.com/questions/28189442/datetime-current-year-and-month-in-python)

# Dance Cork Firkin Crane (DCFC) Cleaning Schedule.

![Dance Cor Firkin Crane and New Angel Logo](logos.png)

### An application for DCFC to easily reformat their cleaning schedule.

This application was developed for Dance Cork Firkin Crane (DCFC) and Angel Cleaning. Angel Cleaning is an external cleaning service regularly employed at the theater, as well as at Jack Lynch House, an artist accommodation managed by DCFC. DCFC uses one format for their cleaning schedules, while Angel Cleaning prefers a different one. This program converts the cleaning schedule from DCFC's format to Angel Cleaning's preferred format, presenting it neatly on Sheet 2.

## Function.

- The program prompts the user to confirm the current month by inputting the data (Month).

- Using datetime, the entered month is validated. An additional precaution is taken to restrict the printing of the month's schedule to the current calendar month, ensuring accurate information is forwarded to Angel Cleaning.

- After confirming the correct month, Sheet 2 is cleared, and the schedule from Sheet 1 is formatted according to Angel Cleaning's requirements and printed on Sheet 2.

- Subsequently, the program computes the total regular billable hours and extra hours separately. It's important to note that "extra hours" refer to Sunday hours, which are billed at time and a half. This term is used internally within the organizations for clarity.

### User flow Diagram.

![User Flow Diagram](diagram.png)

### Dance Cork Firkin Crane Format
![User Flow Diagram](diagram.png)

### Angel Cleaning Format
![User Flow Diagram](diagram.png)

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Checks 

![Syk check](SYK.png)

## Deployment

The application deployment faced some obstacles due to errors occurring within the IDE environment. Consequently, the CREDS file had to be added separately to GitHub. This file pertains to a third-party account tailored specifically for this application. It's important to note that access to both companies' data is restricted solely to their cleaning rota and is not accessible beyond that context.

- Deployment happened on a Heoku account.
- The final iteration of the code was copied to the relevent GitHub repository.
- The relavent Creds file was added to the Heroku account.
- Two build packs were also added to the Heroku account in this order :
  1. `heroku/python`
  2. `heroku/nodejs`
- The project was deployed and didn't function as the creds file wasn't picked up by the application ( due to IDE erros ).
- Apon advice from tech support the, the CREDS file was added to the GitHub repository.
- The application was redeployed and foud to be fully functional.

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

## Credits

Extra reading / help from the following book : Matthes, Eric. Python Crash Course, 3rd Edition: A Hands-on, Project-Based Introduction to Programming. No Starch Press, Incorporated, 2023. 

datetime method used : **Insert Datetime**

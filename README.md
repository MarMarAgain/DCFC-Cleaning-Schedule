# Dance Cork Firkin Crane (DCFC) Cleaning Schedule.

![Dance Cor Firkin Crane and New Angel Logo](logos.png)

This project is an application built for Dance Cork Firkin Crane and Angel Cleaning. 
Angel Cleaning is a third-party cleaning company that is hired into the Theatre on an almost daily basis. They also clean a DCFC managed artist accommodation - Jack Lyncvh House. There is one format that DCFC writes their cleaning schedule in , and another format that Angel cleaning perfers to receive. This programme rewrites the information from the DCFC formated schedule and rewrites it in the Angel Cleaning Format on Sheet 2. 

## Steps.

- The programme asks the user to confirm the current month via inputted data ( Month) 
- The Month entered is verified using datetime. Restricting the Month to be printed to the current calender month is an extra precaution to ensure the 
  correct information is sent to Angel Cleaning. 
- Once the correct Month is verified,Sheet 2 is cleared and the schedule on Sheet 1 is printed in the Angel Cleaning format on Sheet 2.
- The programme then calculates the total amount of regular billable hours and extra hours repectively._Please note that extra hours equates to Sunday hours, which cost time and a half. "Extra hours" is used as this is the term used internally within the organisations._

### User flow Diagram.

![User Flow Diagram](diagram.png)

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Checks 


## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!

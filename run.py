import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Load Credentials and Access spreadsheet 
CREDS = Credentials.from_service_account_file('dcfccreds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('DCFC cleaning')

def get_month():
    """Get month desired from user"""

    print("Please enter the month you wish to translate")
    print("Write the Month with a capital letter at the beginning - ex: 'March'")

    while True:
        data_str = input("Enter the Month here: ")
        print(f"The Month you provided is {data_str}")

        try:
            validate_data(data_str)
            break 
        except ValueError as e:
            print(f"{e}  Please try again\n")
            

def validate_data(data_str):
    """ Raise an error if the user does not enter a Month"""

    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    if data_str not in months:
        raise ValueError("I said Month Dammit!!")

get_month()


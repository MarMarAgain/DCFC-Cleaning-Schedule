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
           return data_str  # Return the validated month string
       except ValueError as e:
           print(f"Invalid data {e}. Please try again\n")


def validate_data(data_str):
   """ Raise an error if the user does not enter a Month"""
   months = ["January", "February", "March", "April", "May", "June",
             "July", "August", "September", "October", "November", "December"]
   if data_str not in months:
       raise ValueError("I said Month Dammit!!")


def get_column_values(worksheet, column_name):
   """Get values under a specific column in a worksheet."""
   # Find the column index by searching for the column letter
   column_values = worksheet.col_values(1)


   result = column_values[1:]
   return result


def main():
   # Get the month from the user
   selected_month = get_month()


   # Open the source worksheet and get values from sheet 1
   source_worksheet = SHEET.worksheet("Sheet1")
   result = get_column_values(source_worksheet, selected_month)


   # Open sheet two, and add them in a column.
   target_worksheet = SHEET.worksheet("Sheet2")
   start_cell = "A1"
   for value in result:
       target_worksheet.append_row([value])


   print("Values moved successfully from Sheet1 to Sheet2.")

main()
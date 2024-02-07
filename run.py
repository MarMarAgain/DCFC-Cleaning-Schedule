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
        print(f"The Month you provided is {data_str}\n")
        print(f"Converting data now...\n")

        try:
            validate_data(data_str)
            # Return the validated month
            return data_str  
        except ValueError as e:
            print(f"Invalid data {e}. Please try again\n")

def validate_data(data_str):
    # Raise an error if the user does not enter a Month
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    if data_str not in months:
        raise ValueError("I said Month Dammit!!")

def get_sheet1_data():
    # Open the source worksheet and get values from sheet 1
    source_worksheet = SHEET.worksheet("Sheet1")
    data = source_worksheet.get_all_values()

    # Process the data
    processed_data = []
    for row in data:
        date = row[0]
        day = row[1]
        area = row[2]
        time = row[3]
        duration = row[4]
        processed_data.append(["Dance Cork Firkin Crane", area, duration, date, time])  # Remove unnecessary quotation mark

    return processed_data

def main():
    # Get the month from the user
    selected_month = get_month() 

    # Get data from Sheet1
    processed_data = get_sheet1_data()

    # Open target worksheet (Sheet2)
    target_worksheet = SHEET.worksheet("Sheet2")

    # Write processed data to the target worksheet. Start from the first row/column
    for i, row in enumerate(processed_data, start=1): 
        target_worksheet.insert_row(row, i)

    print("Data has been successfully written to Sheet2.")

main()

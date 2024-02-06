import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Load credentials from the file
CREDS = Credentials.from_service_account_file('dcfccreds.json')

# Authorize the client using the credentials and scopes
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Open the spreadsheet
try:
    SHEET = GSPREAD_CLIENT.open('DCFC cleaning')
    print("Successfully connected to Google Sheets.")
    print("Spreadsheet title:", SHEET.title)
except gspread.SpreadsheetNotFound:
    print("The specified spreadsheet was not found.")
except gspread.exceptions.APIError as e:
    print("An error occurred while accessing Google Sheets API:", e)
except Exception as e:
    print("An unexpected error occurred:", e)

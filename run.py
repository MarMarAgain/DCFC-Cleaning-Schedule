import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

'Load Credentials and  Access spreadsheet' 
CREDS = Credentials.from_service_account_file('dcfccreds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

'Open the spreadsheet'
try:
    SHEET = GSPREAD_CLIENT.open('DCFC cleaning')
    print("Successfully connected to Google Sheets.")
    print("Spreadsheet title:", SHEET.title)
    

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('python_quiz')

def get_quiz_data(question_title="questions"):
    """
    Retrieve quiz data and returns list of list representing questions with options.
    """
    try:
        worksheet = SHEET.worksheet(question_title)
        # Skip header row and retrieve questions and options
        questions_and_options = worksheet.get_all_values()[1:]
        return questions_and_options
    except gspread.exceptions.WorksheetNotFound:
        print(f"Worksheet '{question_title}' not found.")
        return []

# Test the function
quiz_data = get_quiz_data()
print(quiz_data)



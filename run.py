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

print("Welcome to the Python Quiz Game!")
print("Answer a series of Python-related questions and see how well you know the language.")
print("For each question, choose the correct option (a, b, c, or d). Let's get started!\n")


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
# quiz_data = get_quiz_data()
# print(quiz_data)


def display_question(question_number, question_options):
    """
    Display a quiz question with options.

    """
    print(f"\nQuestion {question_number}: {question_options[0]}")
    print(f"a) {question_options[1]}")
    print(f"b) {question_options[2]}")
    print(f"c) {question_options[3]}")
    print(f"d) {question_options[4]}\n")

# Test the function
sample_question_options = ["What is 5 + 7?", "4", "5", "6", "12"]
display_question(1, sample_question_options)
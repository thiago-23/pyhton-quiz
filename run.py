import gspread
from google.oauth2.service_account import Credentials
from art import *

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


def get_user_name():
    """
    Get the user's name.
    """
    return input("Please enter your name: ").strip()



def display_question(question_number, question_options):
    """
    Display a quiz question with options.

    """
    print(f"\nQuestion {question_number}: {question_options[0]}")
    print(f"a) {question_options[1]}")
    print(f"b) {question_options[2]}")
    print(f"c) {question_options[3]}")
    print(f"d) {question_options[4]}\n")


def get_user_answer():
    """
    Get the user's choice for a quiz question (a, b, c, or d).
    Implement a while loop to continuously prompt the user to input a valid choice.
    """
    valid_choices = ["a", "b", "c", "d"]

    while True:
        user_answer = input("Please choose between (a, b, c, or d): ").strip().lower()

        if user_answer in valid_choices:
            break
        else:
            print("Invalid choice. Please choose a, b, c, or d.")

    return user_answer

#Test Function
# user_choice = get_user_answer()
# print(f"You chose: {user_choice}")



def main():
    """
    Main function to run the Python Quiz Game.
    """

    art = text2art("Python Quiz") # Return ASCII art as a string in normal modee

    print("Welcome to the Python Quiz Game!")
    print(art)
    print("Answer a series of Python-related questions and see how well you know the language.")
    print("For each question, choose the correct option (a, b, c, or d). Let's get started!\n")

    user_name = get_user_name()
    print(f"Hello {user_name}, Welcome to python Quiz Game!\n")
    print(f"Let's get started\n")

    questions_and_options = get_quiz_data()

if __name__ == "__main__":
    main()
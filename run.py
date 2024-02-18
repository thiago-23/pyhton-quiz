import colorama
import gspread
from colorama import Fore, Style
from google.oauth2.service_account import Credentials
from art import *
colorama.init()

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
    return input("Please enter your name:\n ").strip()



def display_question(question_number, question_options):
    """
    Display a quiz question with options.

    """
    print(f"{Fore.BLUE}Question {question_number}:{Style.RESET_ALL} {question_options[0]}")
    print(f"{Fore.BLUE}a){Style.RESET_ALL} {question_options[1]}")
    print(f"{Fore.BLUE}b){Style.RESET_ALL} {question_options[2]}")
    print(f"{Fore.BLUE}c){Style.RESET_ALL} {question_options[3]}")
    print(f"{Fore.BLUE}d){Style.RESET_ALL} {question_options[4]}\n")


def get_user_answer():
    """
    Get the user's choice for a quiz question (a, b, c, or d).
    Implement a while loop to continuously prompt the user to input a valid choice.
    """
    valid_choices = ["a", "b", "c", "d"]

    while True:
        user_answer = input(f"Please choose between {Fore.BLUE}(a, b, c, or d):{Style.RESET_ALL}").strip().lower()

        if user_answer in valid_choices:
            break
        else:
            print(f"{Fore.RED}Invalid choice!\n{Style.RESET_ALL}")

    return user_answer


def update_sheet_with_answers(user_name, user_answers):
    """
    Update the 'answers' worksheet with user data.
    """
    try:
        answers_sheet = SHEET.worksheet("answers")

        header_row = answers_sheet.row_values(1)
        if len(header_row) > 2:  # Check if there are correct answers in the sheet
            correct_answers = header_row[2:]
        else:
            print("No correct answers found in the 'answers' worksheet.\n")
            return

        correct_answers_count = 0

        # Compare user responses with correct answers starting from column C (index 2)
        for i in range(len(user_answers)):
            if user_answers[i] == correct_answers[i]:
                correct_answers_count += 1

        overall_score = correct_answers_count / len(correct_answers) * 100

        # Find the next available row
        next_row = len(answers_sheet.col_values(1)) + 1

        # Append user data to the next available row without unnecessary values
        user_data = [user_name] + [""] * 1 + user_answers  # Insert one empty column before user choices

        # Append the new user data to the next available row
        answers_sheet.append_row(user_data, value_input_option='USER_ENTERED', insert_data_option='INSERT_ROWS', table_range=f'A{next_row}:L{next_row}')

        print(f"User data successfully stored in 'answers' worksheet.")
        print(f"Correct answers score is: {correct_answers_count}/{len(correct_answers)}")
        print(f"Overall score is: {overall_score:.2f}%\n")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """
    Main function to run the Python Quiz Game.
    """
    while True:
        art = text2art("Python Quiz") # Return ASCII art as a string in normal mode

        print(f"{Fore.BLUE}{art}{Style.RESET_ALL}")
        print(f"Welcome to the Python Quiz Game!\n")
        print(f"Answer a series of Python-related questions \nand see how well you know the language.\n")
        print(f"For each question, choose the correct option {Fore.BLUE}(a, b, c, or d).{Style.RESET_ALL}")
        print(f"Let's get started!\n")

        user_name = get_user_name()
        print(f"Hello {Fore.BLUE}{user_name}{Style.RESET_ALL}, Welcome to python Quiz Game!\n")
        print(f"Let's get started\n")

        questions_and_options = get_quiz_data()

        # Store user choices and display questions
        user_responses = []
        for idx, question_options in enumerate(questions_and_options, start=1):
            display_question(idx, question_options)
            user_answer = get_user_answer()
            user_responses.append(user_answer)

        # Update the 'answers' worksheet with user data
        update_sheet_with_answers(user_name, user_responses)

        while True:
            play_again = input("Do you want to play again? (yes/no): \n").strip().lower()
            if play_again in ["yes", "no"]:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if play_again != "yes":
            print("Thanks for playing. Goodbye!\n")
            break

if __name__ == "__main__":
    # Run the main function
    main()
# Python Quiz

The Python Quiz Game is a console-based application that tests the user's knowledge of Python through a series of 10 multiple-choice questions. the Python Quiz Game is to provide an interactive and educational experience for individuals learning Python. The results are stored in a Google Sheets spreadsheet, facilitating data analysis and visualization.

# Contents

- [User Experience](#user-experience-ux)
    - [User Stories](#user-stories)

- [Play the Game](#playing-the-game)

- [Technologies Used](#technologies-used)

- [Design](#design)
    - [Flowchart](#flowchart)

- [Features](#features) 
    - [Existing Features](#existing-features)
    - [Future Implementations](#future-implementations)

- [Deployment & Local Development](#Deployment--Local-Development)

  - [Deployment](#Deployment)
  - [Local Development](#Local-Development)
    - [How to Fork](#How-to-Fork)
    - [How to Clone](#How-to-Clone)

- [](#)


--- 

# User Experience (UX)

### Key information for the site

The Python Quiz Game is designed for users who are learning Python and want to test their knowledge. The user experience includes:

* Clear instructions for playing the quiz
* User-friendly input prompts
* Display of the final score
* Option to play again or exit the program
---
## User stories:

* As a user, I want to easily start the quiz: I expect a straightforward way to begin the quiz without any complex setup.
* As a user, I want clear instructions on how to play: I expect concise and easy-to-understand instructions on how to navigate through the quiz.
* As a user, I want to track my progress and see my final score: I expect to see my overall score at the end of the quiz.
* As a learner, I want to have a variety of Python-related questions in the quiz, covering different aspects of the language.

---

# Playing the Game:

1. Initiate the Game:
* Begin by entering a valid name to kickstart the game. Your chosen name will personalize the quiz experience.

2. Review the Instructions:
* Take a moment to peruse the provided instructions. This step ensures that you understand how the quiz operates and what is expected of you.

3. Commence the Quiz:
* Dive into the quiz where you'll encounter a series of questions. For each question, choose between options a, b, c, or d as your response.

4. View Your Overall Score:

* After tackling the 10 questions, witness the display of your overall score. This snapshot offers insight into your performance throughout the quiz.

5. Play Again Option:

* Conclude the quiz with a decision. You'll be prompted to decide whether you want to embark on another round. Choose wisely and enjoy the quiz anew!

---

# Technologies Used
* Python

# Libraries
* colorama
* gspread
* google-auth
* Art

# Frameworks & Tools
* [Heroku](https://id.heroku.com/) Platform - for deployment
* [Gitpod](https://gitpod.io/) - for coding and creating the game Quiz
* [GitHub](https://github.com/)  - for version control and deployment
* [Google Sheets API](https://console.cloud.google.com/) - for handling data automation
* [Code Institute template](https://github.com/Code-Institute-Org/p3-template) - for providing necessary files to run the mock terminal in the browser
* [Lucid Cahrt](https://www.lucidchart.com/pages/)- Used to create flowcharts

---

# Design

The design of the Python Quiz Game is kept simple and follows a console-based interface. The terminal provides a straightforward way for users to interact with the application.

## Flowchart
A flowchart summarizing the structure and logic of the application is provided in the Flowchart section.

![Flowchart](documentation%20/flowchart.png)

# Features

## Existing Features
* Introduction to the Python Quiz
* User input for a valid username
* Display of quiz instructions
* Presentation of quiz questions with multiple-choice options
* Validation of user choices
* Calculation and display of the final score
* Option to play again or exit the program

## Future Implementations
* Inclusion of various question levels
* Random selection of questions from a library
* Add a timer for each question, making the quiz more challenging.
* Create a leaderboard feature to showcase the highest scores achieved by users. This can add a competitive element and encourage users to improve their performance.

## Deployment & Local Development

### Deployment

- This site was deployed by completing the following steps:

1. Log in to [Heroku](https://id.heroku.com) or create an account
2. On the main page click the button labeled New in the top right corner and from the drop-down menu select Create New App
3. You must enter a unique app name
4. Next select your region
5. Click on the Create App button
6. The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
7. Click Reveal Config Vars and enter port into the Key box and 8000 into the Value box and click the Add button
8. Click Reveal Config Vars again and enter CREDS into the Key box and the Google credentials into the Value box
9. Next, scroll down to the Build pack section click Add Build pack select Python and click Save Changes
10. Repeat step 8 to add node.js. o Note: The Build packs must be in the correct order. If not click and drag them to move into the correct order
11. Scroll to the top of the page and choose the Deploy tab
12. Select Github as the deployment method
13. Confirm you want to connect to GitHub
14. Search for the repository name and click the connect button
15. Scroll to the bottom of the deploy page and select the preferred deployment type
16. Click either Enable Automatic Deploys for automatic deployment when you push updates to GitHub

### Local Development

#### How to Fork

To fork the thiago-23/pyhton-quiz repository:

1. Log in (or sign up) to Github.
2. Go to the repository for this project, thiago-23/pyhton-quiz.
3. Click the Fork button in the top right corner.

#### How to Clone

To clone the thiago-23/pyhton-quiz repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, Zest-studi-o/thiago-23/pyhton-quiz.
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

---

# quiz-app

## **Quiz App using Open Trivia API**

- based on Day 34 project of Angela Yu's 100 Days of Code course
- currently working with the following restrictions:
  - run the program on MacOS or see bugfix section
  - Single Player Mode must be selected
- all other selections should work

*Note:* The current version is work in progress. Built and tested on MacOS. 

## **Bugfixes**
It is possible to run the code on other distributions than MacOS. If you want to do that, it is currently necessary to replace `tkmacosx.Button` by `tk.Button` in the `mc_ui.py` file. This issue will be fixed in the future.

Variable text size affect button and window frame size (will be fixed). 

Sometimes, the Open Trivia API might return an empty list of results leading the quiz to load no questions. This error occurs when several attempts to load the quiz has been made in a short period of time.

## **To DO's:**
- add topic to question number label
- add total number of questions to score
- enable multiple player mode
- *optionally:* keep track of past highscore and notify player when new highscore has been reached (in single player mode only)
- add possibility to load own questions
- include option to start a new quiz when quiz has been completed


Happy Quizzing!


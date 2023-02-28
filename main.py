from question_model import Question
from quiz_brain import QuizBrain
from boolean_ui import BoolQuizInterface
from setup_ui import ConfigQuizInterface
import requests

question_bank = []

cfg_ui = ConfigQuizInterface()
config = True 
while config:
    if cfg_ui.parameters != {}:
        config = False 

mode = cfg_ui.selected_mode

response = requests.get('https://opentdb.com/api.php',params=cfg_ui.parameters)
response.raise_for_status()

cfg_ui.destroy()

question_data = response.json()['results']
print(question_data)

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = BoolQuizInterface(quiz)

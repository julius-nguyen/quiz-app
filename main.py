from question_model import Question
from quiz_brain import QuizBrain
from boolean_ui import BoolQuizInterface
from mc_ui import MCQuizInterface
from setup_ui import ConfigQuizInterface
import requests

question_bank = []

cfg_ui = ConfigQuizInterface()
config = True 
while config:
    if cfg_ui.parameters != {}:
        config = False 

mode = cfg_ui.selected_mode
quiz_type = cfg_ui.q_type

print(cfg_ui.parameters)

response = requests.get('https://opentdb.com/api.php?',params=cfg_ui.parameters)
response.raise_for_status()

cfg_ui.destroy()

question_data = response.json()['results']

for question in question_data:
    print(question)
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question_incorrect_answers = question["incorrect_answers"]
    new_question = Question(question_text, question_answer,question_incorrect_answers)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

if quiz_type == 'boolean':
    quiz_interface = BoolQuizInterface(quiz)
if quiz_type == 'multiple':
    quiz_interface = MCQuizInterface(quiz)


class Question:

    def __init__(self, q_category, q_text, q_correct_answer,q_incorrect_answers):
        self.category = q_category
        self.text = q_text
        self.correct_answer = q_correct_answer
        self.incorrect_answers = q_incorrect_answers

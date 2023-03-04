import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOUR = "#4D455D"
SAND = '#F5E9CF'
RED = '#E96479'
GREEN = '#7DB9B6'

class BoolQuizInterface:
    def __init__(self,quiz_brain):
        self.quiz = quiz_brain 
        self.window = tk.Tk()
        self.window.title('Quiz Game')
        self.window.configure(bg=THEME_COLOUR,padx=20,pady=20)
        
        self.canvas = tk.Canvas(width=300, height=250,bg=SAND)
        self.q_text = self.canvas.create_text(150,125,text='Test',font=('SF Pro Medium',25,'normal'),width=280)
        self.canvas.grid(column=0,row=2,columnspan=2)
        
        self.score_label = tk.Label(text='Score: 0',bg=THEME_COLOUR,fg='white',font=('SF Pro Bold',25,'normal'))  
        self.score_label.grid(column=1,row=0,pady=10,sticky='E')

        self.number_label = tk.Label(text='Question 1', bg=THEME_COLOUR, fg=SAND,font=('SF Pro Medium',15,'normal'))
        self.number_label.grid(column=0,row=1,columnspan=2,pady=10)
        
        right_img = tk.PhotoImage(file='images/true.png')
        wrong_img = tk.PhotoImage(file='images/false.png') 
        self.button_right = tk.Button(image=right_img,highlightthickness=0,command=self.answer_right)
        self.button_right.grid(column=0,row=3,pady=20)

        self.button_wrong = tk.Button(image=wrong_img,highlightthickness=0,command=self.answer_wrong)
        self.button_wrong.grid(column=1,row=3,pady=20)

        self.get_next_question()
        
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(self.canvas, bg=SAND)
            q_cat, q_text = self.quiz.next_question()
            q_number = self.quiz.question_number 
            self.canvas.itemconfig(self.q_text,text=q_text)
            self.number_label['text'] = f'Question {q_number}:\n {q_cat}'
        else:
            self.canvas.config(bg=SAND)
            self.number_label['text'] = ''
            self.canvas.itemconfig(self.q_text, text='You\'ve reached the end of the questions.')
            self.button_right.config(state='disabled')
            self.button_wrong.config(state='disabled')

    def answer_wrong(self):
        is_right = self.quiz.check_answer('False')
        self.score_label['text'] = f'Score: {self.quiz.score}'
        self.give_feedback(is_right)

    def answer_right(self):
        is_right = self.quiz.check_answer('True')
        self.score_label['text'] = f'Score: {self.quiz.score}'
        self.give_feedback(is_right)        

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg=GREEN)
            self.window.after(1000,self.get_next_question)
        else:
            self.canvas.config(bg=RED)
            self.window.after(1000,self.get_next_question)



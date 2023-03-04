import tkinter as tk
from quiz_brain import QuizBrain
import tkmacosx

THEME_COLOUR = "#4D455D"
SAND = '#F5E9CF'
RED = '#E96479'
GREEN = '#7DB9B6'
BGCOL = '#F5FFC9'


class MCQuizInterface:
    def __init__(self,quiz_brain):
        self.quiz = quiz_brain 
        self.answers = []
        self.window = tk.Tk()
        self.window.title('Quiz Game')
        self.window.configure(bg=THEME_COLOUR,padx=20,pady=20)
        
        self.canvas = tk.Canvas(width=300, height=250,bg=SAND)
        self.q_text = self.canvas.create_text(150,125,text='Test',font=('SF Pro Medium',25,'normal'),width=280)
        self.canvas.grid(column=0,row=2,columnspan=2,pady=(0,10))
        
        self.score_label = tk.Label(text='Score: 0',bg=THEME_COLOUR,fg='white',font=('SF Pro Bold',25,'normal'))  
        self.score_label.grid(column=1,row=0,pady=10,sticky='E')

        self.number_label = tk.Label(text='Question 1', bg=THEME_COLOUR, fg=SAND,font=('SF Pro Medium',15,'normal'))
        self.number_label.grid(column=0,row=1,columnspan=2,pady=10)
        
        self.answer_button1 = tkmacosx.Button(text='1.58 x 10^20', foreground=THEME_COLOUR, bg=BGCOL, borderless=1, highlightthickness=0,font=('SF Pro Bold',15,'normal'),height=40, width=150, command=self.answer1)
        self.answer_button1.grid(column=0,row=3,pady=10)

        self.answer_button2 = tkmacosx.Button(text='1.58 x 10^22',foreground=THEME_COLOUR, bg=BGCOL, borderless=1, highlightthickness=0,font=('SF Pro Bold',15,'normal'),height=40,width=150, command=self.answer2)
        self.answer_button2.grid(column=1,row=3,pady=10)

        self.answer_button3 = tkmacosx.Button(text='1.58 x  10^18',foreground=THEME_COLOUR, bg=BGCOL, borderless=1, highlightthickness=0,font=('SF Pro Bold',15,'normal'),height=40,width=150, command=self.answer3)
        self.answer_button3.grid(column=0,row=4,pady=10)

        self.answer_button4 = tkmacosx.Button(text='1.58 x 10^24',foreground=THEME_COLOUR, bg=BGCOL, borderless=1, highlightthickness=0,font=('SF Pro Bold',15,'normal'),height=40,width=150, command=self.answer4)
        self.answer_button4.grid(column=1,row=4,pady=10)

        self.get_next_question()
        
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(self.canvas, bg=SAND)
            q_cat, q_text = self.quiz.next_question()
            q_number = self.quiz.question_number 
            self.canvas.itemconfig(self.q_text,text=q_text)
            self.number_label['text'] = f'Question {q_number}:\n {q_cat}'

            # set buttons
            self.answers = self.quiz.get_answers()

            self.answer_button1['text'] = self.answers[0]
            self.answer_button2['text'] = self.answers[1]
            self.answer_button3['text'] = self.answers[2]
            self.answer_button4['text'] = self.answers[3]
                
        else:
            self.canvas.config(bg=SAND)
            self.number_label['text'] = ''
            self.canvas.itemconfig(self.q_text, text='You\'ve reached the end of the questions.')
            self.answer_button1.config(state='disabled')
            self.answer_button2.config(state='disabled')
            self.answer_button3.config(state='disabled')
            self.answer_button4.config(state='disabled')

    def answer1(self):
        is_right = self.quiz.check_answer(self.answers[0])
        self.score_label['text'] = f'Score: {self.quiz.score}'
        self.give_feedback(is_right)

    def answer2(self):
        is_right = self.quiz.check_answer(self.answers[1])
        self.score_label['text'] = f'Score: {self.quiz.score}'
        self.give_feedback(is_right)     

    def answer3(self):
        is_right = self.quiz.check_answer(self.answers[2])
        self.score_label['text'] = f'Score: {self.quiz.score}'
        self.give_feedback(is_right)     

    def answer4(self):
        is_right = self.quiz.check_answer(self.answers[3])
        self.score_label['text'] = f'Score: {self.quiz.score}'
        self.give_feedback(is_right)        

    def give_feedback(self, is_right):
        self.window.focus()
        if is_right:
            self.canvas.config(bg=GREEN)
            self.window.after(1000,self.get_next_question)
        else:
            self.canvas.config(bg=RED)
            self.window.after(1000,self.get_next_question)

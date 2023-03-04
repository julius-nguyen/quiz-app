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
     def __init__(self):   
        self.quiz = quiz_brain 
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
        
        # replace tkmacosx with tk on other distros
        self.answer_button1 = tkmacosx.Button(text='1.58 x 10^20', foreground=THEME_COLOUR, bg=BGCOL, borderless=1, highlightthickness=0,font=('SF Pro Bold',15,'normal'),height=40,command=None)
        self.answer_button1.grid(column=0,row=3,pady=10)

        self.answer_button2 = tkmacosx.Button(text='1.58 x 10^22',foreground=THEME_COLOUR, bg=BGCOL, borderless=1, highlightthickness=0,font=('SF Pro Bold',15,'normal'),height=40,command=None)
        self.answer_button2.grid(column=1,row=3,pady=10)

        self.answer_button3 = tkmacosx.Button(text='1.58 x  10^18',foreground=THEME_COLOUR, bg=BGCOL, borderless=1, highlightthickness=0,font=('SF Pro Bold',15,'normal'),height=40,command=None)
        self.answer_button3.grid(column=0,row=4,pady=10)

        self.answer_button4 = tkmacosx.Button(text='1.58 x 10^24',foreground=THEME_COLOUR, bg=BGCOL, borderless=1, highlightthickness=0,font=('SF Pro Bold',15,'normal'),height=40,command=None)
        self.answer_button4.grid(column=1,row=4,pady=10)

        #self.get_next_question()
        
        self.window.mainloop()

import tkinter as tk

THEME_COLOUR = "#4D455D"
SAND = '#F5E9CF'
RED = '#E96479'
GREEN = '#7DB9B6'

categories = {
    'Any':'0',
    'General Knowledge':'9',
    'Entertainment: Books':'10',
    'Entertainment: Film':'11',
    'Entertainment: Music':'12',
    'Entertainment: Musicals & Theatres':'13',
    'Entertainment: Television':'14',
    'Entertainment: Video Games':'15',
    'Entertainment: Board Games':'16',
    'Science & Nature':'17',
    'Science: Computers':'18',
    'Science: Mathematics':'19',
    'Mythology':'20',
    'Sports':'21',
    'Geography':'22',
    'History':'23',
    'Politics':'24',
    'Art':'25',
    'Celebrities':'26',
    'Animals':'27',
    'Vehicles':'28',
    'Entertainment: Comics':'29',
    'Science: Gadgets':'30',
    'Entertainment: Japanese Anime & Manga':'31',
    'Entertainment: Cartoon & Animations':'32',
}

categories_list = list(categories.keys())
difficulty_list = ['easy','medium','hard']
numbers = [i for i in range(1,40) if i % 5 == 0]

class ConfigQuizInterface:
    def __init__(self):
        self.selected_mode = 0 # default value = Any
        self.cat = 'Any' # default value
        self.difficulty_level = 'easy' #default value
        self.n_questions = 5
        self.q_type = 2

        self.window = tk.Tk()
        self.window.title('Quiz Game: Setup the Game')
        self.window.configure(bg=THEME_COLOUR,padx=20,pady=20)
        
        self.title_label = tk.Label(text='Set up the Game and off you go!',bg=THEME_COLOUR,fg=SAND,font=('SF Pro Bold',25,'normal'))
        self.title_label.grid(column=1,row=0,columnspan=3,pady=20)

        self.mode_label = tk.Label(text='Mode',font=('SF Pro Bold',15,'normal'),bg=THEME_COLOUR,fg=SAND)
        self.mode_label.grid(column=0,row=1,sticky='E')

        self.rbtn_state = tk.IntVar()
        self.single_pl_rbtn = tk.Radiobutton(text='Single Player',value=1, variable=self.rbtn_state,command=self.set_player_mode,bg=THEME_COLOUR,fg=SAND)
        self.mult_pl_rbtn = tk.Radiobutton(text='Multiple Player',value=2, variable=self.rbtn_state,command=self.set_player_mode,bg=THEME_COLOUR,fg=SAND)
        
        self.single_pl_rbtn.grid(column=1,row=1)
        self.mult_pl_rbtn.grid(column=2,row=1)

        self.cat_label = tk.Label(text='Select a category',font=('SF Pro Bold',15,'normal'),bg=THEME_COLOUR,fg=SAND)
        self.cat_label.grid(column=0,row=3,sticky='E',pady=5)

        self.type_label = tk.Label(text='Type',font=('SF Pro Bold',15,'normal'),bg=THEME_COLOUR,fg=SAND)
        self.type_label.grid(column=0,row=2,pady=5,sticky='E')

        self.type_rbtn_state = tk.IntVar()
        self.boolean_rbtn = tk.Radiobutton(text='True or False',value=2, variable=self.type_rbtn_state,command=self.set_qtype,bg=THEME_COLOUR,fg=SAND)
        self.mc_rbtn = tk.Radiobutton(text='Multiple Choice',value=4, variable=self.type_rbtn_state,command=self.set_qtype,bg=THEME_COLOUR,fg=SAND)
        self.boolean_rbtn.grid(column=1,row=2,pady=5)
        self.mc_rbtn.grid(column=2,row=2,pady=5)

        self.cat_var = tk.StringVar()
        self.cat_var.set(categories_list[0])
        self.cat_menu = tk.OptionMenu(self.window, self.cat_var, *categories_list,command=self.get_category_selection)
        self.cat_menu.configure(bg=THEME_COLOUR,width=27)
        self.cat_menu.grid(column=1,row=3,pady=5,sticky='S',columnspan=2)

        self.difficulty_label = tk.Label(text='Difficulty',font=('SF Pro Bold',15,'normal'),bg=THEME_COLOUR,fg=SAND)
        self.difficulty_label.grid(column=0,row=4,pady=5,sticky='E')

        self.diff_var = tk.StringVar()
        self.diff_var.set(difficulty_list[0])
        self.diff_menu = tk.OptionMenu(self.window, self.diff_var, *difficulty_list,command=self.get_difficulty_selection)
        self.diff_menu.configure(width=10,bg=THEME_COLOUR)
        self.diff_menu.grid(column=1,row=4,pady=5,columnspan=1)

        self.number_label = tk.Label(text='Number of questions',font=('SF Pro Bold',15,'normal'),bg=THEME_COLOUR,fg=SAND)
        self.number_label.grid(column=0,row=5,pady=5,sticky='E')

        self.n_var = tk.IntVar()
        self.n_var.set(numbers[0])
        self.n_menu = tk.OptionMenu(self.window, self.n_var, *numbers,command=self.get_n_selection)
        self.n_menu.configure(width=10,bg=THEME_COLOUR)
        self.n_menu.grid(column=1,row=5,pady=5,columnspan=1)

        self.finish_setup_btn = tk.Button(text='Finish setup and start game',font=('SF Pro',15,'normal'),bd=0,fg=THEME_COLOUR,highlightbackground=THEME_COLOUR,bg=THEME_COLOUR)
        self.finish_setup_btn.grid(column=1,row=6,sticky='E',columnspan=2,pady=(30,5))

        self.window.mainloop()
    
    def set_player_mode(self):
        self.selected_mode = self.rbtn_state.get()
        print(self.selected_mode)

    def set_qtype(self):
        self.q_type = self.type_rbtn_state.get()

    def get_category_selection(self,choice):
        self.cat = choice
        print(self.cat)

    def get_difficulty_selection(self,choice):
        self.difficulty_level = choice 
        print(self.difficulty_level)

    def get_n_selection(self,choice):
        self.n_questions = self.n_var.get()
        print(self.n_questions)

cfg_ui = ConfigQuizInterface()

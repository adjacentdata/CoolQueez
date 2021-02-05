from tkinter import *
from quiz_backend import Backend
BG_COLOR = "#375362"

class UI:
    def __init__(self, question_bank: Backend):
        self.question_bank = question_bank

        self.root = Tk()
        self.root.title("Who wants to be a Millionare? (Fast Version)")
        self.root.config(padx=15, pady=15, bg=BG_COLOR)

        self.score = Label(text=f"Score: {self.question_bank.score}", bg=BG_COLOR, fg="white")
        self.score.grid(row=0, column=0, sticky=W)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(bg="black", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.q_a_text = self.canvas.create_text(150, 125,text="Which city is the capital of the United States of America? ", font=("Georgia", 12), width=200, fill="white")

        self.choice_A_button = Button(text="A", highlightbackground="blue", command=self.check_Ans_A)
        self.choice_A_button.grid(row=2, column=0, sticky=E+W)
        self.choice_B_button = Button(text="B", highlightbackground="blue",command=self.check_Ans_B )
        self.choice_B_button.grid(row=3, column=0, sticky=E+W)
        self.choice_C_button = Button(text="C", highlightbackground="blue", command=self.check_Ans_C)
        self.choice_C_button.grid(row=2, column=1, sticky=E+W)
        self.choice_D_button = Button(text="D", highlightbackground="blue", command=self.check_Ans_D)
        self.choice_D_button.grid(row=3, column=1, sticky=E+W)

        self.get_Q()

        self.root.mainloop()

    def get_Q(self):
        gameOn = self.question_bank.game_On()
        if (gameOn):
            text = self.question_bank.next_Question()
            self.canvas.itemconfig(self.q_a_text, text=text)
            self.canvas.config(bg="black")
        else:
            self.canvas.itemconfig(self.q_a_text, text="Thank your for playing")

    def check_Ans_A(self):
        isAnswer = self.question_bank.checkAnswer("a", self.question_bank.correct_Answer, self.question_bank.choices)
        if(isAnswer):
            print("correct")
        else:
            print("False")
        self.answer_correspond(isAnswer)

    def check_Ans_B(self):
        isAnswer = self.question_bank.checkAnswer("b", self.question_bank.correct_Answer, self.question_bank.choices)
        if (isAnswer):
            print("correct")
        else:
            print("False")
        self.answer_correspond(isAnswer)

    def check_Ans_C(self):
        isAnswer = self.question_bank.checkAnswer("c", self.question_bank.correct_Answer, self.question_bank.choices)
        if (isAnswer):
            print("correct")
        else:
            print("False")
        self.answer_correspond(isAnswer)

    def check_Ans_D(self):
        isAnswer = self.question_bank.checkAnswer("d", self.question_bank.correct_Answer, self.question_bank.choices)
        if (isAnswer):
            print("Correct")
        else:
            print("False")
        self.answer_correspond(isAnswer)

    def answer_correspond(self, checkedAns: bool):
        if checkedAns:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score.config(text=f"Score: {self.question_bank.score}")
        self.root.after(2000, self.get_Q)


THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain



class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain


        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        #Canvas
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="caca",
                                                     font=("arial", 20, "italic")
                                                     ,width=280)
        self.canvas.grid(column=0, row=1, columnspan=2,pady=20)

        #True button
        true_image = PhotoImage(file="images/true.png")
        self.true = Button(image=true_image, highlightthickness=0, background=THEME_COLOR,
                       borderwidth=0,command=self.true_button)
        self.true.grid(column=0, row=2)

        #False button
        false_image = PhotoImage(file="images/false.png")
        self.false = Button(image=false_image, highlightthickness=0, background=THEME_COLOR,
                            borderwidth=0,command=self.false_button)
        self.false.grid(column=1, row=2)

        #Score label
        self.scorelab = Label(text=f"Score: {self.quiz.score}", highlightthickness=0, background=THEME_COLOR,
                           font=("arial",15,"italic"),fg="white")
        self.scorelab.grid(column=1,row=0)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):

        self.true.config(state='active')
        self.false.config(state='active')

        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.scorelab.config(text=f"Score {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the test")
            self.true.config(state='disabled')
            self.false.config(state='disabled')
            self.canvas.config(bg="white")


    def true_button(self):
        is_right = self.quiz.check_answer('true')
        self.give_feedback(is_right)

    def false_button(self):
        is_right = self.quiz.check_answer('false')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.true.config(state='disabled')
        self.false.config(state='disabled')
        self.window.after(1000, self.get_next_question)
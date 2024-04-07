from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score = 0
        self.score_label = Label(text="Score : 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="White")
        self.question_text = self.canvas.create_text(150, 125, text="This is the question", font=("Arial", 20, "italic")
                                                     , fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        tick_image = PhotoImage(file="images/true.png")
        cross_image = PhotoImage(file="images/false.png")
        self.tick_button = Button(image=tick_image, highlightthickness=0, command=self.check_answer_true)
        self.tick_button.grid(column=0, row=2)
        self.false_button = Button(image=cross_image, highlightthickness=0, command=self.check_answer_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="White")
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
        self.score_label.config(text=f"Score : {self.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz!")
            self.false_button.config(state="disabled")
            self.tick_button.config(state="disabled")

    def check_answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def check_answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="Green")
            self.score += 1
        else:
            self.canvas.config(bg="Red")
        self.canvas.itemconfig(self.question_text, fill="White")
        self.window.after(1000, self.get_next_question)

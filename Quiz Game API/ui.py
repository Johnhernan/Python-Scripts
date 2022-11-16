from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class UI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.current_question = "questionasdfssssss"

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text=f"{self.current_question}",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
            )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.true_picture = PhotoImage(file="./images/true.png")
        self.true_button = Button(
            image=self.true_picture,
            highlightthickness=0,
            command=self.false_check_answer)
        self.true_button.grid(row=2, column=0)

        self.false_picture = PhotoImage(file="./images/false.png")
        self.false_button = Button(
            image=self.false_picture,
            highlightthickness=0,
            command=self.true_check_answer)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've completed the quiz\n"
                                        f"Your final score was: "
                                        f"{self.quiz.score}/{self.quiz.question_number}")

    def true_check_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_check_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, is_true):
        if is_true:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

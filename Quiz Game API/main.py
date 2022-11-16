from question_model import Question
from ui import UI as QuizInterface
from quiz_brain import QuizBrain
import requests

QUIZ_API = "https://opentdb.com/api.php?amount=10&type=boolean"

response = requests.get(QUIZ_API)
response.raise_for_status()
data = response.json()["results"]

question_bank = []
for question in data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_interface = QuizInterface(quiz)
#
# while quiz.still_has_questions():
#     quiz.next_question()


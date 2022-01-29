from question_model import Question
from data import question_data, new_question_data
from quiz_brain import QuizBrain

question_bank_general = []
question_bank_computer = []
for question in question_data:
    question_bank_general.append(Question(question['text'], question['answer']))
for question in new_question_data:
    question_bank_computer.append(Question(question['text'], question['answer']))

choice = input("Do you want general knowledge or computer questions: ")
if choice.lower() == "general":
    quiz = QuizBrain(question_bank_general)
else:
    quiz = QuizBrain(question_bank_computer)

while quiz.still_has_questions():
    quiz.next_question()

print("You completed the quiz!")
print(f'Your final score is: {quiz.score}/{quiz.question_number}, wh4ich is {quiz.score/quiz.question_number * 100}%')
from question_model import Question
from Data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(item['question'], item['correct_answer']) for item in question_data]

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was: {quiz.counter}/{quiz.question_number}")

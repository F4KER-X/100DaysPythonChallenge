class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.counter = 0

    def next_question(self):

        question = self.question_list[self.question_number]
        user_answer = input(f"Q {self.question_number + 1}: {question.text}. 'True / False: ").lower()
        self.question_number += 1
        self.check_answer(user_answer,question.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self,user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.counter += 1
            print("You got it right")
        else:
            print("Wrong answer")
        print(f"The correct answer: {correct_answer}")
        print(f"Score: {self.counter}/{self.question_number}\n")



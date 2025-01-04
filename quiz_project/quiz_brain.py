class Quiz_brain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.choose = ''
        self.correct_answer = ''
        self.score = 0
    def still_has_questions(self):
        return len(self.question_list) > self.question_number
    def next_question(self):
            self.choose = input(f'Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False)?: ').title() 
            self.question_number+=1
    def is_right_answer(self):
        self.correct_answer = self.question_list[self.question_number-1].answer
        if self.choose == self.correct_answer:
            print("good job, you are right!")
            self.score+=1
            print(f"score: {self.score}/{self.question_number}")
        else:
            print("oh wrong answer, try another one!")
            print(f"score: {self.score}/{self.question_number}")



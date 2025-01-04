from data import question_data
from question_model import question
from quiz_brain import Quiz_brain
question_bank = []
for Question in question_data:
    text = Question['text']
    answer = Question['answer']
    question_ob = question(text, answer)
    question_bank.append(question_ob)
quiz = Quiz_brain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    quiz.is_right_answer()



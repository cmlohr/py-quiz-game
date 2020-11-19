from question_model import Question
from data import q_data
from quiz_brain import QuizBrain

print("It's History Quiz Time!")
print("   2020 | @Cmlohr")
q_bank = []
for question in q_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    q_bank.append(new_question)

quiz = QuizBrain(q_bank)

while quiz.still_question():
    quiz.next_question()

print("Quiz complete!")
print(f"Final score was {quiz.score}/{quiz.question_number}")
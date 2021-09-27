from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

# create list of question objects
question_bank = []
for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))
    
# create quiz
quiz_brain = QuizBrain(question_bank)

# run quiz
while quiz_brain.still_has_question():
    quiz_brain.next_question()

print("You've completed the quiz.")
print(f"Your final score was {quiz_brain.score}/{len(quiz_brain.question_list)}")
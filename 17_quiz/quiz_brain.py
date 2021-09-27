class QuizBrain:
    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.question_list = q_list
        
    def next_question(self):
        # TODO asking the questions
        user_answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text}. (True/False)): ").title()
        self.question_number += 1
        self.check_answer(user_answer)

    # Checking if we are at the end of the quiz    
    def still_has_question(self):
        return self.question_number < len(self.question_list)


    def check_answer(self, u_answer):
        if u_answer.lower() == self.question_list[self.question_number-1].answer.lower():
            self.score += 1
            print("You got it right!")
        else: 
            print("That's incorrect.")
        print(f"The correct answe was: {self.question_list[self.question_number-1].answer}")
        print(f"Yor score is {self.score}/{self.question_number}")
        print("\n")
        
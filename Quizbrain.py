class Quizzbrain:
    def __init__(self,qlists) -> None:
        self.q_no = 0
        self.mark = 0
        self.q_list = qlists
        
    def still_questions(self):
        return self.q_no< len(self.q_list)
    def next_question(self):
        current_question = self.q_list[self.q_no]
        self.q_no += 1
        user_answer = input(f"Q.{self.q_no}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.mark += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.mark}/{self.q_no}")
        print("\n")
   
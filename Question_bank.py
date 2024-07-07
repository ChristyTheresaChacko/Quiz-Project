from data import question_data
from questions import Question
from Quizbrain import Quizzbrain

question_bank = []
for que in question_data:
    q_text = que["text"]
    q_ans = que["answer"]
    que = Question(q_text,q_ans)
    question_bank.append(que)

quest = Quizzbrain(question_bank)
while quest.still_questions():
    quest.next_question()
print("Hurray !! You've completed the quiz and your final score is ",quest.mark,"/",quest.q_no)

    
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questionBank=[]
for i in question_data:
    q_text=i["text"]
    q_ans=i["answer"]
    new_question=Question(q_text,q_ans)
    questionBank.append(new_question)

quiz=QuizBrain(questionBank)
while quiz.stillHasQuestions():
    quiz.nextQuestion()

print(f"You have completed the game! Your score is {quiz.score}/{len(questionBank)}")
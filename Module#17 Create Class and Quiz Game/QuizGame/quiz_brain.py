# todo:
# 1 ask ques
# 2 check
# 3 end

class QuizBrain:
    def __init__(self, q_List):
        self.questionNumber=0
        self.questionList = q_List
        self.score=0

    def nextQuestion(self):
        currentQues=self.questionList[self.questionNumber]
        correctAns=currentQues.answer
        self.questionNumber+=1#this will increase the question number in the output and also when we are accessing qustion from the q_list, it will move to next ques or else it would be printing same ques from the same index of the list
        userAns=input(f"Q.{self.questionNumber}: {currentQues.text} (True/False) ")
        self.checkAns(userAns,correctAns)

    def stillHasQuestions(self):
        if self.questionNumber < len(self.questionList):
            return True
        else:
            return False

    def checkAns (self,userAns,correctAns):
        if userAns.lower() == correctAns.lower():
            score+=1
            print("You got it right!")
        else:
            print("Wrong answer!")
        print(f"Correct Answer: {correctAns}")
        print(f"Your Current Score is: {self.score}/{self.questionNumber}\n")
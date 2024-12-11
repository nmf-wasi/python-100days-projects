from art import logo
from random  import randint
easyLevel = 10
mediumLevel = 7
hardLevel = 5
attempts = 0

def compare(ans, userGuess):
    if(userGuess>ans):
        print("Too high!")
    elif(userGuess<ans):
        print("Too low!")
    elif(userGuess==ans):
        print("Congrats!")

def game():
    if(lvl==1):
        steps = easyLevel
    elif(lvl==2):
        steps = mediumLevel
    elif(lvl==3):
        steps = hardLevel
    userGuess=int(input("Please enter your guess: "))
    global attempts
    attempts+=1
    if(userGuess==answer):
        print(f"Yayy! You have guess the correct number in {attempts} attempts")
        global gameOver
        gameOver=True
    elif (steps - attempts!=0):
        compare(answer, userGuess)
        print(f"Wrong answer! You have tried {attempts} attempts. You have {steps-attempts} attempts left to try.")
    else:
        gameOver=True
        print(f"GAME OVER! You have tried {attempts} attempts. You have {steps-attempts} attempts left to try. Answer was: {answer} ")


# Program starts from here
print(logo)
gameOver = False
print("Welcome to the Number Guessing Game!")
command =input("Do you want to play number guessing game? Press 'y' to play : ")
start=int(input("Write the range you want to start from: "))
end=int(input("Write the range you want to start from: "))
answer = randint(start, end+1)
if(command.lower()=='y'):
    lvl = int(input("Please choose difficulty level. Press '1' for Easy level and '2' for Medium Level and '3' for Hard Level : "))
    print(f"I'm thinking of a number between {start} and {end}.")
    while(gameOver==False):
        game()

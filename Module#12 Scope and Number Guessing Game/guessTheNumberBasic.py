from art import logo
from random  import randint
easyLevel = 10
mediumLevel = 7
hardLevel = 5
attempts = 0

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
    elif (steps - attempts!=0):
        print(f"Wrong answer! You have tried {attempts} attempts. You have {steps-attempts} attempts left to try!")
    else:
        global gameOver
        gameOver=True
        print(f"GAME OVER! You have tried {attempts} attempts. You have {steps-attempts} attempts left to try!")


print(logo)
gameOver = False
print("Welcome to the Number Guessing Game!")
command =input("Do you want to play number guessing game? Press 'y' to play :")
if(command.lower()=='y'):
    answer = randint(1, 100)
    lvl = int(input("Please choose difficulty level. Press 1 for Easy level and 2 for Medium Level and 3 for Hard Level : "))
    print("I'm thinking of a number between 1 and 100.")
    while(gameOver==False):
        game()

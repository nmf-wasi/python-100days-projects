import random
from art import logo
from art import vs
from gameData import data
def pickID():
    return random.choice(data)

def formatText(user):
    name=user["name"]
    des = user["description"]
    country = user["country"]
    return(f"{name}, a {des} from {country}")

def follower(user):
    return user["follower_count"]

optionA=pickID()
optionB=pickID()
gameOver=False
point=0

def game(optionA, optionB,userGuess):
    if(follower(optionA)>follower(optionB)):
        ans='A'
    elif(follower(optionA)<follower(optionB)):
        ans='B'
    if(userGuess.upper()==ans):
        global point
        point+=1
        print(f"You guessed it right! Your point is :{point}")
    else:
        global gameOver
        gameOver=True
        print(f"Game Over! You guessed it wrong. Your Point is: {point}")


print(logo)
command=input("Do you want to play Higher Lower Game? Press 'Y' to start the game ")
# print(optionA)
# print(optionB)
if(command.lower()=='y'):
    while gameOver==False:
        print(f"A. {formatText(optionA)}")
        print(vs)
        print(f"B. {formatText(optionB)}")
        userGuess = input("Who has higher number of instagram followers? Select 'A' or 'B': " )
        game(optionA, optionB, userGuess)
        if(gameOver==True):
            break
        else:
            cont=input("Do you want to continue? Press 'Y' to Continue and 'N' to exit the game " )
            if cont.upper()=='Y':
                optionA=optionB
                optionB=pickID()
            else:
                gameOver = True
                print(f"Your Point is: {point}")

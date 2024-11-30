rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import sys  # Import sys module to use sys.exit()
print("Welcome to Rock Paper Scissors Game!")
hooman_option_choice=int(input("Select 0 for Rock, 1 for Paper and 2 for Scissors\n"))
if(hooman_option_choice<0 or hooman_option_choice>2):
    print("Invalid choice! Program will terminate.")
    sys.exit()  # Terminate the program if choice is not 1, 2, or 3
import random
com_option_choice=random.randint(0,2)

options=["rock","paper","scissors"]

hooman_choice=options[hooman_option_choice]
com_choice=options[com_option_choice]
#if you use options 1to3, you have to minus 1 from the index or it will go out of range

designs=[rock,paper,scissors]
hooman_art=designs[hooman_option_choice]
com_art=designs[com_option_choice]

print(f"You chose {hooman_choice}")
print(hooman_art)
print(f"Computer chose {com_choice}")
print(com_art)

if(hooman_choice==com_choice):
    print("It's a Draw!")
elif((hooman_choice=="paper" and com_choice=="rock") or (hooman_choice=="rock" and com_choice=="scissors") or (hooman_choice=="scissors" and com_choice=="paper")):
    print("You win!")
else:
    print("Computer wins!")
# elif(hooman_choice=="rock" and com_choice=="paper"):
#     print("You win!")
# elif(hooman_choice=="paper" and com_choice=="rock"):
#     print("Computer wins!")

# elif(hooman_choice=="scissors" and com_choice=="paper"):
#     print("Computer wins!")
# elif(hooman_choice=="paper" and com_choice=="scissors"):
#     print("You win!")

# elif(hooman_choice=="rock" and com_choice=="scissors"):
#     print("You win!")
# elif(hooman_choice=="scissors" and com_choice=="rock"):
#     print("Computer wins!")


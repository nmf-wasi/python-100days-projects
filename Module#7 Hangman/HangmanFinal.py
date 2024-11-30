# word_list = ["aardvark", "baboon", "camel"]
import hangman_words
import random
import hangman_art
print(hangman_art.logo)
chosenWord=random.choice(hangman_words.word_list)
display=[]
lives=6
wordLength=len(chosenWord)
for i in range(wordLength):
    display+='_'
endOfGame=False
while(endOfGame==False):
    guess=input("Guess a letter: ")
    guess=guess.lower()
    if(guess in display):
        print(f"You have already guessed {guess}")
    # print(f'Pssst, the solution is {chosenWord}.')
    for i in range(wordLength):
        if(guess==chosenWord[i]):
            display[i]=guess
    if(guess not in chosenWord):
        lives-=1
        print(f"You guessed {guess} and it's not in the word. You lose a life. Lives remaining : {lives}")
    print(display)
    if(lives==0):
        print("You Lose!")
        endOfGame=True
    print(hangman_art.stages[lives])
    if '_' not in display:
        endOfGame=True
        print("Yay! You Completed the game!")
# ideal practice is to keep the import on top then keep the functions and then keep the global variables
import os

def clear_screen():
    if os.name == "nt":  # For Windows
        os.system("cls")
    else:  # For Mac and Linux
        os.system("clear")

from art import logo

import random
def deal_card():
    """randomly return a card and k,q,j are counted as 10 and ACE is initially 11"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """will return the total sum of cards of user or computer"""
    # blackjack only happens on a hand with only 2 cards (ace+10)=21 and return 0 instead of the actual score. 0 will represent a blackjack in our game

    # if 11 in cards and 10 in cards and len(cards)==2:
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score>21 and computer_score>21:
        return "You went over, you lose 🤷‍♂️"
    if computer_score == user_score:
        return "Draw 😐"
    elif computer_score == 0:
        return "Lose, opponent has a BlackJack 🤦‍♂️"
    elif user_score == 0:
        return "Win with a BlackJack 😎"
    elif user_score > 21:
        return "You went over, you lose 🤷‍♂️"
    elif computer_score > 21:
        return "Win, opponent went over 😆"
    elif user_score > computer_score:
        return "You win 🎉"
    elif user_score < computer_score:
        return "You lose, opponent wins 😩"


def playGame():
    print(logo)
    user_cards = []
    computer_cards = []
    gameOver = False

    for n in range(2):
        new_user_card = deal_card()
        user_cards.append(new_user_card)
        new_computer_card = deal_card()
        computer_cards.append(new_computer_card)

    while not gameOver:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards are : {user_cards} and your current score is : {user_score}")
        print(f"Computer's first card : {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            gameOver = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass\n")
            if user_should_deal.lower() == "y":
                user_cards.append(deal_card())
            else:
                gameOver = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while(input("Do you want to play a game of BlackJack? Type 'y' to play ").lower()=='y'):
    clear_screen()
    playGame()
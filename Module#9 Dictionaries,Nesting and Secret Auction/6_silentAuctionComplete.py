logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
import os
def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Mac and Linux
        os.system('clear')
print(logo)
bids = {}
def highestBid(biddingList):
    maxBid=0
    winner=""
    for bidder in biddingList:
        if maxBid < biddingList[bidder]:
            maxBid=biddingList[bidder]
            winner=bidder
    print(f"The winner is {winner} with a bid of ${maxBid}")

auctionOngoing=True
while(auctionOngoing):
    name = input("What's your name? ")
    price = input("What's your bid? $")
    bids[name] = int(price)#input are by default strings, convert it to int
    continuation=input("Are there any other bidders? Type 'yes' or 'no .'\n") 
    continuation=continuation.lower()
    if(continuation=='no'):
        auctionOngoing=False
        highestBid(bids)
    else:
        clear_screen()

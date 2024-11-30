import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to Password Generator!")
nletters=random.randint(1,50)
nsymbols=random.randint(1,50)
nnumbers=random.randint(1,50)
password=""
for Lia in range(1,nletters+1):
    password+=random.choice(letters)
for Lia in range(1,nsymbols+1):
    password+=random.choice(symbols)
for Lia in range(1,nnumbers+1):
    password+=random.choice(numbers)
print(f"Your password is {password}\nRun again the program to generate another random password")
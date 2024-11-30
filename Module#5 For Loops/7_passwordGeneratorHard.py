#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

passwordList=[]
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# allchars=letters+symbols+numbers
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# totalChar=nr_letters+nr_numbers+nr_symbols

for Lia in range(1,nr_letters+1):
    passwordList+=random.choice(letters)
    # can use append funtion as well
    # passwordList.append(random.choice(letters))
for Lia in range(1,nr_symbols+1):
    passwordList+=random.choice(symbols)
for Lia in range(1,nr_numbers+1):
    passwordList+=random.choice(numbers)
# print(passwordList)
random.shuffle(passwordList)
# print(passwordList)
password=""
for Lia in passwordList:
    password+=Lia
print(f"Your password is "+password)
# print(f"Your password is {password}")


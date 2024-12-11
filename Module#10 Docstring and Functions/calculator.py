import os
def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Mac and Linux
        os.system('clear')
from art import logo
print (logo)

def addition(n1,n2):
    return n1+n2

def substraction(n1,n2):
    return n1-n2

def multiplication(n1,n2):
    return n1*n2

def division(n1,n2):
    return n1/n2
operations={
    "+":addition,
    "-":substraction,
    "*":multiplication,
    "/":division
}

num1 = float(input("What's the first number?: "))
continuation=True
for smb in operations:
        print(smb)

while continuation:
    operator = input("Select an operation from above to continue ")
    # if(operation!='+' or operation!='-' or operation!='*' or operation!='*'):
    #     print("Please select a valid operator to proceed")
    num2 = float(input("What's the second number?: "))
    calculation = operations[operator]
    ans=calculation(num1,num2)
    print(f"{num1} {operator} {num2} = {ans}\n")
    cont = input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation: ")
    if(cont=='y'):
        num1 = ans
    else:
        continuation=False
        clear_screen()

# //tip calculator
print("Welcome to The Tip Calculator!\n")
bill=float(input("What's your total bill?\n"))
tip=float(input("How much do you wanna pay as tip?[enter percent]\n"))
people=int(input("How many people are paying the bill?\n"))
totalTip=float(bill*(tip/100))
totalBill=float(bill+totalTip)
x=float(totalBill/people)
print(f"Each people should be paying {round(x,2)}")
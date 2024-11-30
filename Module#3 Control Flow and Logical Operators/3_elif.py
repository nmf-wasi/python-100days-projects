print("Welcome to Yamagi Art Club")
age=int(input("Enter your age to proceed\n"))
if age>12:
    height=int(input("Enter your height in cm to proceed to payment\n"))
    if height<=110:
        print("Please pay $18\n")
    elif height<=120:
        print("Please pay $20\n")
    elif height<=130:
        print("Please pay $25\n")
    else:
        print("Please pay $30")
else:
    print("Sorry Kiddo, you need to grow up to enter\n")
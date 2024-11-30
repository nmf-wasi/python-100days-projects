year=int(input("Enter a year to check if it's new year or not\n"))
if year%4!=0:
    print(f"{year} is not a leap year")
else:
    if year%100!=0:
        print(f"{year} is a leap year")
    else:
        if year%400==0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
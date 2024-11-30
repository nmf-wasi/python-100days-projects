# Write your code below this line 👇
def prime_checker(number):
  flag=True
  for i in range(2,(number+1)//2):
    if(number%i==0):
      flag=False
  if(flag==True):
    print(f"It's a prime number.")
  else:
    print(f"It's not a prime number.")

# num/2=returns a float
# num//2 returns a int


# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)
# https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/e806e25c-5f84-4d7c-9c7c-2c0fcd0bfe84?sl=%225a6962c9-0e42-448b-b7df-0616c6d30431%22&st=%22SEfB5kQTLxCzgxd1DdyJRDPpY9Rp1HhB%22
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
position=position.upper()
if(position[0]=='A'):
  if(position[1]=='1'):
    line1[0]='X'
  elif(position[1]=='2'):
    line2[0]='X'
  elif(position[1]=='3'):
    line3[0]='X'
elif(position[0]=='B'):
  if(position[1]=='1'):
    line1[1]='X'
  elif(position[1]=='2'):
    line2[1]='X'
  elif(position[1]=='3'):
    line3[1]='X'
elif(position[0]=='C'):
  if(position[1]=='1'):
    line1[2]='X'
  elif(position[1]=='2'):
    line2[2]='X'
  elif(position[1]=='3'):
    line3[2]='X'
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")



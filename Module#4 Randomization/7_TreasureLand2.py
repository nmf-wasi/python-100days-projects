# https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/e806e25c-5f84-4d7c-9c7c-2c0fcd0bfe84?sl=%225a6962c9-0e42-448b-b7df-0616c6d30431%22&st=%22SEfB5kQTLxCzgxd1DdyJRDPpY9Rp1HhB%22
#use own recording for this
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
position=position.upper()
letter=position[0]
#input's first character is letter
number=position[1]
#input's second character is letter
possible_letters=['A','B',"C"]
letter_index=possible_letters.index(letter) 
#will find out which of the possible letters are there
number_index=int(position[1])-1
map=[number_index][letter_index]="X"



# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")



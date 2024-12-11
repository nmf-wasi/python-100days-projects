############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20: #range(1,20) never actually reaches 20 it reaches upto 19 and end
#       print("You got it")
# my_function()

# # # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# # dice_num = randint(1, 6)
# dice_num = randint(1, 5)
# # //randint return any int from 1 to 6, including 6!
# # Therefore, can't use 6 here. Just use 5 since the max index of the list is 5
# print(dice_imgs[dice_num])

# Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# # what if year==1994??
# elif year > 1994:
#   print("You are a Gen Z.")

# Fix the Errors
# age = input("How old are you?") #inputs are always string, make it int to compare
# if age > 18:
#   print("You can drive at age {age}.") #need to add f to make it fstring

# # #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)


# # #Use a Debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     #   b_list.append(new_item)
#     print(b_list)


# mutate([1, 2, 3, 5, 8, 13])

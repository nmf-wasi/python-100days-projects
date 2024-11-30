import random
random_integer = random.randint(1, 10)
print(random_integer)
randomFloat=random.random()
# random.random() func returns a random number from 0 to 0.9999999
# what if we need a random number from 0-5[not including 5]?
# we can multiply it by 5, right?

print(randomFloat)
print(randomFloat*5)


lovescore=random.randint(1,100)
print(f"Your love score is {lovescore}")
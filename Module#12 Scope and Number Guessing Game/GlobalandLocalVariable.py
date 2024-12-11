enemies = 1  # global variable
print(enemies)  # accessing global variable in global position

# while delcaring a global variable, try to make it upper_case. (eg: PIE, TWITTER_ID PASSWORD)

def enemyCount():
    print(f"initial:{enemies}")
    # accessing global variable inside a fucntion


enemyCount()


def enemyCountIncrease():
    global enemies
    enemies += 1
    # modifying a global variable inside a function isn't allowed
    print(f"Enemies inside function after declaring 'global': {enemies}")


enemyCountIncrease()


def enemyIncrease():
    # enemies += 1 isn't allowed because it's still a global variable
    enemies = 4
    # here we arent modifying a global variable inside a function
    # we are creating a new varibale inside the function with the same name and assigning values and it will be printed as well inside this function
    print(f"Enemies inside function after creating a new variable: {enemies}")


enemyIncrease()
print(f"Enemies outside fucntion after creating a new variable: {enemies}")

# best practice is to return from a function instead of modifying a global varible inside a function
# here's how you can do that


def enemyCountIncrease2():
    return enemies + 2


enemies = enemyCountIncrease2()
print(f"Enemies after returning from function: {enemies} ")

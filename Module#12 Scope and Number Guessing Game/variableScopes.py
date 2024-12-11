enemies = 1  # global variable

def enemyCountIncrease():
    global enemies
    enemies += 1
    # modifying a global variable inside a function isn't allowed
    print(f"Enemies inside function after declaring 'global': {enemies}")


enemyCountIncrease()

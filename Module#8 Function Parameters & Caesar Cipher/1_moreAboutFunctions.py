def greet():
    print(f"Good Aftieee")
    print(f"How's it going, man?")
    print(f"Seeyaa")

greet()

def greet_with_name(Yuna):
    print(f"Hi {Yuna}, wanna go shopping?")
    print(f"{Yuna}, do you mind trying some jeans?")

greet_with_name("Wasi")

def greetMultiplePeople(name1, name2):
    print(f"Hi {name1}, wanna go shopping?")
    print(f"{name2}, do you mind trying some jeans?")

greetMultiplePeople("Wasi","Yuna")
greetMultiplePeople(name1="Wasi",name2="Yuna")
greetMultiplePeople(name2="Yuna",name1="Wasi")
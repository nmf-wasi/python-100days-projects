class animal:
    def __init__(self):
        self.eyes=2
    def breathe(self):
        print("inhale,exhale")

class fish(animal):
    def __init__(self):
        super().__init__() #will initialize the class which is written inside fish()
    def swim(self):
        print("rep row")
    def breathe(self): #can modify a function which is already declared in the parent fucntion as well
        print("Underwater breathing")


nemo=animal()
nemo.breathe()
nemo=fish()
nemo.breathe()

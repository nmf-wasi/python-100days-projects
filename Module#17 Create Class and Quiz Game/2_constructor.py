#  We can make a constructer where we wouldn't need to write every single attribute name to assign values in n object.
# # We will use a constructor(__init__) and just pass the value to that constructor and what will create the objects for us
class Student:
    def __init__(self):
        print("new user found!")


student1=Student()
student1.id='1001'
student1.userName="Wasi"
print(student1.userName)





class Student:
    def __init__(self):
        print("new user found!")
class Student:
    def __init__(self, name, id, roll, section):
        self.id=id
        self.username=name
        self.roll=0 # if someone doesn't fillup this attribute, this will be set to 0
        self.sec=section


student1=Student("Wasi",1001,1,"Lions")
student2=Student("Lia",1003,5,"Tigers")
print(f"Name: {student1.username} Roll: {student1.roll} ID: {student1.id} Section: {student1.sec}")
print(f"Name: {student2.username} Roll: {student2.roll} ID: {student2.id} Section: {student2.sec}")






























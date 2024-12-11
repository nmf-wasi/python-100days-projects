class Student:#Class name should be PascalCase
    #PascalCase->ClassName #camelCase #snake_case #Title Case
    pass #will allow users not to put anything inside a class
student1=Student()
student2=Student()
# student# is object, Student is class


student1.name="Wasi" #even though we didnt set any attributes inside the class, it will still work, unlike C++
print(student1.name)

# We can make a constructer where we wouldn't need to write every single attribute name to assign values in n object.
# # We will use a constructor(__init__) and just pass the value to that constructor and what will create the objects for us

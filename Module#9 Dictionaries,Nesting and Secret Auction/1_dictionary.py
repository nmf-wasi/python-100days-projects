# syntax:
#     {key:value}
#     {"Key":"A thing which helps to open doors",
        # "Key":"A thing which helps to open doors",
        # "Key":"A thing which helps to open doors"}
programming_dictionary={
    "Bug":"An error in a program that prevents the program from running as expected",
    "Function":"A piece of code that you can easily can call over and over again",
}
print(programming_dictionary["Bug"])
How to retrive items from a dictionary?
syntax: dictionaryName["key"]

Adding new items to dictionary:
syntax: dictionaryName["NewKey"]="Value"


print whole dictionary:
    syntax: print(dictionaryname)

empty_dictionary={}
empty_dictionary["Key"]="Value"

wipe an existing dictinary:
programming_dictionary={
    "Bug":"An error in a program that prevents the program from running as expected",
    "Function":"A piece of code that you can easily can call over and over again",
}
programming_dictionary={} #now, there's nothing in the dictionary

# changing value of an existing key
programming_dictionary={
    "Bug":"An error in a program that prevents the program from running as expected",
    "Function":"A piece of code that you can easily can call over and over again",
}
programming_dictionary["Bug"]={"Home addressof nmf_wasi"}

#loop through a dictionary
for thing in programming_dictionary:
    print(thing) #the keys will be printed
    print(programming_dictionary[thing]) #the values will be printed



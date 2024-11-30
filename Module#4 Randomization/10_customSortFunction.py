def condition(i):
    return abs(i-90)


list1=[100,90,70,80,50,30,20]
list1.sort(key=condition)
print(list1)
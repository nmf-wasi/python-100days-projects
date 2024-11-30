# functions of list
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

myMembers=["Yuna","Wasi","Yeji","Lia","Ryu","Chaer","Yuwi"]
print(myMembers)#will show the list
# append()	Adds an element at the end of the list
newMemebers="Yuqi","Minnie","Micky"
myMembers.append(newMemebers)
# //append func will add brackets inside the appended list, to avoid the brackets, use extend or appened one by one
print(myMembers)#will show the list
myMembers.append("Liam")
print(myMembers)#will show the list

# clear()	Removes all the elements from the list
myMembers.clear()
print(myMembers)#will show the list

myMembers=["Yuna","Wasi","Yeji","Lia","Ryu","Chaer","Yuwi"]

# copy()	Returns a copy of the list
x=myMembers.copy()
print(x)

#count()	Return the number of times the value "x" appears in the fruits list
myMembers.append('Yuna')
print(myMembers)
print(myMembers.count("Yuna"))

# extend()	Add the elements of a list (or any iterable), to the end of the current list //this will not brackets
listOne=["werwsea","ewqrb",'asd','dasd']
listTwo=["asewrwewerwsea","werweewqrb",'ashjhjk6uyih,md','ryetrjdasd']
listOne.extend(listTwo)
print(listOne)

# index()	Returns the index of the first element with the specified value
a=["123", "456", "789", "147", "258", "369", "123," "459", "687"]
print(a.index("123"))
# print(a.index("113")) #if the value isnt present, it will give value error

# insert()	Adds an element at the specified position
Lia=['a','b','c','c',"d"]
Lia.insert(1,'e')
print(Lia)
# pop()	Removes the element at the specified position
Lia.pop()
print(Lia)

#remove() -> removes the first occurrence of the element with the specified value
Lia.remove('c')
print(Lia)

# reverse()	Reverses the order of the list
Lia.reverse()
print(Lia)

# sort()	Sorts the list
names=['Wasi','Yuna','Yeji','Lia','Chaer','Ryu']
names.sort()
print(names)

#len func returns the number of elements of a list as well
print(f"The length of the list 'name' is : {len(names)}")
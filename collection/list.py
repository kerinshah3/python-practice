# List

list_of_int = [1,2,3,5,7,10,90]

for x in list_of_int:
    print(x)

# Common methods in List

#append :- Adds single element
list_of_int.append(10)
print("after appends")
for x in list_of_int:
    print(x)

#extends :- Adds single or list of elements to existing list
list_of_int.extend([9,10,80,18])

print("after extends")
for x in list_of_int:
    print(x)

#pop :- Removes last element or Removes specified index element
list_of_int.pop()
print("after popping last index")
for x in list_of_int:
    print(x)


list_of_int.pop(3)
print("after popping 4th element index")
for x in list_of_int:
    print(x)



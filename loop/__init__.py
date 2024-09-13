from functions import *

name = input("NAME: ")

age = get_age()

# Infinite Loop with While
# while age != 0:
#     print("Something")

# Infinite loop to get correct input of age with else which is new in python
while age <= 0:
    print("Age cannot be less than or equal 0")
    age = get_age()
else:
    print("Age passed validation")

# Normal for each loop it will iterate through each element of String/Collection
for n in name:
    print(n)

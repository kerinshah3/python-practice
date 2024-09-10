name = input("NAME: ")

age = input("AGE: ")

print(int(age) - 10)

age = int(age)

#Condtional Statement
if name == 'Kerin':
    print("Kerin is learning python")

# Chained Conditional Statement
if name == 'Kerin' or name == 'Kerin Shah':
    print("Kerin Shah is learning python")



if age < 10:
    print("Age is less than 10")
elif age < 20:
    print("Age is less than 20")
else:
    print("Age is Greater than 20")
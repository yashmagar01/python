# Differentiate between if-else and nested-if statement about different Logical operators in Python with appropriate examples. 

a = int(input("Enter number 1: ")) 
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))

if a >= b:
    if a >= c:
        print(f"{a} is grater..")
    else:
        print(f"{c} is grater..")
else:
    if b >= c:
        print(f"{b} is grater..")
    else:
        print(f"{c} is grater")
# Write a python program to find Factorial of given number. 

num = int(input("Enter a integer: "))
fact = 1

if num < 0:
    print("Factorial does not exist for negative numbers")
else:
    for i in range(1, (num + 1)):
        fact = fact * i
    print(f"Factrial of {num} is {fact}")
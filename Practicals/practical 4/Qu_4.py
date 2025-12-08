#  Write a program to check if a Number is Positive, Negative or Zero

num = int(input("Enter a integer: "))

if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f"{num} is negative")
elif num == 0:
    print(f"{num} is zero")
else:
    print("plz Enter a valid integer")
# Write a python program to find Fibonacci series for given number. 

n = int(input("How many terms? "))

a = 0
b = 1

if n <= 0:
    print("Enter a positive number")
elif n == 1:
    print(a)
else:
    print(a, b, end=" ")
    for i in range(3, n+1):
        c = a + b
        print(c, end=" ")
        a = b
        b = c

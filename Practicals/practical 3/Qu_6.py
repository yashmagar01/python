# Write a program to swap the value of two variables.

a = int(input("Enter first_num : "))
b = int(input("Enter second_num : "))

print("Before Swap: First_num = ", a, " Second_num = ", b )

temp = a
a = b
b = a

print("After Swap: First_num = ", a, " Second_num = ", b)



# Write a Python program that takes a number and checks whether it is a palindrome or not.

number = int(input("Enter a integer: "))
temp = number
reminder = 0
reverse = 0

while(temp != 0):
    reminder = temp % 10
    reverse = reverse * 10 + reminder
    temp = temp // 10
    
if number == reverse:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
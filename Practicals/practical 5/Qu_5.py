# Write a Python Program to Reverse a given number. 

number = int(input("Enter a number: "))
temp = number
reminder = 0
reverse = 0

while(temp != 0):
    reminder = temp % 10
    reverse = reverse * 10 + reminder
    temp = temp // 10

print(f"Original number: {number}\nreversed number: {reverse}")
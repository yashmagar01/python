# Find sum of four-digit number.

num = int(input("Enter a four digit number: "))
temp = num
reminder = 0
result = 0

while temp != 0:
    reminder = temp % 10
    result = result + reminder
    temp = temp // 10

print(f"Addition of {num} is: {result}")
# Print the number in words for Example: 1234 => One Two Three Four

digits = ('zero','one','two','three','four','five','six','seven','eight','nine')

a = int(input("Enter a number: "))
temp = a
mylist = []

while temp != 0:
    reminder = temp % 10
    mylist.append(digits[reminder])
    temp = temp // 10

mylist.reverse()

for word in mylist:
    print(word, end=" ")
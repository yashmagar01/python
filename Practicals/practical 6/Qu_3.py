# Write program to demonstrate use of nested if-else.

# I used nested if-else to get the highes number among three

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a > b:
    if a > c:
        print(f"\n{a} is grater..")
    else:
        print(f"\n{c} is grater..")
elif b > a:
    if b > c:
        print(f"\n{b} is grater..")
    else:
        print(f"{c} is grater..")
else:
    print("Enter a integer..")
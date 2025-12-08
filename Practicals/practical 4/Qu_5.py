#  Write a program that takes the marks of 5 subjects and displays the grades.
print("Enter marks out of 100: --")
sub1 = float(input("Enter marks of subject 1: "))
sub2 = float(input("Enter marks of subject 2: "))
sub3 = float(input("Enter marks of subject 3: "))
sub4 = float(input("Enter marks of subject 4: "))
sub5 = float(input("Enter marks of subject 5: "))

avg = (sub1 + sub2 + sub3 + sub4 + sub5) / 5

print(f"\nYour avarage is: {avg}")

if avg >= 85 and avg <= 100:
    print("Grade: A")
elif avg >= 60 and avg <= 84:
    print("Grade: B")
elif avg >= 45 and avg <= 69:
    print("Grade: C")
elif avg < 45:
    print("Grade: Fail")
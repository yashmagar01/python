# Write a program that takes the marks of 5 subjects and displays the grades.

total_marks = 0
total_subject = 5

# Taking input
print("Enter marks of 5 subjects: ")
for i in range(1,6):
    marks = int(input(f"Enter marks of sub. {i}: "))
    total_marks += marks

# Calculating avg
avg = total_marks / total_subject
print("Total Marks u got: ", total_marks)

if avg <= 100 and avg >= 75:
    print("\nGrade: A")
elif avg < 75 and avg >= 60:
    print("\nGrade: B")
elif avg < 60 and avg >= 40:
    print("\nGrade: C")
else:
    print("\nGrade: D")
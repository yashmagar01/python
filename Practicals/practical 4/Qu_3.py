# Write a program to check if the input year is a leap year of not
 
year = int(input("Enter a year: "))

if year % 4 == 0 or year % 400 == 0:
    print(f"the year {year} is a leap year.")
else:
    print(f"the year {year} is not a leap year.")
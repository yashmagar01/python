# Write a Python program to find the repeated items of a tuple.

one = (15, 60, 20, 45)
two = (20, 80, 60, 40)

print("First Tuple: ", one, "\nSecond Tuple: ", two)

common = list(set(one) & set(two))
print("Common Elements: ", common)

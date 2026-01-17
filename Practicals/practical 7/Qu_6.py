#  Write a Python program to find common items from two lists.

list1 = [12,24,36,48,60]
list2 = [6,12,18,24,30,36,42,48]

common = list(set(list1) & set(list2))

print(f"List 1 = {list1}")
print(f"List 2 = {list2}")
print(f"\nCommon elements: {common}")
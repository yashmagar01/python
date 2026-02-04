# Write a Python program to find common items from two lists.

list1 = [8,16,24,36,32,40,48,54,64,72,80]
list2 = [16,32,48,64,80]
print(f"List 1 = {list1}")
print(f"List 2 = {list2}")
list1.sort(reverse=True)
print(list1)
common = list(set(list1) & set(list2))

print(f"\nCommon Elements: {common}")
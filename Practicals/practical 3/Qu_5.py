# Write a program to convert bits to Megabytes, Gigabytes and Terabytes.

bits = int(input("Enter bits: "))
bytes_ = bits / 8
kb = bytes_ / 1024

mb = kb / 1024
gb = mb / 1024
tb = gb / 1024

print(f"{bits} is equal to {mb} MB")
print(f"{bits} is equal to {gb} GB")
print(f"{bits} is equal to {tb} TB")
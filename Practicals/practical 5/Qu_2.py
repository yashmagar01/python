# Write  a  Python  program  to  print  all  even  numbers  between  1  to  100  using  while loop.

print("----- All even numbers between 1 to 100 -----\n") 

print("Method - 1: by using range(start, stop, update)\n")
for i in range(2, 100, 2):
    print(f"{i} ")
    
print("\nmethod - 2: by using conditional statements")
for i in range(1,100):
    if i % 2 == 0:
        print(f"{i} ")
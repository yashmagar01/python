"""
Print the following patterns using loop: 
a. 
    1010101   
    10101     
    101       
    1  
"""
s = "1010101"

for i in range(7,0,-2):
    print(s[:i])
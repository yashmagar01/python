# check is number is prime or not?

n = int(input("Enter n: "))

if n <= 1:
    print(f"{n} is not a prime number")
else:
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is a composite number")
            break
        else:
            print(f"{n} is a prime number")
            break

# Print the number in words for Example: 1234 => One Two Three Four

a = (input("Enter a number: "))

for i in a:
    match a:
        case 1:
            print("One")
            break
        case 2:
            print("Two")
            break
        case 3:
            print("Three")
            break
        case 4:
            print("Four")
            break
        case 5:
            print("Five")
            break
        case 6:
            print("Six")
            break
        case 7:
            print("Seven")
            break
        case 8:
            print("Eight")
            break
        case 9:
            print("Nine")
            break
        case 0:
            print("Zero")
            break
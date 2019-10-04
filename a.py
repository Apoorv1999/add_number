while True:
    try:
        a = input("Enter no.1: \n")
        a = int(a)

        b = input("Enter no.2: \n")
        b = int(b)
        break

    except:
        print("Please enter a number")

print("The sum is:")
print(a+b)

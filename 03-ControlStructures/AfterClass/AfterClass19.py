x = int(input("Enter the dog's age in human years: "))

if x-2 > 0:
    y = int(2*10.5+(x-2)*4)
    print(f"The dog's age in dog's years is {y} years.")
elif x-2 == 0:
    y = int(2*10.5)
    print(f"The dog's age in dog's years is {y} years.")
elif x-1 > 0:
    y = int(10.5+(x-1)*4)
    print(f"The dog's age in dog's years is {y} years.")
elif x-1 == 0:
    y = int(10.5)
    print(f"The dog's age in dog's years is {y} years.")
else:
    print(f"The dog's age can't be {x}")

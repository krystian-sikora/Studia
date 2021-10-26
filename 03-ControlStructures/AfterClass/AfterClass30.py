z=2
x=0
n=int(input("Enter N of prime values: "))
while x < n:
    y = 2
    while y <= z **0.5:
        if z%y == 0:
            break
        y += 1
    else:
        print(z)
        x += 1
    z += 1
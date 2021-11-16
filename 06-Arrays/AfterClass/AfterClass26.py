array = [4,2,8,4,7,9,5]
x = []
for a in array:
    if a%2==0:
        x.append(a)
for a in array:
    if a%2!=0:
        x.append(a)

print(x)

x = [15,8,31,47,2,19]
a=len(x)-1
b=0
display1="existed array: "
display2="reverse array: "

while b != len(x):
    display1+=str(x[b])+" "
    b+=1

while a != -1:
    display2+=str(x[a])+" "
    a-=1

print(display1)
print(display2)

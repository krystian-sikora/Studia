array=[4,3,7,1,3]

def sum(array):
    x="Sum of values: "
    a=0
    for i in array:
        a+=i
    x+=str(a)
    return x
def array2str(array):
    a="Array: "
    for i in array:
        a+=str(i)+" "
    return a

print(array2str(array))
print(sum(array))
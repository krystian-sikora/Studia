array = [4,2,8,4,7,9,5]

def minmax(array):
    x = []
    x.append(min(array))
    x.append(max(array))
    return x

print(minmax(array))
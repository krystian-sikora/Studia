array = []

for a in range(0,1000):
    array.append(a)

def rand_elem(array):
    import random
    i = len(array)
    x = random.randint(0,i)
    return array[x]

print(rand_elem(array))
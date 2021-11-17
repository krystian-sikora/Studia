array1 = [100,10,5,2,7,8,19]
array2 = [62,73,12,86]
array3 = [5,4,3,2,1]

def bubblesort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1], array[j]


bubblesort(array1)
bubblesort(array2)
bubblesort(array3)
print(array1)
print(array2)
print(array3)
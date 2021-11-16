array = ["Genowefa","Onufury","Celestyna","Alojzy","Pankracy"]
display1 = "Names: "
display2 = "Longest name:"
a=0
b=1
the_longest_name= array[0]
while a != len(array):
    display1+=str(array[a])+" "
    a+=1
while b != len(array):
    if len(the_longest_name) < len(array[b]):
        the_longest_name = array[b]
        b+=1
    else:
        b+=1

print(display1)
print(display2,the_longest_name)
def is_in_range():
    a = int(input("Enter the number you want to check if its within the <x1,x2>: "))
    b = int(input("Enter the x1 from <x1,x2>: "))
    c = int(input("Enter the x2 from <x1,x2>: "))
    
    if a>b and a<c:
        return True
    else:
        return False

print(is_in_range())
x = int(input("x = "))
y = int(input("y = "))

if x == 0:
    print(f"Point P is located at ({x},{y})")
elif x > 0:
    if y > 0:
        print(f"Point P({x},{y}) is located in the first quadrant")
    elif y < 0:
        print(f"Point P({x},{y}) is located in the fourth quadrant")
    elif y == 0:
        print(f"Point P is located at ({x},{y})")
elif x < 0:
    if y > 0:
        print(f"Point P({x},{y}) is located in the second quadrant")
    elif y < 0:
        print(f"Point P({x},{y}) is located in the third quadrant")
    else:
        print(f"Point P is located at ({x},{y})")
    
    
    
    
    
    
    
    
    
#if y == 0:
#        print(f"Point P is located at ({x},{y})")
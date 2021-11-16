array = [15,38,7,23,14]
number = 23

def occurs(number,array):
    for a in array:
        if a==number:
            return True
            break
    return False

print(occurs(number,array))
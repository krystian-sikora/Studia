for a  in range(1,31):
    if a%3==0 and a%5==0:
        print("BINGO")
    elif a%3==0:
        print("THREE")
    elif a%5==0:
        print("FIVE")
    else:
        print(a)
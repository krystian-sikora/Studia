with open("powers.txt","w") as file:
    for number in range(1,11):
        file.write(f"{number}, {number**2}, {number**3}\n   ")
        
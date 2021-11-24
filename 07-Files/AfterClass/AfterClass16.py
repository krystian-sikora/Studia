file = "internet.txt"

with open(file,"r") as file:
    for number in range(0,5):
        print(file.readline())
    keyboard_input = input("Press enter to display 5 more lines: ")
    while keyboard_input=="":
        for number in range(0,5):
            print(file.readline())
        keyboard_input = input("Press enter to display 5 more lines: ")
first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))

if first_number == second_number:
    print("Those numbers are equal!")
elif first_number > second_number:
    print(f"Numbers in ascending order: {second_number}, {first_number}")
else:
    print(f"Numbers in ascending order: {first_number}, {second_number}")
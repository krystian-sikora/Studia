x = int(input("Enter the amount in PLN: "))

if x // 5 > 0:
    piatka = x // 5
    if x % 5 // 2 > 0:
        dwojka = x % 5 // 2
        if x % 5 % 2 > 0:
            jedynka = x % 5 % 2
            print(f"The amount of PLN {x} in coins:\n5zł - {piatka}\n2zł - {dwojka}\n1zł - {jedynka}")
        else:
            print(f"The amount of PLN {x} in coins:\n5zł - {piatka}\n2zł - {dwojka}")
    else:
        if x % 5 > 0:
            jedynka = x % 5
            print(f"The amount of PLN {x} in coins:\n5zł - {piatka}\n1zł - {jedynka}")
        else:
            print(f"The amount of PLN {x} in coins:\n5zł - {piatka}")
else:
    if x // 2 > 0:
        dwojka = x // 2
        if x % 2 > 0:
            jedynka = x % 2
            print(f"The amount of PLN {x} in coins:\n2zł - {dwojka}\n1zł - {jedynka}")
        else:
            print(f"The amount of PLN {x} in coins:\n2zł - {dwojka}")
    else:
        if x > 0:
            jedynka = x
            print(f"The amount of PLN {x} in coins:\n1zł - {jedynka}")
        else:
            print("Zero monet!")
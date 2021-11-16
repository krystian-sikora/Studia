def sum_of_numbers(x):
    y=0
    x = str(x)
    for a in range(len(x)):
        y+=int(x[a])
    return y

a = 7182
print(sum_of_numbers(a))
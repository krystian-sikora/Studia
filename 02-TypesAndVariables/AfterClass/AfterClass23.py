# After class
# 23. 23% VAT was paid from the amount of PLN 15.84.
# Calculate and display VAT. Apply formatting with decimal places.
# Sample result:
# Amount  : 15.84 zł
# VAT 23% :  3.64 zł

n = 15.84
v = n*23/100

# f' {v:.2f}

print(f"Amount  : {n} zł\nVAT 23% :"  f' {v:.2f}  zł')


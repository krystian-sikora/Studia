pin = "0805"
for a in range(1,4):
    x = input("Enter the PIN code: ")
    if x == pin:
        print("PIN code is correct")
        break
    else:
        print("PIN is incorrect")
else:
    print("Sorry, your payment card has been blocked.")
        
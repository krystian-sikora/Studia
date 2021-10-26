number=int(input("Enter number: "))
sum=number
quantity=1
mean=number
while number!=0:
    number=int(input("Enter number: "))
    if number!=0:
        sum+=number
        quantity+=1
        mean=sum/quantity
    else:
        break
        
print(f"RESULT: Quantity={quantity}, Sum={sum}, Mean={mean}")
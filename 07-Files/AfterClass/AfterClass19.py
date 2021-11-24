shopping_list = open("shoppinglist.txt","w")
meat_and_fish = open("MeatAndFish.txt","r")
grains_and_bread = open("GrainsAndBread.txt","r")

for line in meat_and_fish:
    shopping_list.write(line)

shopping_list.write("\n")

for line in grains_and_bread:
    shopping_list.write(line)

shopping_list.close()
meat_and_fish.close()
grains_and_bread.close()

shopping_list = open("shoppinglist.txt","r")

for line in shopping_list:
    print(line)

shopping_list.close()

    

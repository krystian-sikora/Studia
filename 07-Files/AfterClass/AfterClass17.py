with open("internet.txt","r") as file:
    with open("copy.txt","w") as copy:
        copy.write(file.read())
        

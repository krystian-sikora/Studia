film_titles = ["Tytanic","Star Wars","James Bond","Indiana Jones","Matrix"]
file = open("Films.txt","w")
for film in film_titles:
    file.write(film)
    file.write("\n")
file.close()
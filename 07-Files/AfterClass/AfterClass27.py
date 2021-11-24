import re
with open("internet.txt","r") as file:
    x = file.read()
    six_plus_char_words = re.findall("[a-zA-Z]{6,}",x)
    lenght = len(six_plus_char_words)
    for number in range(0,lenght):
        print(six_plus_char_words[number])
        

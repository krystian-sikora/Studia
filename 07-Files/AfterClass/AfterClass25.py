import re
text = "To be, or not to be, that is the question"
vowels = re.findall("[AEIOUaeiou]",text)
print(len(vowels))
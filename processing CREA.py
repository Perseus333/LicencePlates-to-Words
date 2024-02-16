import re
print("Write the amount of times that the word must appear in the corpus:")
exigence = int(input("> "))

with open("words_dictionary_spanish.txt", "w", encoding="latin-1"):
    pass

words = set()

i = 1
with open("CREA_total.TXT", "r", encoding="latin-1") as file:
    for line in file:
        # Use regular expression to extract numbers and words
        matches = re.findall(r'\b(?:\d{1,3}(?:,\d{3})*(?:\.\d+)?|[a-zA-Z]+)\b', line)
        # Assuming you are interested in the third match (index 2)
        if len(matches) > 2 and matches[1].replace(",", "").isdigit():
            if int(matches[1].replace(",", "")) > exigence:
                words.add(matches[0])

with open("words_dictionary_spanish.txt", "a", encoding="latin-1") as file:
    for word in words:
        file.write(word + '\n')

import json
import random


def subset_in_set(subset, set_):
    return set(subset) <= set(set_)


language = input("Language? [s: spanish, e: english] ")
if language == "s":
    with open("words_dictionary_spanish.txt", 'r') as file:
        # Use a set comprehension to create a set from the words in the file
        raw_word_dict = {line.strip() for line in file}
else:

    with open('words_dictionary_english.json', 'r') as file:
        raw_word_dict = json.load(file)

print(f"Raw Word dict: {len(raw_word_dict)}")


# Create a new set with words of length greater than or equal to 4
word_dict = set(word for word in raw_word_dict if len(word) >= 3)

len_word_dict = len(word_dict)
print(f"Word Dict:     {len_word_dict}\n")


alphabet = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')


# Generate a random license plate with three consonants
licence_plate = "".join(random.choice(alphabet) for _ in range(3))
print(f"LICENCE PLATE: {licence_plate.upper()}\n")


i = 1
not_valid_candidates = set()

# Find words in the filtered dictionary that match the chosen consonants
print(f"Finding words that contain: {licence_plate.upper()}")
for word in word_dict:
    if not subset_in_set(licence_plate, word):
        not_valid_candidates.add(word)
    if i % 100000 == 0:
        print(f"\rProgress: {i}/{len_word_dict} ({round(i/len_word_dict*100,5)}%)", end="")
    i += 1
print(f"\rProgress: {i}/{len_word_dict} ({round(i/len_word_dict*100,0)}%)", end="")

candidates = word_dict - not_valid_candidates
print(f"\nCandidates Remaining: {len(candidates)}")

print(f"Finding words that contain {licence_plate.upper()} in the same order")
for word in candidates:
    temp_word = word
    for char in licence_plate:
        if char in temp_word:
            temp_word = temp_word[temp_word.index(char):]
        else:
            not_valid_candidates.add(word)
            break

candidates -= not_valid_candidates

print(f"Candidates Remaining: {len(candidates)}")

input()

print(candidates)

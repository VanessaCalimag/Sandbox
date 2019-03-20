"""Counting the number of vowels from the name given by the user."""

name = input("Name: ")
count = 0
for letter in name:
    if letter.lower() in 'aeiou':
        count += 1
print("Out of {} letters, {} has {} vowels.".format(len(name), name, count))

#!/usr/bin/env python3

filename = 'Files/wcfile.txt'

counts = {'lines':0,
          'characters':0,
          'words':0}

words = set()

for one_line in open(filename):
    counts['lines'] += 1
    counts['characters'] += len(one_line)
    line_words = one_line.split()
    counts['words'] += len(line_words)
    words.update(line_words)

counts['different words'] = len(words)
for key, value in counts.items():
    print(f"{key:15}: {value}")


# Write a program that shows, for a file:

# - number of lines
# - number of characters
# - number of words (separated by whitespace)
# - number of different/unique words



def duplicate_count(text):
    # Your code goes here
    text = text.lower()    
    newText = list(text)
    letters ={}
    n = 0
    for letter in newText:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    for letter, count in letters.items():
        if letters[letter] > 1:
            n += 1
    return n

print(duplicate_count("abcde"))
print(duplicate_count("abcdea"))
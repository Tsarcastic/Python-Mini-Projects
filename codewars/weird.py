def duplicate_encode(word):
    #your code here
    word = list(word.lower())
    newWord = ""
    counter = {}
    for letter in word:
        if letter not in counter:
            counter[letter] = word.count(letter)
    for letter in word:
        if counter[letter] > 1:
            newWord += ")"
        else:
            newWord += "("
    return newWord

duplicate_encode("None") 
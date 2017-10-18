def duplicate_encode(word):
    #your code here
    word = list(word.lower())
    newWord = ""
    counter = {}
    for letter in word:
        if letter not in counter:
            counter[letter] = word.count()
    print counter

duplicate_encode("Success") 
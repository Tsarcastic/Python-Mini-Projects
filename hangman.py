from random import *
list = ['consider', 'minute', 'accord']
answer = list[randint(0,2)]
numLetters = len(answer)
i = 0
theirView = []
guesses = 6

while i < numLetters:
    theirView.append("_")
    i += 1

theirLetters = " ".join(theirView)
guessPhrase =  "You have " + str(guesses) + " guesses remaining."
wordPhrase = "You know your word has the following letters. " + theirLetters

print "Let's play Hangman!"
print guessPhrase
print wordPhrase

theirGuess = raw_input('Which letter would you like to check?')

#then we check to see if it's only one letter -give an error & new raw_input if they do
#then we split theirLetters and run a forLoop to see if the letter matches any of those letters
#then we use dark sorcery to replace the "_" function above with actual letters

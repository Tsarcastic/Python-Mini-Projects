from random import *
list = ['consider', 'minute', 'accord']
answer = list[randint(0,2)] #The answer in the format of a word
answerList = answer.split() #The answer in the form of a list - for checking
numLetters = len(answer) #The number of letters for the answer
theirView = [] #The portion of the puzzle they have solved - or blank spaces if they haven't. 
guesses = 6 #Guesses remaining

i = 0 #Tracker

while i < numLetters: #Populate theirView with an underscore for each letter of answer
    theirView.append("_")
    i += 1

theirLetters = " ".join(theirView) #Creates a word from the list of Theirview - with a space between to display underscores
guessPhrase =  "You have " + str(guesses) + " guesses remaining."
wordPhrase = "You know your word has the following letters. " + theirLetters
print answer
def printout():
    print guessPhrase
    print wordPhrase

def checkAnswer(input):
    for item in answerList:
        if input = item:
            print "Yes it's working"


print "Let's play Hangman!"
printout()

checkAnswer(raw_input('Which letter would you like to check?'))

 
#then we check to see if it's only one letter -give an error & new raw_input if they do
#then we split theirLetters and run a forLoop to see if the letter matches any of those letters
#then we use dark sorcery to replace the "_" function above with actual letters

from random import *
list = ['consider', 'minute', 'accord']
rightAnswer = list[randint(0,2)] #The answer in the form of a list
answerList = rightAnswer.split() #The answer in the form of a word
numLetters = len(rightAnswer) #The number of letters for the answer
theirTrack = numLetters * "_"
theirView = [] #The portion of the puzzle they have solved - or blank spaces if they haven't. 
guesses = 6 #Guesses remaining
hangedMan = {} #for the drawings of the hanged man

for i in rightAnswer:
    theirView.append("_")

theirLetters = " ".join(theirView) #Creates a word from the list of Theirview - with a space between to display underscores
guessPhrase =  "You have " + str(guesses) + " guesses remaining."
wordPhrase = "You know your word has the following letters. " + theirLetters

def printout():
    print guessPhrase
    print wordPhrase

def checkAnswer(input):
    matchInWord = 0
    for a, item in enumerate(rightAnswer): #cycle through the answer list
        if input == item:
            matchInWord += 1
            print "That's in the word!"
            theirView[a] = input
    if matchInWord < 1:
        guesses += -1
    print hangedMan[guesses]    
            

hangedMan[0] = """                                   
                    _____
                    O    |    
                  / | \\  |
                   / \\   |
                         |
   """
hangedMan[1] = """                                   
                    _____
                    O    |    
                  / | \\  |
                   /     |
                         |
   """

hangedMan[2] = """                                   
                    _____
                    O    |    
                  / | \\  |
                         |
                         |
   """

hangedMan[3] = """                                   
                    _____
                    O    |    
                  / |    |
                         |
                         |
   """

hangedMan[4] = """                                   
                    _____
                    O    |    
                    |    |
                         |
                         |
   """

hangedMan[5] = """                                   
                    _____
                    O    |    
                         |
                         |
                         |
   """

hangedMan[6] = """                                   
                    _____
                         |    
                         |
                         |
                         |
   """

print hangedMan[6]

printout()

checkAnswer(raw_input('Which letter would you like to check?'))

 
#then we check to see if it's only one letter -give an error & new raw_input if they do
#then we split theirLetters and run a forLoop to see if the letter matches any of those letters
#then we use dark sorcery to replace the "_" function above with actual letters
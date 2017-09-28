from random import *
list = ['consider', 'minute', 'accord']
rightAnswer = list[randint(0,2)] #The answer in the form of a list
theirTrack = len(rightAnswer) * "_"
theirView = [] #The portion of the puzzle they have solved - or blank spaces if they haven't. 
guesses = 6 #Guesses remaining
hangedMan = {} #for the drawings of the hanged man

for i in rightAnswer:
    theirView.append("_")

theirLetters = " ".join(theirView) #Creates a word from the list of Theirview - with a space between

def checkAnswer(input): #Takes a letter as an input and checks it
    matchInWord = 0
    for a, item in enumerate(rightAnswer): #cycle through the answer list
        if input == item:
            matchInWord += 1
            theirView[a] = input
            theirLetters= " ".join(theirView)
    if matchInWord < 1:
        global guesses
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



def runGame():
    print hangedMan[6]
    while guesses > 0: #The game itself
        theirLetters = " ".join(theirView)
        print "You know your word has the following letters. " + theirLetters
        checkAnswer(raw_input('Which letter would you like to check?'))
        check = "".join(theirView)
        if check == rightAnswer:
            print theirLetters
            print "Congratulations! Little homey doesn't have to die."
            break
runGame()
 

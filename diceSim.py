import random



def diceRoller():
    sides = int(raw_input("How many sides would you like the die to have?"))
    rolls = int(raw_input("And how many times would you like to roll it?"))
    totalRolls = rolls
    runningTotal = 0
    listOfNum = {}

    while rolls > 0:
        newNum = random.randint(1, sides)
        runningTotal += newNum

        if newNum in listOfNum:
            listOfNum[newNum] += 1
        else:
            listOfNum[newNum] = 1
        rolls += -1

    
    for x in xrange(1, 5):
        print str(x) + " was rolled " + str(float(listOfNum[x]) / float(totalRolls) * 100) + "% of the time."
    
    print totalRolls
    print listOfNum
    print str(runningTotal)

while 1 > 0:
    diceRoller()
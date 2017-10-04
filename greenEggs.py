from string import maketrans



def encode():
    myFile = open('sam.txt', 'r')
    
    intab = "i"
    outtab = "I"
    trantab = maketrans(intab, outtab)
       
    for line in myFile:
        print line

    myFile.close()

encode()

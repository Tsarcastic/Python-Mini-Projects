totalPrice = 0
listOfItems = {}

menu = {}
menu[1] = 'Chicken strips'
menu[2] = 'French fries'
menu[3] = 'Hamburger'
menu[4] = 'Hotdog'
menu[5] = 'Large drink'
menu[6] = 'Medium drink'
menu[7] = 'Milk shake'
menu[8] = 'Salad'
menu[9] = 'Small drink'

prices = {}
prices['Chicken strips'] = 3.50
prices['French fries'] = 2.50
prices['Hamburger'] = 4.00
prices['Hotdog'] = 3.50
prices['Large drink'] = 1.75
prices['Medium drink'] = 1.50
prices['Milk shake'] = 2.25
prices['Salad'] = 3.75
prices['Small drink'] = 1.25

def enterOrder():
    myOrder = str(raw_input("Enter your order"))
    myItems = list(myOrder)
    for item in myItems: #Cycles through each number of their order
        for a in menu:
            if str(a) == str(item): #Checks to see if the input is equal to a key in menu
               #print "Adding " + str(prices[menu[item]])
               global totalPrice
               totalPrice += prices[menu[a]]
               print '${:,.2f}'.format(totalPrice)
               
               global listOfItems
               listOfItems[menu[a]] = 1
               print listOfItems


enterOrder()


#for a in menu: #Reference - Will print name of menu item & the price
    #print menu[a] + " \t " + str(prices[menu[a]])
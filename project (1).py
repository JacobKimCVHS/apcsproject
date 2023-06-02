import random


def pVal(card):
    if card == 'J' or card == 'Q' or card == 'K':
        return 10
    elif card == 'A':
        unooreleven = int(input("You got an " + card + " , choose: 1 or 11: "))
        while unooreleven != 1 and unooreleven != 11:
            unooreleven = int(input("You got an ace, choose: 1 or 11: "))
        if unooreleven == 1:
            return 1
        else:
            return 11
    card = int(card)
    return card
    
def cVal(card, ctotal):
    if card == 'J' or card == 'Q' or card == 'K':
        return 10
    elif card == 'A':
        if ctotal + 11 > 21:
            return 1
        else:
            return 11
    card = int(card)
    return card
    
def getpTotal(deck):
    total = 0
    i = 0
    for i in range(len(deck)):
        string = deck[i]
        total += pVal(string[0:string.index(" ")])
    return total
    
def getcTotal(decks, cTotal):
    total = 0
    for i in range(len(decks)):
        string = decks[i]
        total += cVal(string[0:string.index(" ")], cTotal)
    return total
    
def getDeck(deck, symbol, cards):
    count = 0
    for i in range(len(symbol)):
        for y in range(len(cards)):
            deck[count] = cards[y] + " " + symbol[i]
            count += 1
    return deck

def playerRound(playerD, pTotal, deck):
    hitorstay = "hit"
    while pTotal != 21:
        hitorstay = input("hit or stay: ")
        while hitorstay != "hit" and hitorstay != "stay":
            hitorstay = input("hit or stay: ")
        if hitorstay == "hit":
            playerD.append(deck[random.randint(0, len(deck) - 1)])
            last = playerD[len(playerD) - 1]
            pTotal += pVal(last[0:last.index(" ")])
            print("You got a " + playerD[len(playerD) - 1])
            print("Deck: ")
            displayCard(playerD, "player", 2)
            for p in range(len(playerD)):
                print(playerD[p])
            print("\nYour Value: " + str(pTotal))
            removedDeck.append(last)
            deck.remove(last) 
            
            
            if pTotal > 21:
                return pTotal
        else:
            return pTotal

def displayCard(card, person, order):
    if person == "player" or (person == "computer" and order > 1):
        for x in range(len(card)):
            onCard = card[x]
            displayedSymbol = ""
            if onCard[onCard.index(" ") + 1: len(onCard)] == "Spade":
                displayedSymbol = "\U00002660"
            elif onCard[onCard.index(" ") + 1: len(onCard)] == "Club":
                displayedSymbol = "\U00002663"
            elif onCard[onCard.index(" ") + 1: len(onCard)] == "Heart":
                displayedSymbol = "\U00002665"
            else:
                displayedSymbol = "\U00002666"

            print('┌───────┐')
            if len(onCard[0:onCard.index(" ")]) == 1:
                print('|' + onCard[0:onCard.index(" ")] + '      |')
            else:
                print('|' + onCard[0:onCard.index(" ")] + '     |')
            print('|       |')
            print('|   ' + displayedSymbol + '   |')
            print('|       |')
            if len(onCard[0:onCard.index(" ")]) == 1:
                print('|      ' + onCard[0:onCard.index(" ")] + '|')
            else:
                print('|     ' + onCard[0:onCard.index(" ")] + '|')
            print('└───────┘')
    else:
        print('┌───────┐')
        for q in range(5):
            print('|       |')
        print('└───────┘')
        for x in range(1, len(card)):
            onCard = card[x]
            displayedSymbol = ""
            if onCard[onCard.index(" ") + 1: len(onCard)] == "Spade":
                displayedSymbol = "\U00002660"
            elif onCard[onCard.index(" ") + 1: len(onCard)] == "Club":
                displayedSymbol = "\U00002663"
            elif onCard[onCard.index(" ") + 1: len(onCard)] == "Heart":
                displayedSymbol = "\U00002665"
            else:
                displayedSymbol = "\U00002666"

            print('┌───────┐')
            if len(onCard[0:onCard.index(" ")]) == 1:
                print('|' + onCard[0:onCard.index(" ")] + '      |')
            else:
                print('|' + onCard[0:onCard.index(" ")] + '     |')
            print('|       |')
            print('|   ' + displayedSymbol + '   |')
            print('|       |')
            if len(onCard[0:onCard.index(" ")]) == 1:
                print('|      ' + onCard[0:onCard.index(" ")] + '|')
            else:
                print('|     ' + onCard[0:onCard.index(" ")] + '|')
            print('└───────┘')





print("You are playing BlackJack with the computer.")
stop = "yes"
cScore = 0
pScore = 0
while stop == "yes":
    print("Your Score: " + str(pScore))
    print("Computer Score: " + str(cScore))
    cTotal = 0
    pTotal = 0
    hitorstay = "hit"
    cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    symbol = ["Heart", "Diamond", "Club", "Spade"]
    deck = [""] * 52
    getDeck(deck, symbol, cards)
    playerD = [deck[random.randint(0, len(deck) - 1)], deck[random.randint(0, len(deck) - 1)]]
    compD = [deck[random.randint(0, len(deck) - 1)], deck[random.randint(0, len(deck) - 1)]]
    removedDeck = [playerD[0], playerD[1], compD[0], compD[1]]
    for b in range(len(removedDeck)):
        deck.remove(removedDeck[b])
    pTotal = getpTotal(playerD)
    cTotal = getcTotal(compD, cTotal)
    print("Your Hand: ")
    displayCard(playerD, "player", 1)
    print("You have " + playerD[0] + " and " + playerD[1])
    displayCard(compD, "computer", 1)
    print("Computer has " + compD[1])
    print("\nYour Value: " + str(pTotal))
   
   #Allows Player to Hit or Stay
    
    pTotal = playerRound(playerD, pTotal, deck)
    #Makes the Computer to Hit or Stay
    if cTotal < pTotal and pTotal <= 21:
        compD.append(deck[random.randint(0, len(deck) - 1)])
        cTotal = getcTotal(compD, cTotal)
    print("Computer Hand: ")
    displayCard(compD, "computer", 2)
    print("Player Hand: ")
    displayCard(playerD, "player", 2)
    # Determine Victory   
    if pTotal > 21 and cTotal <= 21:
        print("Computer Wins! You have " + str(pTotal) + " and Computer has " + str(cTotal))
        cScore += 1
    elif cTotal > pTotal and cTotal <= 21:
        print("Computer Wins! You have " + str(pTotal) + " and Computer has " + str(cTotal))
        cScore += 1
    elif pTotal > 21 and cTotal > 21:
        print("Draw! Both has more than 21.")
        cScore += 1
        pScore += 1
    elif  pTotal == cTotal:
        print("Draw! Both have " + str(pTotal))
        cScore += 1
        pScore += 1
    elif cTotal > 21 and pTotal <= 21:
        print("You Win! You have " + str(pTotal) + " and Computer has " + str(cTotal))
        pScore+= 1
    else:
        print("You Win! You have " + str(pTotal) + " and Computer has " + str(cTotal));
        pScore += 1
    
    stop = input("Do you want to keep playing BlackJack: yes or no: ")


print("Your Score: " + str(pScore))
print("Computer Score: " + str(cScore))

if pScore > cScore:
    print("You Win!")
elif cScore > pScore:
    print("You Lose!")
else:
    print("You and Computer Ties!")
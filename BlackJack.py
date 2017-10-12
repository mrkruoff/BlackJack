from DeckofCards import *

def cardValue(card):
    if type(card[0])==int:
        return card[0]
    elif card[0]=="A":
        return 11
    else:
        return 10

def handvalue(hand):
    """iterates through hand returns values"""
    value=0
    acecount=0
    for i in range(len(hand)):
        card=cardValue(hand[i])
        value+=card
        if card==11:
            acecount+=1
    if value >21:
        if acecount>0:
            value-=(10*acecount)
    return value
    

def playerHandDelt(hand):
    """takes in hand as a list, iterates through
    and returns a value of the value of hand"""
    value=handvalue(hand)
    printHand(hand)
    return value
    
def dealerHandDelt(hand):
    """Reviews Dealers initial hand, if not 21, prints first card, if 21 ends round
    """
    value=handvalue(hand)
    if value ==21:
        printHand(hand)
        return value
    else:
        card=hand[0]
        printCard(card)
        print("XX")
        
def printCard(card):
    print(str(card[0])+card[1]+" ", end='')


def printHand(hand):
    """Prints out hand"""
    for i in range(len(hand)):
        current=hand[i]
        printCard(current)
    print("")

def deal(deck):
    """Draws a card and returns card"""
    card=drawCard(deck)
    return card


def round(deck):
    """plays a round of plackJack, prints out winner"""



if __name__=="__main__":

        
    


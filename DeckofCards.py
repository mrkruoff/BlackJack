"""
Python Module for creating a deck of cards
includes method for shuffling deck
"""
from random import shuffle

def createDeck(deck):
    """Creates deck of cards, takes in list,
    which should be empty or contain another deck for multilple decks in one
    """
    for i in range(1,14):
        value=i
        if value==1:
            value="A"
        elif value==11:
            value="J"
        elif value==12:
            value="Q"
        elif value==13:
            value="K"
        cardHeart=(value,"H")
        cardDiamond=(value,"D")
        cardSpade=(value,"S")
        cardClub=(value,"C")
        deck.append(cardHeart)
        deck.append(cardSpade)
        deck.append(cardDiamond)
        deck.append(cardClub)

def printDeck(deck):
    """prints deck"""
    for i in range(len(deck)):
        current=deck[i]
        print(str(current[0])+current[1]+" ", end='')
    print("")

def shuffleDeck(deck):
    """takes in deck object and uses python random.shuffle to shuffle deck"""
    shuffle(deck)

def drawCard(deck):
    """takes a deck, and returns the first card, also removing it from deck"""
    return deck.pop(0)

def cardsLeft(deck):
    """Takes a deck and returns value of amount of cards left"""
    return len(deck)
    

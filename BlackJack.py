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
        printHand(hand)
        #TODO: Uncomment these when done testing
        #card=hand[0]
        #printCard(card)
       # print("XX")
        return value
        
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

def dealer_turn(deck, dealerhandvalue, dealerdeck):
    while(dealerhandvalue<17):
        card=deal(deck)
        printCard(card)
        dealerdeck.append(card)
        dealerhandvalue=handvalue(dealerdeck)
        if dealerhandvalue >21:
            return dealerhandvalue
    return dealerhandvalue

def player_turn(deck, player_hand_value, player_deck):
    hit_or_stand=input("Hit(h) or Stand (s)\n")
    while hit_or_stand!="s":
        card=deal(deck)
        printCard(card)
        player_deck.append(card)
        player_hand_value=handvalue(player_deck)
        if player_hand_value >21:
            return player_hand_value
        hit_or_stand = input("Hit(h) or Stand (s)\n")
    return player_hand_value

def result(playerhand, dealerhand):
    if playerhand>dealerhand:
        print("Congrats you win")
    elif playerhand==dealerhand:
        print("Push")
    else:
        print("Dealer Wins")

def round(deck):
    """plays a round of plackJack, prints out winner"""
    dealer=[]
    player=[]
    for i in range (2):
        card=deal(deck)
        dealer.append(card)
        card=deal(deck)
        player.append(card)
    dealerhand=dealerHandDelt(dealer)
    playerhand=playerHandDelt(player)
    if dealerhand==21 and playerhand!=21:
        print("Sorry The Dealer Wins with Blackjack")
    else:
        playerhand=player_turn(deck, playerhand, player)
        if playerhand>21:
            print("Sorry  You Busted")
        else:
            dealerhand=dealer_turn(deck, dealerhand, dealer)
            result(playerhand, dealerhand)


def game():
    """Game function calls round until quit"""
    gamecont=True
    gameDeck=[]
    createDeck(gameDeck)
    shuffleDeck(gameDeck)
    startLength=cardsLeft(gameDeck)
    while(gamecont):
        round(gameDeck)
        print("Another Round[y/n]")
        cardsLeftIn=cardsLeft(gameDeck)
        if cardsLeftIn < (.25*startLength):
            gameDeck=[]
            createDeck(gameDeck)
            shuffleDeck(gameDeck)
        choice=input()
        if choice=="n":
            gamecont=False
    

if __name__=="__main__":
    game()

        
    


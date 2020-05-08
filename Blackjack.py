#version where Ace is always equal to 11
import random

dealerCards = []
playerCards = []

while len(dealerCards)<2:
    dealerCards.append(random.randint(1,11))
    if len(dealerCards)==2:
        print("The dealer has: ", dealerCards)
        """print("The dealer has X & ", dealerCards[1])"""

while len(playerCards)<2:
    playerCards.append(random.randint(1,11))
    if len(playerCards)==2:
        print("You have: ", playerCards)

while sum(dealerCards)<15:
    dealerCards.append(random.randint(1,11))
    print(dealerCards)
    if sum(dealerCards)==21:
        print ("Dealer has 21 and wins.")
        break
    elif sum(dealerCards)>21:
        print ("Dealer has busted. You win. ")
        break


while sum(playerCards)<21:
    choice = input("Do you want to hit or stand?\n")
    if choice == "hit":
        playerCards.append(random.randint(1,11))
        print("You have: ", playerCards)
    else:
        print("The dealer has a total of: " + str(sum(dealerCards)))
        print("You have a total of: " + str(sum(playerCards)))
        if sum(dealerCards)>sum(playerCards):
            print("You lose.")
            break
        elif sum(dealerCards)<sum(playerCards):
            print ("You win.")
            break
        elif sum(dealerCards)==sum(playerCards):
            print ("Tied Game.")
            break

if sum(playerCards)==21:
    print ("You have 21 and you win.")
elif sum(playerCards)>21:
    print ("You busted. Dealer wins. ")

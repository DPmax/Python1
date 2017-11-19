# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 14:21:16 2017

@author: LONGCHENG
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import random

#For Number one
def getseven(N):
    s = []
    # N times of experiments
    for k in range(0,N):
        count = 0
        sum = 0
        # check everytime if get sum of seven if not keep going
        while (sum != 7):
            count = count +1
            d1=random.randint(1,6)
            d2=random.randint(1,6)
            sum = d1+d2
        # count the how many times roll the two dice
        s.append(count)
    # plot the PMF of the Probability of get first "7"
    b=range(1,30)
    h1, bin_edges = np.histogram(s,bins=b)
    b1=bin_edges[1:max(s)]
    fig1=plt.figure(1)
    plt.stem(b1,h1)
    plt.title('Stem plot - Number of rolls needed to get a 7 wiht two dice')
    plt.xlabel('Turns')
    plt.ylabel('Number of rolls')
    	
    fig2=plt.figure(2)
    p1=h1/N
    plt.stem(b1,p1)
    plt.title('Stem plot - Sum of two dice: Probability mass function')
    plt.xlabel('Turns')
plt.ylabel('Probability')

#For Number Two
def getcoin(N):
    success = 0
    # N times of experiments
    for p in range(0,N):
        count = 0
        head, tail = 0, 0
        # each experiment has 100 times toss
        for k in range(0,100):
            coin = random.randint(0,1)
            if coin == 1:
                count = count+1
                head = head+1
            else:
                tail = tail+1
        if count == 50:
            success = success + 1
    print('Number of success is: ',success)
    print('The probability of success is: ', success/N)

#For Number Three
# Card class
class Card(object):
    #Creation of Card
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", 
              "8", "9", "10", "Jack", "Queen", "King"]
    # Initialization
    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank
    # Custome function function for return card's rank
    def getrank(self):
        return self.rank


# Deck class
class Deck(object):
    #Creation of Deck
    def __init__(self):
        self.cards = []
        for suit in range(0,4):
            for rank in range(0, 13):
                card = Card(suit, rank)
                self.cards.append(card)
                
    # Custome function for draw a card from deck
    def pop_card(self,i):
        #Randomly draw a card from the deck
        return self.cards.pop(i)
    


def getfour(N):
    success = 0
    # N experience 
    for x in range(0,N):
        deck = Deck()
        numbers = []
        
        # draw 5 cards
        for k in range(0,5):
            card = deck.pop_card(random.randint(0,51-k))
            #print("You draw a ",card)
            
            # store the cards rank to the list
            numbers.append(card.getrank())
        # sort the list so easy to check if there is 4 of a kind in the list
        numbers.sort()
        # check the 4 of a kind
        if (numbers[0]==numbers[1]==numbers[2]==numbers[3]):
            success = success +1
        
    print("\n The success time is: ",success)
    print("\n The probility is: ", success/N)

#For Number Four
def findpasstenfive(N):
    lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    success = 0
    count = 0
    # 1000 times of experiment
    for k in range(0,1000):
        # reinitialize the words list
        tenfivewords = []
        # store 4 letter words in 10^5 list
        for x in range (0,N):
            word = lowercase[random.randint(0,25)]+lowercase[random.randint(0,25)]+lowercase[random.randint(0,25)]+lowercase[random.randint(0,25)]
            tenfivewords.append(word)
        ps = 'aaaa'
        # check at least one word from list is matching with password
        if ps in tenfivewords:
            count = count+1
        if count > 0:
            success = success+1
        count = 0
    print("The success is: ",success)
    print("The probability is: ",success/1000)




def findpasstensix(N):
    lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    success = 0
    count = 0
    # 1000 times of experiment
    for k in range(0,1000):
        # reinitialize the words list
        tenfivewords = []
        for x in range (0,N):
        # store 4 letter words in 10^6 list
            word = lowercase[random.randint(0,25)]+lowercase[random.randint(0,25)]+lowercase[random.randint(0,25)]+lowercase[random.randint(0,25)]
            tenfivewords.append(word)
        ps = 'aaaa'
        # check at least one word from list is matching with password
        if ps in tenfivewords:
            count = count+1
        if count > 0:
            success = success+1
        count = 0
    print("The success is: ",success)
    print("The probability is: ",success/1000)


def findprob(N):
    lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    success = 0
    count = 0
    # 1000 times of experiment
    for k in range(0,1000):
        # reinitialize the words list
        tenfivewords = []
        for x in range (0,N):
            # store 4 letter words in X amount of list through test I get 315000 clost to get 0.5 probability
            word = lowercase[random.randint(0,25)]+lowercase[random.randint(0,25)]+lowercase[random.randint(0,25)]+lowercase[random.randint(0,25)]
            tenfivewords.append(word)
        ps = 'aaaa'
        # check at least one word from list is matching with password
        if ps in tenfivewords:
            count = count+1
        if count > 0:
            success = success+1
        count = 0
    print("The success is: ",success)
    print("The probability is: ",success/1000)



findprob(315000)
findpasstenfive(100000)
findpasstensix(1000000)
getfour(100000)
getcoin(100000)
getseven(100000)

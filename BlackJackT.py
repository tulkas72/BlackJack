#!/usr/bin/python3.7
import random
from itertools import product
from collections import Counter

special_names = {1: 'ace', 11: 'jack', 12: 'queen', 13: 'king'}


class Deck(object):
    """docstring for ClassName"""
    cards: list

    def __init__(self, ndecks=1):
        """
        :type ndecks: integer
        """
        super(Deck, self).__init__()
        self.suits = ["hearts", "spades", "diamonds", "clubs"]
        self.cards4suits = 13
        self.cards = list(product(self.suits, range(1, self.cards4suits + 1))) * ndecks
        self.extracted = list()

    def __str__(self):
        card: tuple
        name = ''
        result = ''
        counter = 1
        for card in self.cards:
            if card[1] in special_names.keys():
                name = special_names[card[1]]
            else:
                name = str(card[1])
            if counter == 13:
                result += '\n'
                counter = 1
            result += name + " " + card[0] + " "

        return result

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self) -> tuple:
        if len(self.cards) == 0:
            return ('no card', 0)
        card = self.cards.pop(0)
        self.extracted.append(card)
        return card

    def reinit_decks(self):
        self.cards.extend(self.extracted)
        self.extracted.clear()
        self.shuffle()


class Hand: #cambiar a BlackJackHand
    def __init__(self, hand: list):
        self.hand = sorted(hand, key=lambda c: c[1], reverse=True)
        self.splitted = False  #
        self.doubled = False
        self.value = 0
        self.ace = False
        self.black_jack = False

    def hand_value(self) -> tuple:
        """Gives value to BJ hand. Gives to values in any case, bat second value is only meaningful
        if the hands contains an ace at least.
        """
        value = self.value
        ace = self.ace
        for card in self.hand:
            if card[1] in [11, 12, 13]:
                value += 10
            elif card[1] == 1:
                if not ace:
                    value += 11
                    ace = True
                    self.ace = True
                else:
                    value += 1
            else:
                value += card[1]

        if len(self.hand) == 2 and value == 21:
                self.black_jack = True

        self.value = value
        return (self.value, self.black_jack)

    def set_hand(self,hand):
        self.hand = hand

    def get_hand(self):
        return self.hand

    def ret_hand(self):
        "returns cards in the hand, empties hand"
        tmp = self.hand.copy()
        self.hand.clear()
        return tmp

    def setdouble(self):
        self.doubled = True

    @property
    def getdouble(self):
        return self.doubled

    def setsplitted(self):
        self.splitted = True

class Bet:
    def __init__(self,bet,minbet = 2,maxbet = 500, maxraise = 20):
        self.bet = bet
        self.minbet = minbet
        self.maxbet = maxbet
        self.maxraise = maxraise

    def put_bet(self,bet):
        self.bet = bet
    def get_bet(self):
        return self.bet

    def raisebet(self, raise_amount):
        self.bet += raise_amount


class Player:
    def __init__(self, initial_money, name):
        self.hands = [] #list of hands, each hand has a bet thus hands contains pairs (hand,bet)
        self.money = initial_money
        #assert isinstance(name, str)
        self.name = name


class BlackJack:

    def __init__(self, ndecks = 4):
        if ndecks in range(1,10):
            self.ndecks = ndecks
        else:
            print("Number of decks between 1 y 9")
            print("Setting 4 decks")
            self.ndecks = 4
        self.players=[]
        self.minbet = 10
        self.maxbet = 200
        self.split = True
        self.double = True
        self.double_splitted = False

    def newPlayer(self,player):
        pass

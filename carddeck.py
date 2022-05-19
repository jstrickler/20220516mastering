import random

class CardDeck:  #  inherits from 'object'
    CLUB = '\u2663'
    DIAMOND = '\u2662'
    HEART = '\u2661'
    SPADE = '\u2660'

    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


    # constructor
    def __init__(self, dealer):
        self._dealer = dealer
        self._make_deck()


    def _make_deck(self):
        self._cards = []  # list
        for suit in self.CLUB, self.DIAMOND, self.HEART, self.SPADE:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self):
        return self._cards.pop()

    @property
    def cards(self):
        return self._cards


    @property # decorator
    def dealer(self):  # getter property
        return self._dealer

    @dealer.setter
    def dealer(self, dealer):  # setter property
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    @property
    def spam(self):
        return self._spam

    @property
    def ham(self):
        return self._ham

    @ham.setter
    def ham(self, value):
        #  validation code here...
        self._ham = value

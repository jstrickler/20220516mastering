from carddeck import CardDeck

class JokerDeck(CardDeck):

    def _make_deck(self):
        # call method in parent (or g-parent)
        super()._make_deck()
        for joker_rank in '1', '2':
            joker = joker_rank, '*JOKER*'
            self._cards.append(joker)

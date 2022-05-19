from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck('Mike')
print("\U0001F92F")
print("d1: {}".format(d1))

d2 = CardDeck("Lakshmi")
print("\U0001F92F")
print("d2: {}".format(d2))

print("d1.dealer: {}".format(d1.dealer))
print("d2.dealer: {}".format(d2.dealer))

d1.dealer = "Freddy"
print("d1.dealer: {}".format(d1.dealer))

try:
    d1.dealer = 3.1415
except TypeError as err:
    print(err)
else:
    print("d1.dealer: {}".format(d1.dealer))
print()

d1.shuffle()
print(d1.cards)
print()
for _ in range(7):
    print(d1.deal())
print('-' * 60)

j1 = JokerDeck("Amanda")
j1.shuffle()

print(j1.cards)







from collections import defaultdict
from pprint import pprint

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

print("airports['MCI']: {}".format(airports['MCI']))
print("airports.get('YOW'): {}".format(airports.get('YOW')))
print("airports.get('RDU'): {}".format(airports.get('RDU')))
print("airports.get('LAX', 0): {}".format(airports.get('LAX', 0)))

def zero():
    return 0

dd = defaultdict(zero)

dd['spam'] = 37
dd['ham'] = 98
dd['toast'] = 14
dd['eggs'] = 23

print("dd['ham']: {}".format(dd['ham']))
print("dd['eggs']: {}".format(dd['eggs']))
print("dd['schwarma']: {}".format(dd['schwarma']))
print("dd['wombat stew']: {}".format(dd['wombat stew']))
print()

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

fd = defaultdict(list)

for fruit in fruits:
    fd[fruit[0]].append(fruit)

pprint(fd)

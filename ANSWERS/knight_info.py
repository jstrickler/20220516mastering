#!/usr/bin/env python

import sys
from knight import Knight

for name in sys.argv[1:]:
    k = Knight(name)
    print("Name: {} {}".format(k.title, k.name))
    print("Favorite Color:", k.favorite_color)
    print()

k = Knight('Robin')
print(k.quest)

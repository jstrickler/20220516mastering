import sys

#    pkg.pkg          module
from john.math import geometry

a = geometry.circle_area(25)
print("a: {}".format(a))

b = geometry.square_area(18.2)
c = geometry.rectangle_area(14.9, 31.8)
print("b: {}".format(b))
print("c: {}".format(c))

print(geometry.ANIMAL)

for path in sys.path:
    print(path)




# instance = class()
# obj = class()
cities = list()

cities.append('Durham')
cities.append("Edinburgh")

print("cities: {}".format(cities))

fruits = list()
fruits.append('orange')
fruits.append('date')
fruits.append("mangosteen")
print("fruits: {}".format(fruits))

whatever = ['pink', 'blue', 'brown']

colors = list(whatever)
print("colors: {}".format(colors))

class Mammal:
    def run(self):
        print("running...")

class Dog(Mammal):
    def bark(self):
        print("woof! woof!")

d1 = Dog()
d1.bark()
d1.run()

d2 = Dog()
d2.bark()




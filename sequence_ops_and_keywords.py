

cities = ['Durham', 'Kaiserslautern', 'Houston',
          'Toronto', 'Chicago', 'Gettysburg',
          'Lancaster', 'Lakewood']

more_cities = ['Memphis', 'Reno', 'Poughkeepsie']

all_cities = cities + more_cities
print("all_cities: {}".format(all_cities))

a = 'foo'
b = 'bar'
c = a + b
print("c: {}".format(c))
#  FUBAR SNAFU

print('-' * 60)
print("'wombat' * 5: {}".format('wombat' * 5))

flags = ['True'] * 10
print("flags: {}".format(flags))

for city in 'Memphis', 'Dallas', 'Los Angeles', 'Reno':
    print(city, city in all_cities)
print()

s = "Chris Hemsworth"
print("Chris" in s)
print("Liam" in s)
print()

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

print("cities: {}\n".format(cities))
print("nums: {}\n".format(nums))

print(len(cities), min(cities), max(cities), sorted(cities), '\n')

print(len(nums), min(nums), max(nums), sum(nums), sorted(nums), '\n')

print("cities: {}\n".format(cities))

rcities = reversed(cities)
print("rcities: {}".format(rcities))
# print(len(rcities)) INVALID
# print(rcities[0])  INVALID
for city in rcities:
    print(city)
print()
print("Again:")
for city in rcities:
    print(city)
print("finished\n")

data = ['a', 'b', 'c']
e = enumerate(data)
print("e: {}".format(e))
for thing in e:
    print(thing)
print()

e = enumerate(data)
for i, value in e:
    print(i, value)
print()






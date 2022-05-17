
# list()  or  []

list1 = list()  # empty list
print("list1: {}".format(list1))

list2 = []  # also empty list
list3 = ['banana', 'almond', 'molasses']
print("list2: {}".format(list2))
print("list3: {}".format(list3))

color_data = 'red blue green purple'
colors = color_data.split()
print("colors: {}".format(colors))


cities = ['Durham', 'Kaiserslautern', 'Houston',
          'Toronto', 'Chicago', 'Gettysburg',
          'Lancaster', 'Lakewood']

print("cities: {}".format(cities))
print("cities[5]: {}".format(cities[5]))
print("len(cities): {}".format(len(cities)))
cities.append('Memphis')
print("cities: {}".format(cities))
cities.append("Reno")
print("cities: {}".format(cities))

cities.insert(0, 'Bangor')
cities.insert(5, 'Port Arthur')
print("cities: {}".format(cities))

more_cities = ['Tokyo', 'Beaumont', 'Indianapolis']

cities.extend(more_cities)
print("cities: {}".format(cities))

# LIST.insert(pos, obj)  LIST.append(obj)  LIST.exten(iterable)

del cities[1]
print("cities: {}".format(cities))

city = cities.pop()
print("city: {}".format(city))
print("cities: {}".format(cities))

city = cities.pop(4)
print("city: {}".format(city))
print("cities: {}".format(cities))

cities.remove('Lakewood')
print("cities: {}".format(cities))

city_to_remove = 'Albany'
if city_to_remove in cities:
    cities.remove(city_to_remove)

print("sorted(cities): {}".format(sorted(cities)))
# cities.sort()   sort in place

#   del LIST[pos]  LIST.pop(pos=-1)  LIST.remove(value)
print()
print("cities: {}".format(cities))

print("cities[0]: {}".format(cities[0]))
print("cities[9]: {}".format(cities[9]))
print("cities[10]: {}".format(cities[10]))
print("cities[-1]: {}".format(cities[-1]))
print("cities[len(cities)-1]: {}".format(cities[len(cities)-1]))

print("cities[0:4]: {}".format(cities[0:4]))

# slice
#  [start:stop]   [:stop]  [start:]  [:]  [::step]
print("cities[2:4]: {}".format(cities[2:4]))

print("cities[:5]: {}".format(cities[:5]))
print("cities[-4:]: {}".format(cities[-4:]))

actor = 'Chris Hemsworth'
print("actor: {}".format(actor))
print("actor[:5]: {}".format(actor[:5]))
print("actor[-9:]: {}".format(actor[-9:]))
print("actor[3:5]: {}".format(actor[3:5]))

print("cities: {}\n".format(cities))

for city in cities:
    # city = next(cities)
    # ...
    print(city)
print()

for color in 'red', 'purple', 'yellow':
    print("color.upper(): {}".format(color.upper()))
print()

c1 = "Memphis"
c2 = "Nashville"
c3 = "Knoxville"
for city in c1, c2, c3:
    print(city)
print()



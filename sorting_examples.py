
nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n1 = sorted(nums)
print("n1: {}\n".format(n1))

fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f1 = sorted(fruits)
print("f1: {}\n".format(f1))

def ignore_case(fruit):
    compare_value = fruit.lower()
    print(f"Comparing {fruit} as {compare_value}")
    return compare_value

f2 = sorted(fruits, key=ignore_case)
print("f2: {}\n".format(f2))

f3 = sorted(fruits, key=str.lower) # ignore case
print("f3: {}\n".format(f3))

f4 = sorted(fruits, key=len)  # sort by length
print("f4: {}\n".format(f4))s

def custom_sort(element):
    return len(element), element.lower()

f5 = sorted(fruits, key=custom_sort)
print("f5: {}\n".format(f5))

def wacky1(x):  # key function gets ONE item from list
    return x[-1].lower()

f6 = sorted(fruits, key=wacky1)
print("f6: {}\n".format(f6))

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]
for person in sorted(people):
    print(person)
print('-' * 60)

def by_last_name(person):
    print(f"key for {person} is", end=' ')
    # sort_value = person[1]
    # print(sort_value)
    return person[1], person[0]

for person in sorted(people, key=by_last_name):
    print(person)
print('-' * 60)

for person in sorted(people, key=lambda p: (p[1], p[0])):
    print(person)

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

for code, name in airports.items():
    print(code, name)
print('-' * 60)

for code, name in sorted(airports.items()):
    print(code, name)
print('-' * 60)

print(airports.items())
print('-' * 60)

def by_value(element):
    return element[1], element[0]

for code, name in sorted(airports.items(), key=by_value):
    print(code, name)
print('-' * 60)

for code, name in sorted(airports.items(), key=by_value, reverse=True):
    print(code, name)
print('-' * 60)


print("fruits: {}\n".format(fruits))

fruits.sort(key=str.lower)  # sort fruits in-place
print("fruits: {}\n".format(fruits))

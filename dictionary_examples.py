
d1 = dict()  # empty dictionary
d2 = {'NC': 'North Carolina', 'WA': 'Washington'}
d3 = {}  # empty dict


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

print("len(airports): {}".format(len(airports)))
print("airports: {}\n".format(airports))

airports['PIT'] = "Pittsburgh"
airports['ORD'] = "O'Hare"

print(airports['RDU'])
print(airports['MCO'])

print("airports: {}\n".format(airports))

# print("airports['NKW']: {}\n".format(airports['NKW']))
print("airports.get('NKW'): {}\n".format(airports.get('NKW')))
print("airports.get('NKW', 'NO SUCH AIRPORT'): {}\n".format(airports.get('NKW', 'NO SUCH AIRPORT')))

print('NKW' in airports)

print("airports.setdefault('NKW', 'Diego Garcia'): {}\n".format(airports.setdefault('NKW', 'Diego Garcia')))

print("airports: {}\n".format(airports))

del airports['OAK']
del airports['MCO']

print("airports: {}\n".format(airports))
print()

for code, name in airports.items():
    print(code, name)
print()

for code, name in sorted(airports.items()):
    print(code, name)
print()












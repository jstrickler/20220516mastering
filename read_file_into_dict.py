from pprint import pprint

knight_data = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_data[name] = title, color, quest, comment

# print("knight_data: {}\n".format(knight_data))
pprint(knight_data)

print("knight_data['Galahad']: {}".format(knight_data['Galahad']))
print("knight_data['Galahad'][2]: {}".format(knight_data['Galahad'][2]))
print()

for knight, data in knight_data.items():
    print(data[0], knight)
print()


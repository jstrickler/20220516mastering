nellie_countries = ['Diego Garcia', 'New Zealand',
                    'Japan', 'Brazil', 'Italy', 'Ghana',
                    'Burkino Faso']

andy_countries = ['Japan', 'Japan', 'Japan', 'Bulgaria', 'UK',
                  'Italy', 'France', 'Laos', 'New Zealand']

nellie = set(nellie_countries)
andy = set(andy_countries)

andy.add('China')
andy.add('Laos')
nellie.add('Paraguay')
nellie.add('Mongolia')



print("nellie: {}\n".format(nellie))
print("andy: {}\n".format(andy))
print()

print("COMMON:", nellie & andy)  # intersection
print("NOT COMMON:", nellie ^ andy)  # xor
print("ALL:", nellie | andy)  # union
print("Just Nellie:", nellie - andy)
print("Just Andy:", andy - nellie)

all_foods = set()
with open('DATA/breakfast.txt') as breakfast_in:
    for raw_line in breakfast_in:
        food = raw_line.rstrip()
        all_foods.add(food)
print("all_foods: {}\n".format(all_foods))



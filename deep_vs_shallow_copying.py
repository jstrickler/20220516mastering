from copy import deepcopy

colors = ['red', 'blue', 'purple']

c1 = colors  # NOT A COPY OF colors !!!

c1.append('yellow')
colors.append('green')


print("colors: {}".format(colors))
print("c1: {}\n".format(c1))

c2 = list(colors)  # a copy of colors
c3 = colors[::]  # also a copy of colors
print("colors is c1: {}".format(colors is c1))
print("colors is c2: {}".format(colors is c2))
print("colors is c3: {}".format(colors is c3))
print("c2 is c3: {}".format(c2 is c3))

colors = 5

print("colors: {}".format(colors))
print("c1: {}".format(c1))

data = [
    [1, 2, 3],
    [4, 5, 6],
]

d1 = data
d1.append([7, 8, 9])
print("data: {}".format(data))
print("d1: {}\n".format(d1))

d2 = list(data)
print("data is d2: {}".format(data is d2))
d2.append([10, 11, 12])
print("data: {}".format(data))
print("d2: {}\n".format(d2))

data[0].append(100)
print("data: {}".format(data))
print("d2: {}\n".format(d2))

d3 = deepcopy(data)
data[0].append('wombat')
print("data: {}".format(data))
print("d2: {}".format(d2))
print("d3: {}\n".format(d3))






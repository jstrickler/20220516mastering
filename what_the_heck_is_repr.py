
with open('DATA/mary.txt') as mary_in:
    file_contents = mary_in.read()

print(file_contents)   # print(str(file_contents) + '\n')
print('-' * 60)

print(repr(file_contents))

s = "a\nb\nc"
print(s)
print(repr(s))

x = 15
print(str(x), repr(x))

values = [1, 2, 3]
print(str(values), repr(values))




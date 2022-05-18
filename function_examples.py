from math import pi

def hello():
    print("Hello, Python world")

hello()  # call function with ()
hello_value = hello()
print("hello_value: {}".format(hello_value))


def circle_area(diameter):
    radius = diameter / 2
    return pi * (radius ** 2)

a = circle_area(77)
print("a: {}".format(a))

def square_area(length, width):
    return length * width

a = square_area(8, 10)
print("a: {}".format(a))

def get_matching_lines(pattern, file_path):
    matching_lines = []
    with open(file_path) as file_in:
        for line in file_in:
            if pattern in line:
                matching_lines.append(line.rstrip())

    return matching_lines

lines = get_matching_lines('pig', 'DATA/alice.txt')
for line in lines:
    print(line)
print('-' * 60)



def get_matching_lines2(pattern, *file_paths):
    matching_lines = []
    for file_path in file_paths:
        with open(file_path) as file_in:
            for line in file_in:
                if pattern in line:
                    matching_lines.append(line.rstrip())

    return matching_lines

lines = get_matching_lines2('pig', 'DATA/alice.txt', 'DATA/words.txt')
for line in lines:
    print(line)
print('-' * 60)

def square_root(x):
    return x ** .5

for n in 1, 18, 22, 9:
    print("square_root({}): {}".format(n, square_root(n)))









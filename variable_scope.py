
x = 100  # global variable (visible to end of file)

def spam():
    y = 42  # local variable (only visible in current function)
    print("in spam(): x is", x)


spam()
print("y: {}".format(y))



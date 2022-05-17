
i = 0
while i < 3:
    print(i)
    i += 1
print()


while True:
    user_name = input("What is your name? ")
    if user_name == 'q':
        break  # exit loop
    if user_name == '':
        print("Please enter a name")
        continue # go to top
    print("Hello,", user_name)



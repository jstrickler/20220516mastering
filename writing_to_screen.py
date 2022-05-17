person = "John"
city = "San Antonio"

value = 37.32939203

print(person, city, value)

# str(person) + ' ' + str(city) + ' ' + str(value) + '\n'

print(person, end='/')
print(city)

print(person, end='')
print(city)


print(person, city, value, sep=":")
print(person, city, value, sep="#")
print(person, city, value, sep=", ")
print(person, city, value, sep="")
print('-' * 60)

#  John is from San Antonio
print(person, "is from", city)
print(f"{person} is from {city}")  # f-string
print("{} is from {}".format(person, city))


print(f"Value is {value}")
print(f"Value is {value:.2f}")






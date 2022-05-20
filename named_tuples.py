from collections import namedtuple

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

for first_name, last_name, product, dob in people:
    print(last_name, dob)
print('-' * 60)

Person = namedtuple("Person", "first_name last_name product dob")

bob = Person("Robert", "Rodriguez", "Pixar", "1995-02-18")
print("bob.first_name: {}".format(bob.first_name))
print("bob.last_name: {}".format(bob.last_name))
print()


for person_data in people:
    p = Person(*person_data)
    print(p.first_name, p.last_name, p.dob)
print('-' * 60)








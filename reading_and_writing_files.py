
file_path = "DATA/mary.txt"

mary_in = open(file_path, "r")
# read file here ...
mary_in.close()

# read file one line at a time
with open(file_path, "r") as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip() # remove \n \r ' ' \t etc
        print(line)   #  "line contents\n"  + "\n"
print('-' * 60)

# read file into one string
with open(file_path) as mary_in:
    contents = mary_in.read()
    print("RAW:")
    print(repr(contents))
    print("NORMAL:")
    print(contents)
print('-' * 60)

# read file into list of lines with \n
with open(file_path) as mary_in:
    all_lines = mary_in.readlines()
    print(all_lines)
print('-' * 60)

# read file into list of lines without \n
with open(file_path) as mary_in:
    all_lines = [line.rstrip() for line in mary_in]
    print(all_lines)
print('-' * 60)

party_wanted = "Whig"
file_path = "DATA/presidents.txt"
with open(file_path) as presidents_in:
    for raw_line in presidents_in:
        line = raw_line.rstrip()
        term, last_name, first_name, born, died, birthplace, birth_state, took_office, left_office, party = line.split(':')
        if party == party_wanted:
            print(first_name, last_name)
print('-' * 60)

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

delimiter = '\t'
with open('nerds.txt', 'w') as nerds_out:
    for row in people:
        data = delimiter.join(row) + '\n'
        nerds_out.write(data)

with open('nerds.txt') as nerds_in:
    for raw_line in nerds_in:
        line = raw_line.rstrip()
        first_name, last_name, product, dob = line.split(delimiter)
        print(first_name, last_name, dob)




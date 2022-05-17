s1 = "spam\n"
print(len(s1))
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"

print("Guido's the ex-BDFL of Python")
print('Guido is the ex-"BDFL" of Python')

print("""Guido's the ex-"BDFL" of Python""")
print(s5, '\n')

actor = "Chris Hemsworth"

print("actor.upper(): {}".format(actor.upper()))
a = actor.upper()
print("a: {}".format(a))
print("actor: {}".format(actor))

print("actor.count('h'): {}".format(actor.count('h')))
print("actor.lower().count('h'): {}".format(actor.lower().count('h')))

print("actor.find('Chris'): {}".format(actor.find('Chris')))
print("actor.find('Liam'): {}".format(actor.find('Liam')))
print("actor.find('worth'): {}".format(actor.find('worth')))

print("actor.startswith('Chris'): {}".format(actor.startswith('Chris')))
print("actor.startswith('Liam'): {}".format(actor.startswith('Liam')))

print("'worth' in actor: {}".format('worth' in actor))
print("'value' in actor: {}".format('value' in actor))

print("actor.replace('Chris', 'Liam'): {}".format(actor.replace('Chris', 'Liam')))

s = "spam ham splotch"
print("s.replace(' ', '-'): {}".format(s.replace(' ', '-')))

s = "        Guido is the best      "
print(s.lstrip() + "|")
print(s.rstrip() + "|")
print(s.strip() + "|")
print()

s2 = "idiiiiidddseGuido is the bestddiiiiiiiiiiiieeehhhhi"
print(s2.lstrip("idseh") + "|")
print(s2.rstrip("idseh") + "|")
print(s2.strip("idseh") + "|")
print()

s = "$10390.93"
f = float(s.lstrip('$'))
print(f, '\n')

suits = "clubs\tdiamonds     hearts         spades".split()
print("suits: {}".format(suits))

record = "Bill:Gates:Microsoft"
values = record.split(':')
print(values)




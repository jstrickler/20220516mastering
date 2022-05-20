from collections import Counter

with open('DATA/words.txt') as words_in:
    first_letters = [word[0] for word in words_in]

c = Counter(first_letters)
print(c['x'], c['s'])

print(c.most_common(5))
print()
for letter, count in c.items():
    print(letter, count)

for letter in 'a', 'm', 'a', 'r', 'x', 'e', 'v':
    c[letter] += 1





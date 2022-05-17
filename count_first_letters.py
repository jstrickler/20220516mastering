
input_path = "DATA/words.txt"


count = 0
letter = "pre"

output_path = f"{letter}_words.txt"

with open(input_path) as words_in:
    with open(output_path, "w") as words_out:
        for word in words_in:
            if word.startswith(letter):
                words_out.write(word)  # word still has \n
                count += 1

print(f"{count} words start with '{letter}'")  # f-string
# print("{} words start with '{}'".format(count, letter))

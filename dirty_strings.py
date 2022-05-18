#!/usr/bin/python3

spam = [
    "Spam",
    "eggs  ",
    "   spam    ",
    "     spam spam     ",
    "SPAM	",
    "       SPAM and eggs    ",
    "Spam",
    "   Spam,    spam, spam,    spam, spam, eggs, and spam      ",
]

def cleanup(s):
    # your code....
    return s  # return "cleaned up" s

for string in spam:
    clean_string = cleanup(string)
    print(f"|{string}| |{clean_string}|")



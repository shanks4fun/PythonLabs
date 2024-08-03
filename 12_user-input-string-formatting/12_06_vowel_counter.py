# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

sentance = input("Type a sentance for me: ").lower()
vowels = ""
a = e = i = o = u = ""

for char in sentance:
    for vowel in "aeiou":
        if char == vowel:
            vowels += char
        else:
            continue

for char in vowels:
    if char == "a":
        a += char
    elif char == "e":
        e += char
    elif char == "i":
        i += char
    elif char == "o":
        o += char
    elif char == "u":
        u += char
    else:
        continue

print(f"\na {len(a)}\ne {len(e)}\ni {len(i)}\no {len(o)}\nu {len(u)}")

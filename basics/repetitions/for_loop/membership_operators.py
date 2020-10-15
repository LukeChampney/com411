print("What phrase do you see?")
phrase = input()
print("Reversing...")

reversed = ""

for letter in phrase:
    reversed = letter + reversed

print(reversed)
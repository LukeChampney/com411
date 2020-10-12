print("How many live cables should I avoid?")
livecables = int(input())

livecablesavoided = 0

while (livecablesavoided < livecables):
  print("Avoiding...", end="")
  livecablesavoided += 1
  print("Done! {} live cables avoided." .format(livecablesavoided))

print()
print("All live cables have been avoided.")

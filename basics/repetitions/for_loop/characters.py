print("What strange markings do you see?")
markings = input()
print("Identifying...")

for amount in range (0, len(markings), 1):
  print("index {}:" .format(amount), markings[amount])
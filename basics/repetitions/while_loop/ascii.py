print("How many bars should be charged?")
bars = int(input())

chargedbars = 0

while (chargedbars < bars):
  print("Charging:", end="")
  chargedbars += 1
  print("█" * chargedbars)

print()
print("The battery is fully charged.")
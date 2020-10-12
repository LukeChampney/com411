print("What level of brightness is required?")
level = int(input())
print()
print("Adjusting brightness...")
print()

for level in range (0, level + 1, 2):
  print("Beep's brightness level:", "*" * level)
  print("Bop's brightness level:", "*" * level)
  print()

print("Adjustments complete!")
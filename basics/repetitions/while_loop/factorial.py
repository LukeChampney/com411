print("Please enter a number:")
amount = int(input())


number = 0
total = 1

while (number < amount):
  number += 1
  total = total * number

print("The factorial is {}" .format(total))
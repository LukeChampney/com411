print("How many numbers should I sum up?")
amount = int(input())

number = 0
total = 0

while (number < amount ):
  number += 1
  print("Please enter number {} of {}:" .format(number, amount))
  sum = int(input())
  total = sum + total

print("The answer is {}." .format(total))


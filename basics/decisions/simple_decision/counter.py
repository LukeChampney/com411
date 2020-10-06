print("Please enter the first whole number.")
number1 = int(input())
print("Please enter the second whole number.")
number2 = int(input())
print("Please enter the third whole number.")
number3 = int(input())

odd = 0
even = 0

if number1 % 2 == 0:
  even = even + 1

else:
  odd = odd + 1

if number2 % 2 == 0:
  even = even + 1

else:
  odd = odd + 1

if number3 % 2 == 0:
  even = even + 1

else:
  odd = odd + 1


print("There were {} even and {} odd numbers." .format(even ,odd))
print("Please enter the first number.")
number1 = int(input())

print("Please enter the second number.")
number2 = int(input())

if number1 == number2:
  print("Both number are the same")

elif number1 > number2:
  print("{} is bigger than {}" .format(number1 ,number2))

elif number1 < number2:
  print("{} is smaller than {}" .format(number1 ,number2))

else:
  print("Error")
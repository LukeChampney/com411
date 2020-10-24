#define a function
def run():
  
  #print a question
  print("Please enter a number:")
  amount = int(input())


  number = 0
  total = 1

  #repeat the calculation but the number is added each time until number match with amount
  while (number < amount):
    number += 1
    total = total * number

  print("The factorial is {}" .format(total))
#define a function
def run():

  #print a question
  print("Calculating the sum of the first 100 numbers...")

  number = 1
  total = 0

  #repeats the calculation all the way to 100
  while (number <= 100):
    total = total + number
    number += 1

  print("...Done! The answer is {}" .format(total))
#define a function
def run():

  #print a question
  print("How many numbers should I sum up?")
  amount = int(input())

  number = 0
  total = 0

  #repeats the message but changing a little bit every time depending on user answer
  while (number < amount ):
    number += 1
    print("Please enter number {} of {}:" .format(number, amount))
    sum = int(input())
    total = sum + total

  print("The answer is {}." .format(total))


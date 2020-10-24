#define a function
def run():

  #print a question
  print("Please enter the first whole number.")
  number1 = int(input())
  #print an another question
  print("Please enter the second whole number.")
  number2 = int(input())
  #print an another question
  print("Please enter the third whole number.")
  number3 = int(input())

  #creating variables
  odd = 0
  even = 0

  #checking if the number1 is even
  if number1 % 2 == 0:
    even = even + 1

  #if the number1 is not even then automatically becomes odd
  else:
    odd = odd + 1

  #checking if the number2 is even
  if number2 % 2 == 0:
    even = even + 1

  #if the number2 is not even then automatically becomes odd
  else:
    odd = odd + 1

  #checking if the number3 is even
  if number3 % 2 == 0:
    even = even + 1

  #if the number3 is not even then automatically becomes odd
  else:
    odd = odd + 1

  #prints the following message with data collected from the user
  print("There were {} even and {} odd numbers." .format(even ,odd))
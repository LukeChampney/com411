#define a function
def run():

  #print a question
  print("Please enter a whole number.")
  number = int(input())

  #checking if the number is even
  if number % 2 == 0:
    print("The number {} is an even number" .format(number))

  #checking if the number is odd
  else:
    print("The number {} is an odd number" .format(number))
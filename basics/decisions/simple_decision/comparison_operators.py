#define a function
def run():  

  #print a question
  print("Please enter the first number.")
  number1 = int(input())

  #print an another question
  print("Please enter the second number.")
  number2 = int(input())

  #if the number1 and number2 match then print the following message
  if number1 == number2:
    print("Both number are the same")

  #if the number1 is bigger than number2 then print the following message
  elif number1 > number2:
    print("{} is bigger than {}" .format(number1 ,number2))

  #if the number1 is smaller than number2 then print the following message
  elif number1 < number2:
    print("{} is smaller than {}" .format(number1 ,number2))

  else:
    print("Error")
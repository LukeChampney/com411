#define a function
def run():

  #print a question
  print("What is your name human?")
  #only in string format
  name = str(input())

  #print an another question
  print("How old are you (in years)?")
  #only in integer format
  age = int(input())

  #print an another question
  print("How tall are you (in meters)?")
  #only in float/decimal format
  height = float(input())

  #print an another question
  print("How much do you weigh (in kilograms)?")
  #only in float/decimal format
  weight = float(input())

  #calculation using user data
  BMI = weight / (height**2)

  #print an answer with user data
  print("Your name is {} and you are {} years old and your BMI is {:.2f}" .format(name, age, BMI))
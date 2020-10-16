#created a function with couple of parameters
def sum_weights(Beep_weight, Bop_weight):
  addition = Beep_weight + Bop_weight
  return addition

#created an another function with couple of parameters
def calc_avg_weight(Beep_weight, Bop_weight):
  average = (Beep_weight + Bop_weight)/2
  return average

#created another function
def run():
  #asks user some questions to get data
  print("What is the weight of Beep?")
  Beep_weight = int(input())

  print("What is the weight of Bop?")
  Bop_weight = int(input())

  print("What would you like to calculate (sum or average)?")
  answer = str(input())

  #if their answer matches one of following words
  if answer == "sum":
    number = sum_weights(Beep_weight, Bop_weight)
    print("The sum of Beep and Bop's weight is {}." .format(number))

  elif answer == "average":
    number = calc_avg_weight(Beep_weight, Bop_weight)
    print("The average of Beep and Bop's weight is {}." .format(number))

  else:
    print("I don't understand")

run()


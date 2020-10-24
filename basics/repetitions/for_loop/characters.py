#define a function
def run():

  #print a question
  print("What strange markings do you see?")
  markings = input()
  print("Identifying...")

  #for loop with range of how many letters are there in the user input
  for amount in range (0, len(markings), 1):
    print("index {}:" .format(amount), markings[amount])
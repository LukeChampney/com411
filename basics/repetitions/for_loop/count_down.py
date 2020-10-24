#define a function
def run():

  #print a question
  print("How far are we from the cave?")
  steps = int(input())

  #for loop instead of counting up it's downwards
  for steps in range(steps, 0, -1):
    print("{} steps remaining" .format(steps))

  print("We have reached the cave!")
#created a function with parameter
def display_ladder(steps):
  
  #used loop to repeat print message depending on user's answer
  for step in range(steps):
        print("| |")
        print("***")
  
  #this is for bottom of the ladder for aesthetic purpose
  print("| |")


#created another function
def create_ladder():
  print("How many steps remain?")
  steps = int(input())
  display_ladder(steps)

#use function
create_ladder()
#define a function
def run():

  #define a function with parameter
  def display_ladder(steps):
  
    #used loop to repeat print message depending on user's answer
    for step in range(steps):
      print("| |")
      print("***")
  
    #this is for bottom of the ladder for aesthetic purpose
    print("| |")


  #define an another function
  def create_ladder():
    print("How many steps remain?")
    steps = int(input())
    display_ladder(steps)

  #calls a function
  create_ladder()
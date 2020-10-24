#define a function
def run():

  #define a function with single parameter
  def cross_bridge(steps):

    #creates a loop
    for step in range(steps):
      print("Crossed step.")

    #if steps is bigger than 5 print the following message
    if steps > 5:
      print("The bridge is collapsing!")

    #if steps is 0 then print the following message
    elif steps == 0:
      print("Hurry! The large boulder is coming for you")

    #if the steps is bigger than 0 but less or equal to 5 the print the following message
    else:
      print("We must keep going!")

  #calls the functions
  cross_bridge(3)
  cross_bridge(6)
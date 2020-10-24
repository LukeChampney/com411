#define a function
def run():

  #define a function with couple of parameters
  def climb_ladder(stepsremaining, stepscrossed):

    #displays message depending on parameter plan's value
    if stepsremaining > stepscrossed:
      print("Still some way to go!")
  
    else:
      print("We are almost there!")

  #use function
  climb_ladder(5, 2)
  climb_ladder(2, 5)


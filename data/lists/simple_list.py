#define a function
def run():

  #define an another function
  def directions():
    #adding item in the list
    direction = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return direction

  #define an another function
  def run():
    #prints whatever in the list
    print(directions())

  run() 



#define a function
def run():

  #define an another function
  def directions():
    #adding items in the list
    directions = ["Move Forward", "Move Backward", "Move Left", "Move Right"]
    return directions

  #define an another function
  def menu():
    print("Please select a direction:")
    #storing call a function in local variable
    direction = directions()
    #prints the message with index position
    for index in range(len(direction)):
      print("{} is at index {}.".format(direction, index))

  def run():
    #calls menu function
    menu()
  #runs the program
  run()
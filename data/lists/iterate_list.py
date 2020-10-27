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
      print(f"{index}: {direction[index]}")

  def run():
    #calls menu function
    menu()
  #runs the program
  run()




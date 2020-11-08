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
    index = int(input())
    return direction[index]

  def run():
    route = []
    print("Working out escape route...")

    for count in range(5):
      route.append(menu())
    print(f"Escape route: {route}")
    
  run()
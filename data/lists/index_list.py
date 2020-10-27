#define a function
def run():

  #define an another function
  def movements():
    #adding item/number in the list
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path

  #define an another function
  def run():
    print("Moving...")
    path = movements()
    #chooses to print whatever in the list
    print(f"{path[0]} for {path[1]} steps")
    print(f"{path[2]} for {path[3]} steps")
    print(f"{path[4]} for {path[5]} steps")
    print(f"{path[6]} for {path[7]} steps")

  #calls the function
  run()
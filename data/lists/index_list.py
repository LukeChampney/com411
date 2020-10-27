<<<<<<< HEAD
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
=======
def run():

  def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path

  def run():
    print("Moving...")
    path = movements()
>>>>>>> 8f3df700ba3ca0603299935ec14f13f2c2f507d1
    print(f"{path[0]} for {path[1]} steps")
    print(f"{path[2]} for {path[3]} steps")
    print(f"{path[4]} for {path[5]} steps")
    print(f"{path[6]} for {path[7]} steps")

<<<<<<< HEAD
  #calls the function
=======
>>>>>>> 8f3df700ba3ca0603299935ec14f13f2c2f507d1
  run()
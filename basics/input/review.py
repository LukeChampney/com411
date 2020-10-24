#define a function
def run():

  #print a question with new line and tabbed function
  print("\n \t What is your robot called?")
  name = str(input())
  #print a question with tabbed function
  print("\t How old is your robot?")
  age = float(input())
  #print a question with new line and tabbed function
  print("\t How many heart does this robot have?")
  hearts = int(input())
  #print a question with new line and tabbed function
  print("\t Please enter any character for robot's eyes")
  eye = input()

  #print a robot with user's data about eye
  print("         O")
  print("         |")
  print("     #########")
  print("     #", eye," ", eye, "#") 
  print("  O--#  [_]  #--O")
  print("     #########")


  #print an answer with user's data
  print("Hearts:","♥"*hearts)
  #print an answer with user's data
  print("Hello my name is {} and i'm {} years old" .format(name, age))
  
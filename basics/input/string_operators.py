#define a function
def run():

  #print a question
  print("Please enter the number of lives.")
  lives = int(input())

  #print an another question
  print("Please enter the energy level.")
  energy = int(input())

  #print an another question
  print("Please enter the shield level.")
  shield = int(input())

  #print an answer with user data
  print()
  print("Health has been set.")
  print()
  print()
  print("Lives:","♥"*lives) #the message will be repeated as many times as user say
  print("Energy:","♦"*energy)
  print("Shield:","♦"*shield)
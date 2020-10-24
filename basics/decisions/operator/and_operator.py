#define a function
def run():

  #print a question
  print("What did I hear?")
  hear = input()
  #print an another question
  print("What did I see?")
  see = input()
    
  #if both of the answers match then print the following message
  if ((hear == "grrr") and (see == "two red eyes")):
    print("There is a scary creature. I should get out of here!")
  #if both of the answer does not match then print the following message
  else:
    print("I am a little scared but I will continue.")

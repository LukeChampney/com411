#define a function
def run():
  
  #print a question
  print("Towards which direction should I paint (up, down, left or right)?")
  answer = input()

  #if the answer match then print the following message
  if answer == ("up"):
    print("I am painting in the upward direction!")

  #if the answer match then print the following message
  elif answer == ("down"):
    print("I am painting in the downward direction!")

  #if the answer match then print the following message
  elif answer == ("left"):
    print("I am painting in the westward direction!")

  #if the answer match then print the following message
  elif answer == ("right"):
    print("I am painting in the eastward direction!")

  #if the answer does not match then print the following message
  else:
    print("I don't understand")

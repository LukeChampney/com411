#define a function
def run():

  #print a question
  print("Where should I look?")
  place = str(input())
  #if the user answer matches then print the following message
  if place == ("in the bedroom"):
    #print a question
    print("Where in the bedroom should I look?")
    bed = input()
    
    #if the user answer matches then print the following message
    if (bed == "under the bed"):
      print("Found some shoes but no battery")
    #if the user answer does not match then print the following message
    else:
      print("Found some mess but no battery")

  #if the user answer matches then print the following message
  if place == ("in the bathroom"):
      #print a question
      print("Where in the bathroom should I look?")
      bed = input()

      #if the user answer matches then print the following message
      if (bed == "in the bathtub"):
        print("Found a rubber duck but no battery")
      #if the user answer does not match then print the following message
      else:
        print("Found a wet surface but no battery")
  
  #if the user answer matches then print the following message
  if place == ("in the lab"):
    print("Where in the lab should I look?")
    bed = input()

    #if the user answer matches then print the following message
    if (bed == "on the table"):
      print("Yes! I found my battery!")
    #if the user answer does not match then print the following message
    else:
      print("Found some tools but no battery.")


  #if the user answer from the first question doesn't match then print the following message
  else:
    print("I do not know where that is but I will keep looking.")
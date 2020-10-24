#define a function
def run():

  #print a question
  print("What type of adventure do you want to go on?")
  adventure = str(input())

  #if either of the answers match then print the following message
  if ((adventure == "short") or (adventure == "scary")):
    print("Entering the dark forest!")

  #if either of the answers match then print the following message
  if ((adventure == "long") or (adventure == "safe")):
    print("Taking the safe route!")
  #if both of the answer does not match then print the following message
  else:
    print("Not sure which route to take.")
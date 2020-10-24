#define a function
def run():

  #print a question
  print("Please enter the activity to be performed.")
  answer = input()

  #if the answer match then print the following message
  if answer == ("calculate"):
    print("Performimg calculations...")
    print("Calculations completed!")
  #if the answer does not match then print the following message
  else:
    print("Performing activity...")
    print("Activity completed!")




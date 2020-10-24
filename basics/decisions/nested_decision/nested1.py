#define a function
def run():

  #print a question
  print("What type of cover does the book have?")
  cover = str(input())

  #if the user answer matches then print the following message
  if cover == ("soft"):
    print("Is the book perfect-bound?")
    binding = input()

    #if the user answer matches with first question and the previous question then print the following message
    if (binding == "yes"):
      print("soft cover, perfect bound books are very popular!")
    #if the user answer from the first question match but don't match from the previous question then print the following message
    else:
      print("Soft covers with coils or stitches are great for short books")

  #if the user answer from the first question doesn't match then print the following message
  else:
    print("Books with hard covers can be more expensive!")
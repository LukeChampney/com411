#define a function
def run():

  #print a question
  print("What phrase do you see?")
  phrase = input()
  print("Reversing...")

  #create a variable
  reversed = ""

  #reversing the phrase
  for letter in phrase:
    reversed = letter + reversed

  print(reversed)
#define a function
def run():

  #print a question
  print("What phrase do you see?")
  phrase = str(input())
  print("Reversing...")

  #reverses the user's answer
  for reverse in range (len(phrase) -1, -1, -1):
    print(phrase[reverse], end="")
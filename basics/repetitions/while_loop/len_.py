#define a function
def run():

  #print a question
  print("Please enter a phrase:")
  phrase = input()

  bop = 0

  #repeat the word 'bop' depending on how many letter are there in phrase
  while (bop < len(phrase)):
    bop += 1
    print("bop ", end="")

#define a function
def run(): 

  #print a question
  print("How many live cables should I avoid?")
  livecables = int(input())

  livecablesavoided = 0

  #repeat the message but the bars is added each time until livecablesavoided match with livecables
  while (livecablesavoided < livecables):
    print("Avoiding...", end="")
    livecablesavoided += 1
    print("Done! {} live cables avoided." .format(livecablesavoided))

  print()
  print("All live cables have been avoided.")

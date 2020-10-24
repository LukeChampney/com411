#define a function
def run():

  #print a question
  print("What level of brightness is required?")
  level = int(input())
  print()
  print("Adjusting brightness...")
  print()

  #repeat the message for half of the time of what user input
  for level in range (0, level + 1, 2):
    print("Beep's brightness level:", "*" * level)
    print("Bop's brightness level:", "*" * level)
    print()

  print("Adjustments complete!")
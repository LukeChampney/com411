#define a function
def run():
  
  print("How many cables should I remove?")
  cables = int(input())

  cablesremoved = 0

  #repeat the message until cablesremoved is no longer smaller than cables
  while (cablesremoved < cables):
    cablesremoved += 1
    print("Removed Cable.")

#define a function
def run():  

  #print a question
  print("How many bars should be charged?")
  bars = int(input())

  chargedbars = 0

  #repeat the message but the bars is added each time until chargedbars match with bars
  while (chargedbars < bars):
    print("Charging:", end="")
    chargedbars += 1
    print("█" * chargedbars)

  print()
  print("The battery is fully charged.")
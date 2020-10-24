#define a function
def run():

  #print a question
  print("How many mountains should I display?")
  amount = int(input())
  print("Displaying...")

  #repeats for whatever user wants to repeat
  for amount in range(amount):
    print("""
             __
            /  \\_  
           /^    \\
          /  ^    \\_
        _/ ^ ^     ^\\
      /  ^     ^    \\
      """)
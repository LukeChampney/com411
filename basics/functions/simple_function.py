#creates a  function
def listen():
  #print a question
  print("What sound did I hear?")
  #saves user answer as a variable
  sound = input()

  #prints an output
  print("That was a loud {}!" .format(sound))

#use function
listen()
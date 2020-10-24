#define a function
def run():
  
  #print a question
  print("Please enter a sequence")
  sequence = input()

  print("Please enter the character for the marker")
  marker = input()

  #looking for marker1 and marker2
  marker1 = -1
  marker2 = -1

  for position in range(0, len(sequence), 1):
    letter = sequence[position]

    #checks if the letter match with marker
    if (letter == marker):
      if (marker1 == -1):
        marker1 = position
      else:
        marker2 = position

  #caluclation to work out the distance between 2 marker
  distance = marker2 - marker1 - 1

  #displays output
  print("The distance between the markers is {}" .format(distance))
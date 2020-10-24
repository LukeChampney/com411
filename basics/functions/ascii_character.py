#define a function
def run():

  #display message for user to read
  print("Program Started!")
  print("Please enter an ASCII code:")
  number = int(input())

  #making the number into positive if number is negative
  positive = abs(number)

  #check if the number is in range between 32 to 126
  if positive in range(33, 126):

    #coverts from number to asciicode
    asciicode = chr(positive)
  
    #prints the answer with number and asciicode
    print("The character represented by the ASCII code {} is: {}" .format(number, asciicode))

  #made this as an execption because space is 'invisible'
  elif positive == 32:
    print("The character represented by the ASCII code {} is: Space" .format(number))


  #if number is not in between 32 to 126 displays error
  else:
    print("Error")
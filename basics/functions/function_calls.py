#define a function
def run():

  #define a function with single parameter
  def inabox(word):
    #making a box in ascii art
    num_dashes = 4 + len(word)
    print("-" * num_dashes)
    print("| {} |".format(word))
    print("-" * num_dashes)

  #define an another function with single parameter
  def lowercase(word):
    #converts answer to lowercase
    print(word.lower())
  
  #define an another function with single parameter
  def uppercase(word):
    #converts answer to uppercase
    print(word.upper())

  #define an another function with single parameter
  def mirrored(word):
    #making answer mirrored
    reverse = ""
    for letter in reversed(word):
      reverse += letter

    print("{} | {}" .format(word, reverse))
    
  #define an another function with single parameter
  def repeatedword(word):
    #print a question
    print("How many times should the word be displayed?")
    repetitions = int(input())
  
    #making for loop for limited amount of time
    for repetition in range(repetitions):
      #if repetition is even then make answer lowercase
      if (repetition % 2 == 0):
        print(lowercase(word))
      #if repetition is odd then make answer uppercase
      else:
        print(uppercase(word))



  #define a function
  def run():
    #print a question
    print("Enter a word")
    word = str(input())

    #print multiple textline for user to choose
    print("1) Display in a Box – display the word in an ascii art box")
    print("2) Display Lower-case – display the word in lower-case e.g. hello")
    print("3) Display Upper-case – display the word in upper-case e.g. HELLO")
    print("4) Display Mirrored – display the word with its mirrored word e.g. Hello | olleH")
    print("5) Repeat – ask the user how many times to display the word and then display the word that many times alternating between upper-case and lower-case.")
  
    #ask user to give me a number
    number = int(input())
  
    #if the number match then run the following function
    if number == 1:
      inabox(word)

    elif number == 2:
      lowercase(word)
  

    elif number == 3:
      uppercase(word)

    elif number == 4:
      mirrored(word)

    elif number == 5:
      repeatedword(word)

    #if the number doesn't match then print error
    else:
      print("Error")
    
  #calls the function
  run()
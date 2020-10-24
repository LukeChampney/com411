#define a function
def run():

  #define a function
  def play_guess_the_number():
    import random
    print("Please enter the minimum value:")
    min = int(input())
  
    print("Please enter the maximum value:")
    max = int(input())
    
    #choose a number between chosen range 
    randomnumber = random.randrange(min, max)
  
    print("I am thinking of a number between {} and {}.".format(min, max))
    print("Can you guess what it is?")
  
    guess = 0

    #runs this loop forever until guess == randomnumber
    while(guess != randomnumber):
      print("Please enter a number:")
      guess = int(input())
    
      if (guess == randomnumber):
        print("Congratulations!")
        #breaks the loop when number match
        break
      
      #if guess is lower than randomnumber then print the following message and starts the loop again
      elif (guess < randomnumber):
        print("Guess higher")
      
      #if guess is higher than randomnumber then print the following message and starts the loop again
      else:
        print("Guess lower")
  
    #once the user guessed the number print the followimg message
    print("Game over!")

  #calls a function
  play_guess_the_number()
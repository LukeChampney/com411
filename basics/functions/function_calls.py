def inabox(word):
  num_dashes = 4 + len(word)
  print("-" * num_dashes)
  print("| {} |".format(word))
  print("-" * num_dashes)

def lowercase(word):
  print(word.lower())
  
def uppercase(word):
  print(word.upper())

def mirrored(word):
  reverse = ""
  for letter in reversed(word):
    reverse += letter

  print("{} | {}" .format(word, reverse))
    

def repeatedword(word):
  print("How many times should the word be displayed?")
  repetitions = int(input())
  
  for repetition in range(repetitions):
        if (repetition % 2 == 0):
            print(lowercase(word))
        else:
            print(uppercase(word))

#?

#created a function
def run():
  print("Enter a word")
  word = str(input())

  print("1) Display in a Box – display the word in an ascii art box")
  print("2) Display Lower-case – display the word in lower-case e.g. hello")
  print("3) Display Upper-case – display the word in upper-case e.g. HELLO")
  print("4) Display Mirrored – display the word with its mirrored word e.g. Hello | olleH")
  print("5) Repeat – ask the user how many times to display the word and then display the word that many times alternating between upper-case and lower-case.")
  
  #ask user to give me a number
  number = int(input())
  

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

  else:
    print("Error")
    

run()
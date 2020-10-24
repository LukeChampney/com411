#define a function
def run():

  #print a question
  print("What type of book is this?")
  booktype = input()
  #if the answer match then print the following message
  if booktype == ("adventure"):
    print("I like {} books!" .format(booktype))


  print("Finished reading {} book" .format(booktype))
#created a function with single parameter
def escape_by(plan):

  #displays message depending on parameter plan's value
  if plan == "jumping over":
    print("We cannot escape that way! The boulder is too big!")
  elif plan == "running around":
    print("We cannot escape that way! The boulder is moving too fast!")
  elif plan == "going deeper":
    print("That might just work! Let's go deeper!")
  
  else:
    print("I don't know.. this plan sounds kinda stupid")

#use function
escape_by("jumping over")
escape_by("running around")
escape_by("going deeper") 

print("Which path should i take? (left, middle or right)")
direction = str(input())






print("What type of adventure do you want to go on?")
adventure = str(input())

if ((adventure == "short") or (adventure == "scary")):
    print("Entering the dark forest!")

if ((adventure == "long") or (adventure == "safe")):
    print("Taking the safe route!")

else:
  print("Not sure which route to take.")


  print("What did I hear?")
hear = input()
print("What did I see?")
see = input()
    
if ((hear == "grrr") and (see == "two red eyes")):
    print("There is a scary creature. I should get out of here!")
else:
    print("I am a little scared but I will continue.")
    

print("Where should I look?")
place = str(input())

if place == ("in the bedroom"):
    print("Where in the bedroom should I look?")
    bed = input()

    if (bed == "under the bed"):
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery")

if place == ("in the bathroom"):
    print("Where in the bathroom should I look?")
    bed = input()

    if (bed == "in the bathtub"):
        print("Found a rubber duck but no battery")
    else:
        print("Found a wet surface but no battery")

if place == ("in the lab"):
    print("Where in the lab should I look?")
    bed = input()

    if (bed == "on the table"):
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery.")



else:
    print("I do not know where that is but I will keep looking.")


    print("Towards which direction should I paint (up, down, left or right)?")
answer = input()

if answer == ("up"):
  print("I am painting in the upward direction!")

elif answer == ("down"):
   print("I am painting in the downward direction!")

elif answer == ("left"):
   print("I am painting in the westward direction!")

elif answer == ("right"):
   print("I am painting in the eastward direction!")

else:
  print("I don't understand")

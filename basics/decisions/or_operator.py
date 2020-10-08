print("What type of adventure do you want to go on?")
adventure = str(input())

if ((adventure == "short") or (adventure == "scary")):
    print("Entering the dark forest!")

if ((adventure == "long") or (adventure == "safe")):
    print("Taking the safe route!")

else:
  print("Not sure which route to take.")
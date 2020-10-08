
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
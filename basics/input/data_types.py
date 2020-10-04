print("What is your name human?")
name = str(input())

print("How old are you (in years)?")
age = int(input())

print("How tall are you (in meters)?")
height = float(input())

print("How much do you weigh (in kilograms)?")
weight = float(input())

BMI = weight / (height**2)

print("Your name is {} and you are {} years old and your BMI is {:.2f}" .format(name, age, BMI))
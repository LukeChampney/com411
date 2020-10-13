#display message for user to read
print("Program Started!")
print("Please enter a letter:")

#making their answer into variable
letter = input()

#check if their answer has only one character
if len(letter) == 1:
  
  #converts their letter into ascii code
  asciicode = ord(letter)
  #prints the output with their answer and ascii code
  print("The ASCII code for {} is: {}" .format(letter, asciicode))

#if put more/less than one charcter will display error
else:
  print("error")


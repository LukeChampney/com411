def run():

  import matplotlib.pyplot as plt
  import random as rnd

  def data():
    paths = {}
    print("What type of line would you like? (:, -- or -)")
    responseline = input()
    print("What colour your line will be? (r, g or b)")
    responsecolour = input()
    print("what style of marker would you like? (o, s or ^)")
    responsestyle = input()
    paths["responseline"] = responseline
    paths["responsecolour"] = responsecolour
    paths["responsestyle"] = responsestyle
    return paths

  def generate():
    print("How many lines would you like to display?")
    responsecount = int(input())
    for count in range(responsecount):
      values = data()
      x = rnd.sample(range(1, 10), 5)
      y = rnd.sample(range(1, 10), 5)
      format = f"{values['responsecolour']}{values['responseline']}{values['responsestyle']}"
      plt.plot(x, y, format)
  
    plt.show()

  def run():
    print("Running...")
    generate()
    print("Done!")
  
  run()

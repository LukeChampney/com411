def run():

  import matplotlib.pyplot as plt

  def display(x, y):
    plt.plot(x, y)
    plt.show()

  def run():
    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 4, 9, 16, 25]
    plt.plot(x_values, y_values)
    plt.show()

    display(x_values, y_values)

  run()

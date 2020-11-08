def run():

  def likelihood():
    likelihoods = (50,38,27,99,4)
    return (min(likelihoods), max(likelihoods))

  def run():
    minmax = likelihood()
    print("Minimum likelihood of falling: {}%" .format(minmax[0]))
    print("Maximum likelihood of falling: {}%" .format(minmax[1]))

  run()
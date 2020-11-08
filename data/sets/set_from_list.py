def run():
  def observed():
    observations = []

    for count in range(7):
      print("Please enter an observation:")
      answer = input()
      observations.append(answer)

    return observations

  def run():
    print("Counting observations...")
    print("")
    userlist = observed()

    observations_set = set()
    for observation in userlist:
      data = (observation, userlist.count(observation))
      observations_set.add(data)

    for data in sorted(observations_set):
      print("{} is observed {} times" .format(data[0], data[1]))

  run()
def run():
  
  def steps():
    stepsinfo = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
    return stepsinfo

  def run():
    stepsinfo = steps()
    good_steps = []
    bad_steps = []
  
    for step in stepsinfo:
      if (step[1] >= 50):
        bad_steps.append(step)
      else:
        good_steps.append(step) 

    print("Good steps: {}, Bad steps: {}" .format(len(good_steps), len(bad_steps)))

  run()
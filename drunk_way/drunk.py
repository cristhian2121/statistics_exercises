import random

class Drunk:

  def __init__(self, name):
    self.name = name
  
class TraditionalDrunk(Drunk):
  def __init__(self, name):
    super().__init__(name)
  
  def walk(self):
    """Move drunk"""
    return random.choice([
      (0,1),
      (0,-1),
      (1,0),
      (-1,0)
    ])

class PastusoDrunk(Drunk):
  def __init__(self, name):
    super().__init__(name)
  
  def walk(self):
    """Move drunk"""
    return random.choice([
      (random.random(), random.random() * -1),
      (random.random() * -1, random.random()),
      (random.random() * -1, random.random() * -1),
      (random.random(), random.random()),
    ])

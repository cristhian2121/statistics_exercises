from .drunk import Drunk

class Field:

  def __init__(self):
    self.drunk_position = {}

  def add_drunk(self, drunk, coord):
    self.drunk_position[drunk] = coord
  
  def move_drunk(self, drunk: Drunk):
    delt_x, delt_y = drunk.walk()
    current_position = self.drunk_position[drunk]
    new_position = current_position.move(delt_x, delt_y)

    self.drunk_position[drunk] = new_position
  
  def get_position(self, drunk):
    return self.drunk_position[drunk]


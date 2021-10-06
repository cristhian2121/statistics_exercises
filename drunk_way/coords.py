class Coord:

  def __init__(self, x: int, y: int):
    self.x = x
    self.y = y
  
  def move(self, delt_x: int, delt_y: int):
    return Coord(
      self.x + delt_x,
      self.y + delt_y
    )
  
  def distance(self, coord) -> float:
    delt_x = coord.x - self.x
    delt_y = coord.y - self.y

    return (delt_x**2 + delt_y**2)**0.5
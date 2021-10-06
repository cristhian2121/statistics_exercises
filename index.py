# py modules
import random
from bokeh.plotting import figure, show
# ower modules
from drunk_way import Coord, Field, TraditionalDrunk, PastusoDrunk

def plot(x: list, y: list):
  plot = figure(
    title="Drunk way",
    x_axis_label="Steps",
    y_axis_label="Distance"
  )
  plot.line(x, y, legend_label="The drunk way")
  show(plot)

def walking(field, drunk, steps):
  start = field.get_position(drunk)

  for _ in range(steps):
    field.move_drunk(drunk)
  
  return start.distance(field.get_position(drunk))

def simulate_walk(steps, tries: int, drunk_type):
  drunk = drunk_type(name="Michael")
  origin = Coord(0 ,0)
  distance = []

  for _ in range(tries):
    field = Field()
    field.add_drunk(drunk, origin)
    simulate_walk = walking(field, drunk, steps)
    distance.append(round(simulate_walk, 1))

  return distance

def main(distance, tries, drunk_type):
  average_by_walking = []

  for steps in distance:
    distances = simulate_walk(steps, tries, drunk_type)
    average_distance = round(sum(distances) / len(distances), 4)
    max_distance = max(distances)
    min_distance = min(distances)
    average_by_walking.append(average_distance)

    print(f'{drunk_type.__name__} walked {steps}')
    print("--- Distance data ---")
    print(f'Average: {average_distance}')
    print(f'Max: {max_distance}')
    print(f'Mix: {min_distance}')

  plot(distance, average_by_walking)

if __name__ == "__main__":
  distance = [10, 100, 1000, 10000]
  tries = 100

  main(distance, tries, PastusoDrunk)
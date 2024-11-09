from y_2015.d3.puzzle_input import puzzle_input
import copy

SANTA = "santa"
ROBOT = "robot"
LOCATION = 'location'
HOUSES = 'houses'

def update_location(location, direction):
  x, y = location
  if direction == "^":
    location[1] = y + 1
  elif direction == "v":
    location[1] = y - 1
  elif direction == ">":
    location[0] = x + 1
  elif direction == "<":
    location[0] = x - 1
  return location

"""
Starts at staring location
north = ^
south = v
east = >
west = <

How many houses receive at least one present?
(starting location gets present automatically)
"""
def puzzle_solution_part_1(input):
  current_location = [0,0]
  houses = {f'{current_location}': None}

  for direction in input:
    current_location = update_location(
      current_location,
      direction
    )

    houses .setdefault(
      f"{current_location}",
      None
    )

  return len(houses.keys())



def puzzle_solution_part_2(input):
  default_data = {
    LOCATION:[0,0],
    HOUSES: {f'{[0,0]}': None}
  }

  data = {
    SANTA: copy.deepcopy(default_data),
    ROBOT: copy.deepcopy(default_data)
  }

  santa_turn = True

  for direction in input:
    deliverer = SANTA


    if not santa_turn:
      deliverer = ROBOT

    current_location = data[deliverer][LOCATION]

    current_location = update_location(
        current_location,
        direction
    )

    data[deliverer][LOCATION] = current_location

    data[deliverer][HOUSES].setdefault(
        f"{current_location}",
        None
    )

    santa_turn = not santa_turn

  santa_houses = data[SANTA][HOUSES].keys()
  robot_houses = data[ROBOT][HOUSES].keys()

  return len({*santa_houses, *robot_houses})

if __name__ == "__main__":
  print(
    'Printing Puzzle Solutions',
    f'* Part 1: {repr(puzzle_solution_part_1(puzzle_input))}',
    f'* Part 2: {repr(puzzle_solution_part_2(puzzle_input))}',
    sep='\n'
  )

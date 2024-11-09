from y_2015.d3.puzzle_input import puzzle_input
import copy

SANTA = "santa"
ROBOT = "robot"
LOCATION = 'location'
HOUSES = 'houses'

starting_location = [0,0]

default_data = {
  LOCATION: starting_location,
  HOUSES: {f'{starting_location}': None}
}

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
  current_loc = [0,0]
  houses = {f'{current_loc}': None}

  for direction in input:
    current_loc = update_location(
      current_loc,
      direction
    )

    houses.setdefault(
      f"{current_loc}",
      None
    )

  return len(houses.keys())



def puzzle_solution_part_2(input):
  data = {
    SANTA: copy.deepcopy(default_data),
    ROBOT: copy.deepcopy(default_data)
  }

  santa_turn = True

  for direction in input:
    deliverer = SANTA if not santa_turn else ROBOT

    current_loc = data[deliverer][LOCATION]

    current_loc = update_location(
        current_loc,
        direction
    )

    data[deliverer][LOCATION] = current_loc

    data[deliverer][HOUSES].setdefault(
        f"{current_loc}",
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

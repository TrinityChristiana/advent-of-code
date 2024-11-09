import copy

from .puzzle_input import puzzle_input

SANTA = "santa"
ROBOT = "robot"
LOCATION = 'location'
HOUSES = 'houses'

starting_location = [0,0]

default_data = {
  LOCATION: copy.deepcopy(starting_location),
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
--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
"""
def puzzle_solution_part_1(input):
  current_loc = copy.deepcopy(starting_location)
  houses = {f'{starting_location}': None}

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

"""
--- Part Two ---

The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
"""
def puzzle_solution_part_2(input):
  data = {
    SANTA: copy.deepcopy(default_data),
    ROBOT: copy.deepcopy(default_data)
  }

  santa_turn = True

  for direction in input:
    deliverer = SANTA if santa_turn else ROBOT

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

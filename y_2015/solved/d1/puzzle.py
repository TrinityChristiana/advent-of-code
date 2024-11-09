from .puzzle_input import puzzle_input

up = "("
down = ")"

"""
Ground floor = 0

( = up one floor
) = down one floor
"""
def puzzle_solution(input):
  ups = input.count(up)
  downs = input.count(down)
  return ups - downs

def puzzle_solution_2(input):
  position = 0
  index = 0
  input_length = len(input)
  values = {
    up: 1,
    down: -1
  }
  while index < input_length and position != -1:
    move = input[index]
    position += values[move]
    index += 1

  return index

if __name__ == "__main__":
  print(puzzle_solution(puzzle_input))
  print(puzzle_solution_2(puzzle_input))

from .puzzle_input import puzzle_input

up = "("
down = ")"


"""
  --- Day 1: Not Quite Lisp ---

  Santa was hoping for a white Christmas, but his weather machine's "snow" function is powered by stars, and he's fresh out! To save Christmas, he needs you to collect fifty stars by December 25th.

  Collect stars by helping Santa solve puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

  Here's an easy puzzle to warm you up.

  Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

  An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

  The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

  For example:

  (()) and ()() both result in floor 0.
  ((( and (()(()( both result in floor 3.
  ))((((( also results in floor 3.
  ()) and ))( both result in floor -1 (the first basement level).
  ))) and )())()) both result in floor -3.
  To what floor do the instructions take Santa? 74
"""
def puzzle_solution_part_1(input):
  ups = input.count(up)
  downs = input.count(down)
  return ups - downs


"""
  --- Part Two ---

  Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

  For example:

  ) causes him to enter the basement at character position 1.
  ()()) causes him to enter the basement at character position 5.
  What is the position of the character that causes Santa to first enter the basement? 1795
"""
def puzzle_solution_part_2(input):
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
  print(
    'Printing Puzzle Solutions',
    f'* Part 1: {repr(puzzle_solution_part_1(puzzle_input))}',
    f'* Part 2: {repr(puzzle_solution_part_2(puzzle_input))}',
    sep='\n'
  )

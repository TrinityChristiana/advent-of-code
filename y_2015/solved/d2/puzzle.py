from y_2015.solved.d2.puzzle_input import puzzle_input

def convert_dimensions_list(dimension_str):
  return [
    [
      int(leng)
        for leng in dim.split("x")
    ]
      for dim in dimension_str.split("\n")
  ]

"""
l * w * h is format

surface area of the box, which is 2*l*w + 2*w*h + 2*h*l
add the area of the smallest side.
"""
def puzzle_solution_part_1(input):
  total_paper_needed = 0
  # Seperate string into list of lists [[l,w,h]]
  dimension_list = convert_dimensions_list(input)

  for [l, w, h] in dimension_list:
    # loop and grab out l*w
    # loop and grab out w*h
    # loop and grab out h*l
    lw, wh, hl = [l * w, w * h, h * l]

    # Find smalleest value
    smallest_area = min(lw, wh, hl)
    box_surface_ares = (2 * lw) + (2 * wh) + (2 * hl)

    paper_needed = box_surface_ares + smallest_area

    total_paper_needed += paper_needed
    # Add smallest value
  return total_paper_needed


def puzzle_solution_part_2(input):
  total_ribbon = 0
  dimension_list = convert_dimensions_list(input)

  for dims in dimension_list:
    dims.sort()
    first, second = dims[:2]
    ribbon = first * 2 + second * 2 + dims[0] * dims[1] * dims[2]
    total_ribbon += ribbon

  return total_ribbon

if __name__ == "__main__":
  print(
    'Printing Puzzle Solutions',
    f'* Part 1: {repr(puzzle_solution_part_1(puzzle_input))}',
    f'* Part 2: {repr(puzzle_solution_part_2(puzzle_input))}',
    sep='\n'
  )

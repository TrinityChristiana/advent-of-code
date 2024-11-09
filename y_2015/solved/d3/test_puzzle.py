from .puzzle import puzzle_solution_part_1, puzzle_solution_part_2
import pytest


@pytest.mark.parametrize("input, expected_result", [
    (">", 2),
    ("^>v<", 4),
    ("^v^v^v^v^v", 2),

])
def test_puzzle_part_1(input, expected_result):
    assert puzzle_solution_part_1(input) == expected_result


@pytest.mark.parametrize("input, expected_result", [
    ("^v", 3),
    ("^>v<", 3),
    ("^v^v^v^v^v", 11),
])
def test_puzzle_part_2(input, expected_result):
    assert puzzle_solution_part_2(input) == expected_result

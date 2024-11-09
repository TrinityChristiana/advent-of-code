from .puzzle import puzzle_solution_part_1, puzzle_solution_part_2
import pytest


@pytest.mark.parametrize("input, expected_result", [
    ("", ""),
])
def test_puzzle_part_1(input, expected_result):
    assert puzzle_solution_part_1(input) == expected_result


@pytest.mark.parametrize("input, expected_result", [
    ("", ""),
])
def test_puzzle_part_2(input, expected_result):
    assert puzzle_solution_part_2(input) == expected_result

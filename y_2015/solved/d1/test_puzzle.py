from .puzzle import puzzle_solution, puzzle_solution_2
import pytest


@pytest.mark.parametrize("input, expected_result", [
    ("(())", 0),
    ("()()", 0),
    ("(((", 3),
    ("(()(()(", 3),
    ("))(((((", 3),
    ("())", -1),
    ("))(", -1),
    (")))", -3),
    (")())())", -3),
])
def test_puzzle(input, expected_result):
    assert puzzle_solution(input) == expected_result

@pytest.mark.parametrize("input, expected_result", [
    (")", 1),
    ("()())", 5),
])
def test_puzzle_2(input, expected_result):
    assert puzzle_solution_2(input) == expected_result

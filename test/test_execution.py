from pathlib import Path

import pytest

from mars_rover.move_executor import InvalidCommandError

PROJECT_DIR = Path(__file__).parents[0]


def has_state(robot, state):
    return robot.__str__() == state


def test_input_read(executor):
    state, instructions = executor.read_input(f"{PROJECT_DIR}/inputs/read_file.txt")
    assert state == "0 0"
    assert instructions == ["(0, 0, N) RRR"]


def test_state_parse(executor):
    state = executor.parse_state("(0, 0, N)")
    assert state.x == 0
    assert state.y == 0
    assert state.orientation == "N"


def test_invalid_input(executor):
    with pytest.raises(InvalidCommandError):
        executor.execute(f"{PROJECT_DIR}/inputs/invalid.txt")


def test_movement_from_default_file(executor):
    executor.execute("./input.txt")
    assert has_state(executor.world.robots[0], "(4, 4, E)")
    assert has_state(executor.world.robots[1], "(0, 4, W) LOST")


def test_movement_one_lost(executor):
    executor.execute(f"{PROJECT_DIR}/inputs/one_lost.txt")
    assert has_state(executor.world.robots[0], "(2, 3, W)")
    assert has_state(executor.world.robots[1], "(1, 0, S) LOST")


def test_movement_left_lost(executor):
    executor.execute(f"{PROJECT_DIR}/inputs/left_lost.txt")
    assert has_state(executor.world.robots[0], "(0, 3, W) LOST")


def test_movement_right_lost(executor):
    executor.execute(f"{PROJECT_DIR}/inputs/right_lost.txt")
    assert has_state(executor.world.robots[0], "(3, 3, E) LOST")


def test_movement_top_lost(executor):
    executor.execute(f"{PROJECT_DIR}/inputs/top_lost.txt")
    assert has_state(executor.world.robots[0], "(1, 2, N) LOST")


def test_movement_bottom_lost(executor):
    executor.execute(f"{PROJECT_DIR}/inputs/bottom_lost.txt")
    assert has_state(executor.world.robots[0], "(2, 0, S) LOST")


def test_movement_long_valid(executor):
    executor.execute(f"{PROJECT_DIR}/inputs/long_valid.txt")
    assert has_state(executor.world.robots[0], "(8, 8, N)")


def test_movement_many_valid(executor, expected_results_many_valid):
    executor.execute(f"{PROJECT_DIR}/inputs/many_valid.txt")
    for i, result in enumerate(expected_results_many_valid):
        assert has_state(executor.world.robots[i], result)


def test_movement_many_lost(executor, expected_results_many_lost):
    executor.execute(f"{PROJECT_DIR}/inputs/many_lost.txt")
    for i, result in enumerate(expected_results_many_lost):
        assert has_state(executor.world.robots[i], result)

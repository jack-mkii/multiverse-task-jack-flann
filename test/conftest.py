import pytest

from mars_rover.robot import Robot, Position


@pytest.fixture(scope="function")
def robot():
    return Robot(Position(0, 0), "N", limits=Position(3, 3))


@pytest.fixture()
def expected_results_many_valid():
    return [
        "(1, 1, S)",
        "(1, 2, E)",
        "(3, 1, E)",
        "(4, 0, E)",
        "(5, 3, E)",
        "(5, 2, S)",
        "(4, 4, W)"
    ]


@pytest.fixture()
def expected_results_many_lost():
    return [
        "(0, 0, S) LOST",
        "(1, 0, S) LOST",
        "(0, 3, W) LOST",
        "(5, 3, E) LOST",
        "(5, 5, N) LOST",
        "(5, 2, E) LOST",
        "(5, 5, N) LOST"
    ]

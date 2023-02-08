from mars_rover.robot import Robot, Position


def test_robot_creation():
    robot = Robot(Position(2, 3), "E", limits=Position(10, 10))
    assert robot.position.x == 2
    assert robot.position.y == 3
    assert robot.orientation == "E"
    assert robot.limits.x == 10
    assert robot.limits.y == 10


def test_robot_stringify(robot):
    assert robot.__str__() == "(0, 0, N)"


def test_move_forward(robot):
    assert robot.position.y == 0
    robot.move_forward()
    assert robot.position.y == 1
    assert not robot.is_lost


def test_turn_left(robot):
    robot.turn_left()
    assert robot.orientation == "W"
    assert not robot.is_lost


def test_turn_right(robot):
    robot.turn_right()
    assert robot.orientation == "E"
    assert not robot.is_lost


def test_lose_robot_y(robot):
    # turn around twice and move off bottom of grid
    robot.turn_left()
    robot.turn_left()
    robot.move_forward()

    # assert robot has been lost
    assert robot.is_lost

    # assert we haven't updated the last known position
    assert robot.position.x == 0
    assert robot.position.y == 0
    assert robot.orientation == "S"


def test_lose_robot_x(robot):
    # turn right once and move all the way off right side of grid
    robot.turn_right()
    for _ in range(robot.limits.x + 1):
        robot.move_forward()

    # assert robot has been lost
    assert robot.is_lost

    # assert we haven't updated the last known position
    assert robot.position.x == 3
    assert robot.position.y == 0
    assert robot.orientation == "E"


def test_lost_robot_string(robot):
    robot.turn_left()
    robot.turn_left()
    robot.move_forward()

    assert robot.__str__() == "(0, 0, S) LOST"

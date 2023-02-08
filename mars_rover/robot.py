from mars_rover.constants import ROTATE_LEFT, ROTATE_RIGHT


class Position:
    """
    A class to represent a coordinate position

    Attributes
    ----------
    x : int
        x coordinate
    y : int
        y coordinate
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Robot:
    """
    A class encapsulating robot behaviour (movement & rotation)

    Attributes
    ----------
    position : Position
        coordinate position of the robot
    orientation : str
        compass direction the robot is facing
    limits : position
        world limits (for recognising a lost robot)
    is_lost : bool
        whether the robot is lost
    commands : dict
        available commands based on input
    """
    def __init__(self, position: Position, orientation, limits: Position):
        self.position = position
        self.orientation = orientation
        self.limits = limits
        self.is_lost = False
        self.commands = {
            "F": self.move_forward,
            "L": self.turn_left,
            "R": self.turn_right
        }

    def __str__(self):
        """
        String representation of a robot
        """
        stringified = f"({self.position.x}, " \
                      f"{self.position.y}, {self.orientation})"

        if self.is_lost:
            stringified = f"{stringified} LOST"
        return stringified

    def move_forward(self):
        """
        Update robot coordinates on movement based on orientation;
        set lost if moving outside world limits
        """
        if self.orientation == "N":
            if self.position.y + 1 > self.limits.y:
                self.is_lost = True
                return
            self.position.y += 1
        elif self.orientation == "E":
            if self.position.x + 1 > self.limits.x:
                self.is_lost = True
                return
            self.position.x += 1
        elif self.orientation == "S":
            if self.position.y - 1 < 0:
                self.is_lost = True
                return
            self.position.y -= 1
        else:
            if self.position.x - 1 < 0:
                self.is_lost = True
                return
            self.position.x -= 1

    def turn_left(self):
        """
        Rotate left 90 degrees by updating orientation
        """
        self.orientation = ROTATE_LEFT[self.orientation]

    def turn_right(self):
        """
        Rotate right 90 degrees by updating orientation
        """
        self.orientation = ROTATE_RIGHT[self.orientation]

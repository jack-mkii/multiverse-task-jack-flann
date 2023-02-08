import re

from mars_rover.robot import Robot, Position
from mars_rover.world import World


class MoveExecutor:
    """
    A class to represent execution of robot movement

    Attributes
    ----------
    world : World
        The world in which robots are moving
    """
    def __init__(self):
        self.world = None

    @staticmethod
    def read_input(filename):
        """
        Read input file, separating into world state and robot instructions
        """
        with open(filename, "r") as infile:
            content = [x.strip() for x in infile.readlines()]

        world_state = content[0]
        instructions = content[1:]

        return world_state, instructions

    @staticmethod
    def validate(text):
        """
        Raise error if input command not of the form
            (x_coord, y_coord, compass_dir) command_str
        """
        match = re.search(r"^\([0-9]+, [0-9]+, [NESW]\) [FLR]+$", text)
        if not match:
            raise InvalidCommandError(f"Error: \"{text}\" not a valid input")

    @staticmethod
    def parse_state(text):
        """
        Parse the string version of a robot's state into position & orientation
        """
        elements = text.translate({ord(i): None for i in " ()"}).split(",")
        return State(int(elements[0]), int(elements[1]), elements[2])

    def execute(self, filename):
        """
        Execute input from file
        """
        # read text input
        world_state, instructions = self.read_input(filename)

        # create world
        grid = [int(c) for c in world_state.split()]
        self.world = World(grid[0], grid[1])

        # process commands
        for input_str in instructions:
            # ensure command is structured correctly
            self.validate(input_str)

            # separate initial state and commands
            portions = input_str.rsplit(" ", 1)

            state = self.parse_state(portions[0])
            commands = portions[1]

            # create robot
            robot = Robot(
                position=Position(state.x, state.y),
                orientation=state.orientation,
                limits=Position(self.world.width, self.world.height)
            )
            self.world.robots.append(robot)

            # move robot
            for command in commands:
                # stop processing if robot is lost
                if robot.is_lost:
                    break

                # perform command
                robot.commands[command]()

        # finally print each robot's state
        for robot in self.world.robots:
            print(robot)


class State:
    """
    A class to represent a robot's state

    Attributes
    ----------
    x : int
        x coordinate
    y : int
        y coordinate
    orientation: str
        compass direction the robot is facing
    """
    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation


class InvalidCommandError(Exception):
    pass

from typing import List

from mars_rover.robot import Robot


class World:
    """
    A class to represent a world

    Attributes
    ----------
    width : int
        width limit of the world
    height : int
        height limit of the world
    robots : List[Robot]
        list of robots present in the world
    """
    def __init__(self, m, n):
        self.width: int = m
        self.height: int = n
        self.robots: List[Robot] = []

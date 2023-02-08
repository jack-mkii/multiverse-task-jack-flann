from mars_rover.world import World


def test_world_creation():
    world = World(4, 5)
    assert world.width == 4
    assert world.height == 5
    assert world.robots == []

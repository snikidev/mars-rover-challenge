import unittest
from Planet import Planet
from Rover import Rover

mars = Planet(5, 3)


class TestRover(unittest.TestCase):
    def test_execute(self):
        rover = Rover(1, 1, 'E', mars)
        rover.execute('RFRFRFRF')
        x, y = rover.get_position()
        assert((x, y) == (1, 1))
        assert(rover.lost == False)
        assert(rover.direction == 'E')

    def test_execute_lost(self):
        rover = Rover(3, 2, 'N', mars)
        rover.execute('FRRFLLFFRRFLL')
        x, y = rover.get_position()
        assert((x, y) == (3, 3))
        assert(rover.lost == True)
        assert(rover.direction == 'N')


if __name__ == '__main__':
    unittest.main()

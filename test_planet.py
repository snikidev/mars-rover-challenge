import unittest
from Planet import Planet


class TestPlanet(unittest.TestCase):
    def test_scent(self):
        mars = Planet(5, 3)
        mars.add_scent(5, 5)
        mars.add_scent(6, 5)
        assert(mars.print_scents() == [(5, 5), (6, 5)])


if __name__ == '__main__':
    unittest.main()

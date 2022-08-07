class Planet(object):
    """
    Planet class. 
    """

    def __init__(self, x, y):
        """
        Initializes a Planet-object.
        """
        self.x = x
        self.y = y
        self.scent = []

    def add_scent(self, x, y):
        """
        Adds a scent to the planet.
        """
        self.scent.append((x, y))

    def print_scents(self):
        """
        Prints the scents on the planet.
        """
        for scent in self.scent:
            print(scent)
        return self.scent

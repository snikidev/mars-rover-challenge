#!/usr/bin/env python3

from Planet import Planet
from Rover import Rover, DIRECTIONS


def input_planet_size():
    """Read and return width and height of the grid, or raise SystemExit."""

    while True:
        text = input(
            "Please enter the Planet width and height in numbers separated by space (or 'exit'): ")

        if text.lower() == "exit":
            raise SystemExit

        # Validate that the input is actually int's
        try:
            width, height = map(int, text.split(' ')[:2])
        except ValueError:
            print("Those were not numbers. Try again or type 'exit' to finish.")
            continue

        # Continue validation of numbers
        if width > 0 and height > 0 and width <= 50 and height <= 50:
            return width, height


def input_rover_location_and_direction(planet):
    """
    Read x, y and direction from the input and validate the input as well as its relation to the planet
    """

    while True:
        location_and_direction = input(
            "Please enter Rover location in numbers and direaction separated by space (or 'exit'): ")

        if location_and_direction.lower() == "exit":
            raise SystemExit

        # Validate that the input is actually int's
        try:
            x, y, = map(int, location_and_direction.split(' ')[:2])
        except ValueError:
            print("Those were not numbers. Try again or type 'exit' to finish.")
            continue

        if x < 0 or y < 0 or x > 50 or y > 50:
            print(
                "Negative values and values higher than 50 are not allowed. Try again or type 'exit' to finish.")
            continue

        try:
            direction = location_and_direction.split(' ')[2:][0]
        except IndexError:
            print(
                "You didn't provide the direction for the Rover. Try again or type 'exit' to finish.")
            continue

        if not direction.upper() in DIRECTIONS:
            print("Those were not valid directions. Try again or type 'exit' to finish.")
            continue

        return x, y, direction.upper()


def input_commands():
    """
    Read the commands from the input and validate them
    """
    allowed_commands = "LRF"

    while True:
        commands = input("Please enter commands for the Rover (or 'exit'): ")

        if commands.lower() == "exit":
            raise SystemExit

        if (commands.lower() == "exit"):
            return commands
        elif (all(ch.upper() in allowed_commands for ch in commands) and len(commands) <= 100):
            return commands
        else:
            print("Those were not valid commands. Try again or type 'exit' to finish.")
            continue


def main():
    """
    Main function.
    """

    x, y = input_planet_size()

    mars = Planet(x, y)

    while True:
        rover_x, rover_y, direction = input_rover_location_and_direction(
            mars)

        rover = Rover(rover_x, rover_y, direction, mars)

        commands = input_commands()

        rover.execute(commands)

        if (rover.lost):
            x, y = rover.get_position()
            mars.add_scent(x, y)


if __name__ == "__main__":
    main()

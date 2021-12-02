import math

def get_commands():
    with open("./input.txt", "r") as in_file:
        commands = [x.strip() for x in in_file.readlines()]
    return commands

# mapping containing distance modifiers
dist_map = {"forward": [1, 0], "up": [0, -1], "down": [0, 1]}

def parse_commands():
    commands = get_commands()
    # store your position
    pos = [0, 0]
    for command in commands:
        # parse direction and distance from command
        direction, distance = command.split(" ")
        distance = int(distance)
        # finally, apply direction map to distance, and add to current pos
        pos = [coord + (distance * dist_map[direction][i]) for i, coord in enumerate(pos)]
    print(f"Final position is {pos}, answer is {math.prod(pos)}")


if __name__ == "__main__":
    parse_commands()

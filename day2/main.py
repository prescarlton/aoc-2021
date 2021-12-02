import math


def get_commands():
    with open("./input.txt", "r") as in_file:
        commands = [x.strip() for x in in_file.readlines()]
    return [[command.split(" ")[0], int(command.split(" ")[1])] for command in commands]


def part1():
    # mapping containing distance modifiers
    dist_map = {"forward": [1, 0], "up": [0, -1], "down": [0, 1]}
    commands = get_commands()
    # store your position
    pos = [0, 0]
    for command in commands:
        # parse direction and distance from command
        direction, distance = command
        # finally, apply direction map to distance, and add to current pos
        pos = [
            coord + (distance * dist_map[direction][i]) for i, coord in enumerate(pos)
        ]
    print(f"Part 1's final position is {pos}, answer is {math.prod(pos)}")


def part2():
    # mapping for aiming
    AIM_MAP = {"down": 1, "up": -1}
    commands = get_commands()
    # store pos and aim
    pos = [0, 0]
    aim = 0
    for command in commands:
        # parse direction and distance from command
        direction, distance = command
        if direction == "forward":
            pos[0] += distance
            pos[1] += distance * aim
        else:
            aim += AIM_MAP[direction] * distance
    print(f"Part 2's final position is {pos}, product = {math.prod(pos)}")


if __name__ == "__main__":
    part2()

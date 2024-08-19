
dir_increments = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}

next_left = {
    "N": "W",
    "W": "S",
    "S": "E",
    "E": "N",
}

next_right = {
    "N": "E",
    "E": "S",
    "S": "W",
    "W": "N",
}

def isRobotBounded(instructions):
    direction, position = "N", [0, 0]
    for instruction in instructions:
        if instruction == "G":
            position[0] += dir_increments[direction][0]
            position[1] += dir_increments[direction][1]
        elif instruction == "L":
            direction = next_left[direction]
        else:
            direction = next_right[direction]
    return position == [0,0] or direction != "N"


print(isRobotBounded("GGLLGG"))  # True
print(isRobotBounded("GG"))  # False
print(isRobotBounded("GL"))  # True

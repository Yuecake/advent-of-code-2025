"""
You arrive at the secret entrance to the North Pole base ready to start decorating. 
Unfortunately, the password seems to have been changed, so you can't get in. 
A document taped to the wall helpfully explains:

"Due to new security protocols, the password is locked in the safe below. 
Please see the attached document for the new combination."
"""


def parse_instructions_file() -> int:
    """Parses the input to receive instructions line by line, then processes the current position of the dial.
    
    returns: 
        - the final position of the dial after processing the instructions file."""

    # Dial position starts at 0
    current_position = 50
    zero_count = 0

    instructions = "day_one_inputs.txt"

    with open(instructions) as i:
        for line in i:
            print(f"Reading line: {line.strip()}")
            print(f"Current Dial Position: {current_position}")

            direction, distance = split_instruction(line)

            print(f"Resulting instruction: {direction, distance}")

            current_position = turn_dial(current_position, direction, distance)

            if current_position == 0:
                zero_count += 1

    # This should be the FINAL "zero count" for the puzzle
    print(f"The final zero count is: {zero_count}")
    return zero_count


def split_instruction(line: str) -> tuple[str, int]:
    """A function that takes a line from the instructions file and splits the 
    instruction based on first letter and remaining number into a direction and distance.
    
    returns: 
        - the direction and distance of the individual instruction."""

    direction = line[0]
    print(f"The direction is: {direction}")
    distance = line[1:].strip()
    print(f"The distance is: {distance}")

    return direction, int(distance)


def turn_dial(current_position: int, direction: str, distance: int) -> int:
    """Takes the parsed direction and distance from the instructions, and turns the dial 
    in the correct direction and for the correct amount of turns. Utilises modulo (%) to wrap between 0 and 99.
    There are 100 possible positions on the dial 0 -> 99, so we modulo 100.

    returns: 
        - the new current position of the dial."""


    if direction == "L":
        addition = (current_position + distance)
        new_position = addition % 100
    else:
        subtraction = (current_position - distance)
        new_position = subtraction % 100

    return new_position


if __name__ == "__main__":
    parse_instructions_file()

"""
You arrive at the secret entrance to the North Pole base ready to start decorating. 
Unfortunately, the password seems to have been changed, so you can't get in. 
A document taped to the wall helpfully explains:

"Due to new security protocols, the password is locked in the safe below. 
Please see the attached document for the new combination."
"""

from helpers import read_file_lines

def parse_instructions_file() -> int:
    """Parses the input to receive instructions line by line, then processes the current position of the dial.
    
    returns: 
        - the final position of the dial after processing the instructions file."""

    # Dial position starts at 50
    current_position = 50
    final_zero_count = 0
    zeroes_touched_during_calc = 0

    instructions = "day_one_inputs.txt"

    for line in read_file_lines(instructions):
        direction, distance = split_instruction(line)

        zeroes_touched_during_calc = times_dial_passed_zero(current_position, direction, distance)

        current_position = turn_dial(current_position, direction, distance)

        if current_position == 0:
            final_zero_count += 1

    print(f"The final zero count is: {final_zero_count}")
    print(f"The amount of zeroes touched during calc is: {zeroes_touched_during_calc}")
    print(f"The actual total is {final_zero_count + zeroes_touched_during_calc}!")

    return final_zero_count + zeroes_touched_during_calc


def split_instruction(line: str) -> tuple[str, int]:
    """A function that takes a line from the instructions file and splits the 
    instruction based on first letter and remaining number into a direction and distance.
    
    returns: 
        - the direction and distance of the individual instruction."""

    direction = line[0]
    distance = line[1:].strip()

    return direction, int(distance)


def turn_dial(current_position: int, direction: str, distance: int) -> int:
    """Takes the parsed direction and distance from the instructions, and turns the dial 
    in the correct direction and for the correct amount of turns. Utilises modulo (%) to wrap between 0 and 99.
    There are 100 possible positions on the dial 0 -> 99, so we modulo 100.

    returns: 
        - the new current position of the dial."""

    if direction == "R":
        addition = (current_position + distance)
        print(f"Calculating {current_position} + {distance} and it is equal to {addition}")
        new_position = addition % 100

    else:
        subtraction = (current_position - distance)
        print(f"Calculating {current_position} - {distance} and it is equal to {subtraction}")
        new_position = subtraction % 100

    return new_position


def times_dial_passed_zero(current_position: int, direction: str, distance: int) -> int:
    """Calculates how many times 0 is passed when rotating the dial for the next instruction.
    Should not count the zeroes where the dial might start or end on 0.
    
    Handles logic for part 2 of the AoC 2025 day 1.
    
    returns:
        - number of times 0 is passed."""

    total_zeroes_passed = 0

    if direction == "R":
        calculation = current_position + distance 
        zeroes_passed += calculation // 100 # Every complete 100 positions means the dial crossed 0 once
        if calculation % 100 == 0: # minus a zero from calculations that started or have a final landing on 0
            zeroes_passed -= 1
        total_zeroes_passed += zeroes_passed

    else:
        calculation = current_position - distance
        zeroes_passed -= calculation // 100 # The floor division results will be minus numbers, therefore, cancel out the minus to get the result
        if current_position == 0:
            zeroes_passed -= 1 # Minus a zero from the total if the starting position was at 0
        total_zeroes_passed += zeroes_passed

    return total_zeroes_passed


if __name__ == "__main__":
    parse_instructions_file()

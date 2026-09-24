'''As it turns out, one of the younger Elves was playing on a gift shop computer and managed 
to add a whole bunch of invalid product IDs to their gift shop database! Surely, it would be no 
trouble for you to identify the invalid product IDs for them, right?'''

from helpers import read_file_comma_separated_values


def day_two_parse_instructions_file() -> int:

    instructions = "day_two/day_two_inputs.txt"
    
    for value in read_file_comma_separated_values(instructions):
        print(f"The current value is {value}!")


if __name__ == "__main__":
    day_two_parse_instructions_file()


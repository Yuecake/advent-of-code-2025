'''As it turns out, one of the younger Elves was playing on a gift shop computer and managed 
to add a whole bunch of invalid product IDs to their gift shop database! Surely, it would be no 
trouble for you to identify the invalid product IDs for them, right?'''

from helpers import read_file_comma_separated_values


def day_two_parse_instructions_file() -> int:

    instructions = "day_two/day_two_inputs.txt"
    
    for product_id in read_file_comma_separated_values(instructions):
        print(f"The current value is {product_id}!")
        invalid_ids = find_invalid_ids(product_id)
        print(invalid_ids)

def find_invalid_ids(product_id) -> str:

    invalid_ids = []

    # First, check if there are non-unique digits
    if has_repeats(product_id):
        invalid_ids.append(product_id)

    return invalid_ids

def has_repeats(n) -> bool:
    """Checks every individual character in a string and stores to a set. 
    If the set is shorter than the total length, returns True."""

    print(f"The current set: {len(set(n))}")
    print(f"The current ID: {n}")
    print(f"The current total length: {len(n)}")

    return len(set(n)) < len(n)

def add_and_return_invalid_ids(id) -> int:
    pass

if __name__ == "__main__":
    day_two_parse_instructions_file()


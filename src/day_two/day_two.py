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

    # Split the value by the -
    for x in product_id.split('-'):
        print(f"Examining {x} for repeating digits!")
        for n in x:
            if x.count(n) > 0:
                print(f"{x} is a potential culprit!")
                invalid_ids.append(x)

    return invalid_ids

def add_and_return_invalid_ids(id) -> int:
    pass

if __name__ == "__main__":
    day_two_parse_instructions_file()


import re

def parse_user_input(user_input):
    pattern = re.compile(r'(\d+),([A-Za-z]+)\s*([\+\-\*/><=!]+)\s*(\d+),([A-Za-z]+)')
    match = pattern.match(user_input.strip())
    if not match:
        raise ValueError("Invalid input format. Expected format: 'row1,col1 operation row2,col2'")
    row1, col1, operation, row2, col2 = match.groups()
    return (int(row1), col1), (int(row2), col2), operation

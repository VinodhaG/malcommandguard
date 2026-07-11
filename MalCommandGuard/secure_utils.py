import string

#input validation
def is_valid_input(input_str):
    input_str = input_str.strip()

    # Reject empty or too short inputs
    if not input_str or len(input_str) < 3:
        return False

    # Ensure there's at least one alphanumeric character
    if not any(c.isalnum() for c in input_str):
        return False

    # Define disallowed characters
    disallowed_chars = set(";|&`")

    # Check for any disallowed character
    if any(char in disallowed_chars for char in input_str):
        return False

    return True

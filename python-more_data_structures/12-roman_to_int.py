#!/usr/bin/python3
def roman_to_int(roman_string):
    # If the input is not a string or is None, return 0
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Dictionary mapping Roman numeral symbols to their integer values
    roman_map = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }

    total = 0        # final result
    prev_value = 0   # stores the value of the previous numeral (to the right)

    # Loop through the Roman string in reverse (right → left)
    for char in reversed(roman_string):
        # Get the integer value of the current Roman symbol
        value = roman_map.get(char, 0)

        # If the current value is smaller than the one to the right,
        # subtract it (e.g., IV = 5 - 1 = 4)
        if value < prev_value:
            total -= value
        else:
            # Otherwise, add it normally (e.g., VI = 5 + 1 = 6)
            total += value

        # Update prev_value for the next loop step
        prev_value = value

    # Return the computed integer
    return total

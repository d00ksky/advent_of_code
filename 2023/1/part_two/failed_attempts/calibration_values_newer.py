input_file = with open('test2.txt', 'r') as f:
    lines = f.readlines()
    calibration_strings = [entry.strip() for entry in lines]

def get_digits(calibration_str: str) -> int:
    first_digit = None
    last_digit = None
    for character in calibration_str:
        if character.isdigit():
            if first_digit is None:
                first_digit = int(character)
            last_digit = int(character)
    return first_digit * 10 + last_digit


def replace_digit_words(calibration_str: str) -> str:
    character_map = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    extracted_string = list(calibration_str)
    # loop through the string:
    for str_index in range(len(calibration_str)):
        for digit_word, digit_value in character_map.items():
            if calibration_str[str_index:].startswith(digit_word):
                extracted_string[str_index] = str(digit_value)
    return "".join(extracted_string)



def solve_part2(input_file: str) -> int:
    with open(input_file, 'r') as f:
        lines = f.readlines()
        calibration_strings = [entry.strip() for entry in lines]
        adjusted_strings = [replace_digit_words(calibration_str) for calibration_str in calibration_strings]
        calibration_numbers = [get_digits(calibration_str) for calibration_str in adjusted_strings]
        return sum(calibration_numbers)
print(solve_part2(input_file))

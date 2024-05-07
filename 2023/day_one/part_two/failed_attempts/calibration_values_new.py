import re

input_file = input("Enter the name of the file: ")

calibration_values = 0

number_keys = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


search = re.compile(r'\b(one|two|three|four|five|six|seven|eight|nine)\b|\b\d\b')

for line in open(input_file):
    number = []
    values = [] 
    for match in search.findall(line):
        if match.isdigit():
            values.append(int(match))
        elif match and match in number_keys:
            values.append(number_keys[match])
    print(values)
    
    if values:
        first_digit = values[0]
        last_digit = values[-1]

        combined = first_digit * 10 + last_digit
        print(combined)
        calibration_values += combined

print(calibration_values)

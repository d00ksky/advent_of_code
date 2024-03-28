file_path = input("Enter the path of the file: ")

# Initialize the sum of calibration values
total_sum = 0

with open(file_path, 'r') as f:
    for line in f.readlines():
        # Find all digits in the line
        numbers = [char for char in line if char.isdigit()]
        
        # Continue only if there's at least one digit
        if numbers:
            # Construct the calibration value from the first and last digit found
            calibration_value = int(numbers[0] + numbers[-1])
            # Add this value to the total sum
            total_sum += calibration_value

print(total_sum)


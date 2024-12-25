import re

def read_input():
    with open("input.txt", 'r') as input_file:
        lines = input_file.readlines()
    return lines

def get_valid_data(lines):
    regex_pat = r"mul\(\d{1,3},\d{1,3}\)"
    valid_data = []

    for line in lines:
        matches = re.findall(regex_pat, line)
        valid_data.extend(matches)

    return valid_data
    
def multiply_numbers(valid_data):
    total = 0

    for item in valid_data:
        # Extract numbers using regex
        numbers = re.findall(r"\d+", item)
        x, y = int(numbers[0]), int(numbers[1])  # Convert to integers

        # Multiply the numbers
        result = x * y
        print(f"Multiplying {x} and {y}: {result}")

        # Add to total
        total += result

    print(f"{total}")


if __name__ == "__main__":
    lines = read_input()

    valid_data = get_valid_data(lines)
    multiply_numbers(valid_data)

    # print(get_valid_data(lines))

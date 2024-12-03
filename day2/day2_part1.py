import sys

def read_input():
    with open("input.txt", 'r') as input_file:
        lines = input_file.readlines()
    return lines

def determin_safe_level():
    lines = read_input()
    counter = 0

    for line in lines:
        values = list(map(int, line.split()))  # Convert each value in the line to an integer

        for i in range(len(values) -1 ):
            if values[i] > values[i+1] or values[i] < values[i+1]:
                if 0 < abs(values[i]-values[i+1]) < 4:
                    counter += 1
            else:
                print("unsafe")
    print(counter)

if __name__ == '__main__':
    determin_safe_level()